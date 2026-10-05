#!/usr/bin/env python3
# subdataset12_screenshot_human_vs_v2_group_cv
# processed_subdataset12 (screenshot) -- Human-written / V2 -- Group-Based Split
# Usage:  python subdataset12_screenshot_human_vs_v2_group_cv.py                   (results are written to the results/ folder next to this file)
#         python subdataset12_screenshot_human_vs_v2_group_cv.py --split-only      (no training; only the data split is computed and saved)
#         python subdataset12_screenshot_human_vs_v2_group_cv.py --preview 3       (saves sample images as the model sees them; no training)
#         python subdataset12_screenshot_human_vs_v2_group_cv.py --data <folder>   (data folder with the class sub-folders;
#                                               default: <repository>/Data/Subdataset_12)
#
# Changes relative to the original notebook: model-specific ImageNet preprocessing; frozen base, only the last block
# is trained (BatchNorm statistics stay fixed in models with BatchNorm); L2 0.01 -> 1e-4 (the loss stays at the level
# of the pure cross-entropy, which is also tracked as "ce"); early stopping on val_ce with patience 4 +
# ReduceLROnPlateau; input 320x320, NO cropping, antialiased resizing; images are decoded once per run; macro/micro/
# weighted + per-class metrics + MCC/AUC/CE; predictions and training history are saved; mixed precision; old CV
# results are not reused if the settings change; Adam clipnorm=1.0; if the model collapses to a single class on the
# validation set, the training is repeated once with lr/10; a 95% bootstrap confidence interval and the class
# distribution of each set are saved for the test set.
# Class weights: class_weight='balanced' (applied to the training loss; validation loss and metrics are unweighted).
import argparse
import gc
import hashlib
import json
import re
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.model_selection import (GroupShuffleSplit, StratifiedGroupKFold, StratifiedKFold,
                                     train_test_split)
from sklearn.metrics import (accuracy_score, balanced_accuracy_score, classification_report, confusion_matrix,
                             log_loss, matthews_corrcoef, precision_recall_fscore_support, roc_auc_score)

SCRIPT_VERSION = "2026-10-02f"

# =================================================================================================================
# SETTINGS OF THIS RUN
# =================================================================================================================
SUBDATASET = 12
CLASSES = ['human', 'v2']                # label = position in this list (0 = human-written)
SPLIT = "group"                     # "group" = Group-Based Split, "snippet" = Snippet-Level Split
REPRESENTATION, LLM = "screenshot", "GPT-4o"
PROCESS = "Process ID 3 (3-2-4): Code Similarity Detection + Low-Level Common Format Transformation + Screenshot Capture"
EXCLUDE_RE = None   # files in the human-written folder whose names mark an LLM version (misplaced) are not used

MODEL_NAME = "VGG19"
PREPROCESSING = "caffe"              # caffe: VGG/ResNet, tf: Inception/MobileNet/NASNet, torch: DenseNet, raw: EfficientNet
ACTIVATION = "relu"
DROPOUT_RATE = 0.1
LEARNING_RATE = 0.0001
TRAINABLE_FROM = 'block5_'         # the base model is trained from the first layer whose name starts with this prefix
LAST_N_LAYERS = 0                    # if TRAINABLE_FROM is not set: number of last base layers to train
IMG = 320
EPOCHS, PATIENCE, LR_PATIENCE, BATCH = 20, 4, 2, 16
L2 = 1e-4
MIXED = True
DENSE_UNITS = 512
TEST_RATIO, VAL_RATIO, CV_FOLDS, INNER_VAL_RATIO, RANDOM_SEED = 0.15, 0.15, 5, 0.15, 42
MERGE_IDENTICAL_CONTENT = True
MIN_MATCH_RATIO = 0.5
MAX_GROUP_RATIO = 0.75
RATIO_TOLERANCE = 0.03
# =================================================================================================================

_p = argparse.ArgumentParser()
_p.add_argument("--split-only", action="store_true")
_p.add_argument("--preview", type=int, default=0)
_p.add_argument("--data", help="data folder containing the class sub-folders (default: <repository>/Data/Subdataset_N)")
_ARGS = _p.parse_args()

SPLIT_FOLDER = {"snippet": "Snippet-Level Split", "group": "Group-Based Split"}
N_CLASSES = len(CLASSES)
BINARY = N_CLASSES == 2
CLASS_NAMES = ["Human-written"] + [s.upper() for s in CLASSES[1:]]
GROUPED = SPLIT == "group"
KERAS_CLASS_NAME = MODEL_NAME
NAME = "subdataset12_screenshot_human_vs_v2_group_cv"

# ---- Data folder: <repository>/Data/Subdataset_N/{Human-written_raw, v1, ..., v5} (or --data) ----
CLASS_FOLDERS = {"human": "Human-written_raw", "v1": "v1", "v2": "v2", "v3": "v3", "v4": "v4", "v5": "v5"}
REPO_ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = Path(_ARGS.data) if _ARGS.data else REPO_ROOT / "Data" / f"Subdataset_{SUBDATASET}"
if not DATA_DIR.is_dir():
    sys.exit(f"Data folder not found: {DATA_DIR}. Pass the folder that contains the class sub-folders with --data.")
CLASS_DIR = {s: DATA_DIR / CLASS_FOLDERS[s] for s in CLASSES}
OUTPUT_ROOT = Path(__file__).resolve().parent / "results"
RESULT_DIR = OUTPUT_ROOT / NAME
RESULT_DIR.mkdir(parents=True, exist_ok=True)

CONFIG = {
    "script_version": SCRIPT_VERSION, "subdataset": SUBDATASET, "classes": CLASSES, "split": SPLIT,
    "data_folder": f"Data/Subdataset_{SUBDATASET}", "model": MODEL_NAME, "activation": ACTIVATION,
    "dropout": DROPOUT_RATE, "learning_rate": LEARNING_RATE,
    "last_n_layers": None if TRAINABLE_FROM else LAST_N_LAYERS,
    "trainable_from": TRAINABLE_FROM, "base": "frozen, only the last layers are trained",
    "exclude_regex": EXCLUDE_RE, "resizing": "bilinear antialias, uint8, images decoded once per run",
    "preprocessing": PREPROCESSING, "epochs": EPOCHS, "patience": PATIENCE, "early_stopping": "val_ce (min)",
    "lr_reduction": {"monitor": "val_ce", "factor": 0.5, "patience": LR_PATIENCE}, "batch": BATCH,
    "img": IMG, "dense": DENSE_UNITS, "l2": L2, "mixed_precision": MIXED,
    "test_ratio": TEST_RATIO, "val_ratio": VAL_RATIO, "cv_folds": CV_FOLDS, "inner_val_ratio": INNER_VAL_RATIO,
    "clipnorm": 1.0,
    "collapse_check": "if the share of a single class in the validation predictions is >= 0.95, retrain once with lr/10",
    "class_weight": "balanced (computed from the training set of each training run; applied to the training loss only)",
    "seed": RANDOM_SEED, "min_match_ratio": MIN_MATCH_RATIO if GROUPED else None,
    "max_group_ratio": MAX_GROUP_RATIO if GROUPED else None,
}
CONFIG_HASH = hashlib.md5(json.dumps(CONFIG, sort_keys=True).encode()).hexdigest()[:12]


class _Tee:
    """Writes everything printed on the screen to run.log as well."""
    def __init__(self, stream, file):
        self.stream, self.file = stream, file

    def write(self, s):
        self.stream.write(s)
        self.file.write(s)
        self.file.flush()

    def flush(self):
        self.stream.flush()
        self.file.flush()


_log = open(RESULT_DIR / "run.log", "a", encoding="utf-8")
_o, _e = sys.stdout, sys.stderr
while hasattr(_o, "stream"):    # Colab %run: unwrap the redirection of a previous run (so that they do not stack)
    _o = _o.stream
while hasattr(_e, "stream"):
    _e = _e.stream
sys.stdout = _Tee(_o, _log)
sys.stderr = _Tee(_e, _log)
print(f"\n{'=' * 100}\n{time.strftime('%Y-%m-%d %H:%M:%S')}  {NAME}  (config hash {CONFIG_HASH})")

if (RESULT_DIR / "results.json").exists() and not _ARGS.split_only:
    print("results.json already exists -> this run is complete, skipping. To run it again, delete the folder:", RESULT_DIR)
    sys.exit(0)

CONFIG_FILE = RESULT_DIR / "config.json"
if CONFIG_FILE.exists():
    old = json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
    if old.get("config_hash") != CONFIG_HASH:
        sys.exit(f"STOPPED: the previous run in this folder used DIFFERENT settings ({old.get('config_hash')} != {CONFIG_HASH}). "
                 f"Not continuing so that old CV results are not mixed with new ones. Delete or move the folder: {RESULT_DIR}")
CONFIG_FILE.write_text(json.dumps({**CONFIG, "config_hash": CONFIG_HASH}, ensure_ascii=False, indent=2), encoding="utf-8")

print(f"Data    : {DATA_DIR}")
print(f"Classes : {CLASS_NAMES}   Split: {SPLIT_FOLDER[SPLIT]}")
print(f"Model   : {MODEL_NAME}  activation={ACTIVATION}  dropout={DROPOUT_RATE}  lr={LEARNING_RATE:g}  "
      f"trained={'base from ' + TRAINABLE_FROM + '* on' if TRAINABLE_FROM else f'last {LAST_N_LAYERS} layers'}  "
      f"preprocessing={PREPROCESSING}  L2={L2:g}")
print(f"Training: at most {EPOCHS} epochs, early stopping val_ce patience {PATIENCE}, batch {BATCH}, "
      f"{IMG}x{IMG} (no cropping), mixed precision {MIXED}")
print(f"Output  : {RESULT_DIR}")

# ---------------------------------------------------------------------------------------------------------------
# Data: list + label (label = position in CLASSES: 0 = human-written)
# ---------------------------------------------------------------------------------------------------------------
def list_images(folder):
    exts = (".png", ".jpg", ".jpeg")
    return sorted([p for p in Path(folder).glob("*") if p.suffix.lower() in exts], key=lambda p: p.name)


for s in CLASSES:
    assert CLASS_DIR[s].is_dir(), f"Folder not found: {CLASS_DIR[s]}"
class_files = {s: list_images(CLASS_DIR[s]) for s in CLASSES}
excluded = []
if EXCLUDE_RE:
    excluded = [p.name for p in class_files["human"] if re.match(EXCLUDE_RE, p.name)]
    class_files["human"] = [p for p in class_files["human"] if not re.match(EXCLUDE_RE, p.name)]
    print(f"{len(excluded)} files in the human-written folder whose names mark an LLM version were NOT used (data unchanged): {excluded}")
for k, s in enumerate(CLASSES):
    print(f"{CLASS_NAMES[k]:3s} (label {k}): {len(class_files[s])} images")
files = [p for s in CLASSES for p in class_files[s]]
paths = np.array([str(p) for p in files])
labels = np.concatenate([np.full(len(class_files[s]), k) for k, s in enumerate(CLASSES)]).astype(int)
file_names = [p.name for p in files]
n = len(files)
print(f"Total {n} images")


def distribution(ix):
    return " ".join(f"{name}={int((labels[ix] == k).sum())}" for k, name in enumerate(CLASS_NAMES))


# ---------------------------------------------------------------------------------------------------------------
# Data split
# ---------------------------------------------------------------------------------------------------------------
idx_all = np.arange(n)
group_info = {}
if GROUPED:
    def file_digest(p):
        with open(p, "rb") as f:
            return hashlib.md5(f.read()).hexdigest()

    contents = np.array([file_digest(p) for p in files])

    # Group key: [<outer index>_][v<n>_[v<m>_]][space]<index>_content_<author>_<repo>_<file>.py[_cleaned] + extension
    #            -> <author>_<repo>_<file>   (same rule as in the original notebooks)
    NAME_RE = re.compile(r"^(?:(?P<outer>\d+)_)?(?:vs?(?P<version>[1-5])_?\s*)*(?P<index>\d+)_content_(?P<body>.+)$")

    def group_key(file_name):
        s = re.sub(r"\.(png|jpg|jpeg|txt)$", "", str(file_name).strip(), flags=re.IGNORECASE)
        m = NAME_RE.match(s)
        if m is None:
            return None, None
        body = re.sub(r"(?:\.py\w*)+$", "", m.group("body"), flags=re.IGNORECASE)
        return re.sub(r"\s+", "", body).lower(), m.group("version")

    parsed = [group_key(name) for name in file_names]
    unparsed = [name for name, (a, _) in zip(file_names, parsed) if not a]
    assert not unparsed, f"CHECK 1: {len(unparsed)} file names do not match the group pattern: {unparsed[:5]}"
    keys = np.array([a for a, _ in parsed])
    name_versions = [s for _, s in parsed]

    def build_groups(value_arrays):
        parent = list(range(n))

        def find(i):
            while parent[i] != i:
                parent[i] = parent[parent[i]]
                i = parent[i]
            return i

        for array in value_arrays:
            first = {}
            for i, value in enumerate(array.tolist()):
                if value in first:
                    a, b = find(i), find(first[value])
                    if a != b:
                        parent[max(a, b)] = min(a, b)
                else:
                    first[value] = i
        roots = [find(i) for i in range(n)]
        number = {root: k for k, root in enumerate(sorted(set(roots)))}
        return np.array([number[root] for root in roots])

    name_only_groups = build_groups([keys])
    families = build_groups([keys, contents]) if MERGE_IDENTICAL_CONTENT else name_only_groups

    tab = pd.DataFrame({"group": families, "label": labels}).groupby("group")["label"]
    n_classes_in_group = tab.nunique()
    has_human = tab.min() == 0
    n_groups = int(len(n_classes_in_group))
    human_and_version = int((has_human & (n_classes_in_group >= 2)).sum())
    match_ratio = human_and_version / n_groups
    group_info = {"n_groups": n_groups, "groups_with_human_and_version": human_and_version,
                  "groups_with_all_classes": int((n_classes_in_group == N_CLASSES).sum()),
                  "human_only_groups": int((has_human & (n_classes_in_group == 1)).sum()),
                  "groups_without_human": int((~has_human).sum()), "match_ratio": match_ratio,
                  "groups_merged_by_content": int(len(np.unique(name_only_groups)) - n_groups)}
    print(f"Groups: {group_info}")
    assert match_ratio >= MIN_MATCH_RATIO, \
        f"CHECK 2: GROUP KEY DOES NOT WORK (match {100 * match_ratio:.1f}% < {100 * MIN_MATCH_RATIO:.0f}%)"
    assert n_groups <= MAX_GROUP_RATIO * n, f"CHECK 3: number of groups ({n_groups}) is too close to the number of samples ({n})"

    # CHECK 4: every human/version pair found with an independent simple rule must be in the same group
    def simple_core(file_name):
        s = re.sub(r"\s+", "", str(file_name))
        s = re.sub(r"^\d+_(?=(?:v\d_)*\d+_content_)", "", s)
        return re.sub(r"^(?:v\d_)+", "", s)

    human_positions = {}
    for i in np.where(labels == 0)[0]:
        human_positions.setdefault(simple_core(file_names[i]), []).append(i)
    cross_pairs = cross_violations = 0
    for i in np.where(labels != 0)[0]:
        for j in human_positions.get(simple_core(file_names[i]), []):
            cross_pairs += 1
            cross_violations += int(families[i] != families[j])
    print(f"CHECK 4: human/version pairs found with the simple rule {cross_pairs}, in different groups {cross_violations}")
    assert cross_pairs > 0 and cross_violations == 0, "CHECK 4 failed: the group key must be fixed"

    suspicious_labels = [name for name, e, s in zip(file_names, labels, name_versions)
                         if (e == 0 and s is not None) or (e != 0 and s != CLASSES[e].lstrip("v"))]
    group_info["files_with_folder_name_version_mismatch"] = len(suspicious_labels)
    print(f"Files whose folder and version tag in the name do not match (data unchanged): {len(suspicious_labels)}")

    def leakage_check(sets, title):
        to_check = [("group", families), ("group key", keys)]
        if MERGE_IDENTICAL_CONTENT:
            to_check.append(("content", contents))
        names = list(sets)
        for a in range(len(names)):
            for b in range(a + 1, len(names)):
                ia, ib = np.asarray(sets[names[a]]), np.asarray(sets[names[b]])
                assert not set(ia.tolist()) & set(ib.tolist()), f"{title}: {names[a]}/{names[b]} same sample"
                for what, array in to_check:
                    common = set(array[ia].tolist()) & set(array[ib].tolist())
                    assert not common, f"LEAKAGE ({title}): {names[a]}/{names[b]} common {what}: {sorted(common)[:3]}"

    def split_groups(indices, ratio, seed):
        gss = GroupShuffleSplit(n_splits=1, test_size=ratio, random_state=seed)
        a, b = next(gss.split(indices, labels[indices], groups=families[indices]))
        return indices[a], indices[b]

    dev_idx, test_idx = split_groups(idx_all, TEST_RATIO, RANDOM_SEED)
    train_idx, val_idx = split_groups(dev_idx, VAL_RATIO / (1.0 - TEST_RATIO), RANDOM_SEED)
    leakage_check({"train": train_idx, "validation": val_idx, "test": test_idx}, "70/15/15")
    for name, ix, target in (("validation", val_idx, VAL_RATIO), ("test", test_idx, TEST_RATIO)):
        assert abs(len(ix) / n - target) <= RATIO_TOLERANCE, f"{name} ratio {100 * len(ix) / n:.1f}%"
    sgkf = StratifiedGroupKFold(n_splits=CV_FOLDS, shuffle=True, random_state=RANDOM_SEED)
    cv_folds = [(dev_idx[tr], dev_idx[va])
                for tr, va in sgkf.split(dev_idx, labels[dev_idx], groups=families[dev_idx])]
    for fold, (tr, va) in enumerate(cv_folds, start=1):
        leakage_check({"fold train": tr, "fold evaluation": va, "test": test_idx}, f"CV fold {fold}")

    def inner_split(fold_train_idx, fold):
        return split_groups(fold_train_idx, INNER_VAL_RATIO, RANDOM_SEED + fold)
else:
    families = keys = None
    dev_idx, test_idx = train_test_split(idx_all, test_size=TEST_RATIO, random_state=RANDOM_SEED, stratify=labels)
    train_idx, val_idx = train_test_split(dev_idx, test_size=VAL_RATIO / (1.0 - TEST_RATIO),
                                          random_state=RANDOM_SEED, stratify=labels[dev_idx])
    skf = StratifiedKFold(n_splits=CV_FOLDS, shuffle=True, random_state=RANDOM_SEED)
    cv_folds = [(dev_idx[tr], dev_idx[va]) for tr, va in skf.split(dev_idx, labels[dev_idx])]

    def leakage_check(sets, title):
        names = list(sets)
        for a in range(len(names)):
            for b in range(a + 1, len(names)):
                assert not set(np.asarray(sets[names[a]]).tolist()) & set(np.asarray(sets[names[b]]).tolist()), \
                    f"{title}: {names[a]}/{names[b]} contain the same sample"

    leakage_check({"train": train_idx, "validation": val_idx, "test": test_idx}, "70/15/15")

    def inner_split(fold_train_idx, fold):
        return train_test_split(fold_train_idx, test_size=INNER_VAL_RATIO, random_state=RANDOM_SEED + fold,
                                stratify=labels[fold_train_idx])

assert len(train_idx) + len(val_idx) + len(test_idx) == n
assert sorted(np.concatenate([va for _, va in cv_folds]).tolist()) == sorted(dev_idx.tolist())
for name, ix in (("Train", train_idx), ("Validation", val_idx), ("Test", test_idx)):
    print(f"{name:10s}: {len(ix):5d} ({100 * len(ix) / n:.1f}%)  {distribution(ix)}")
    assert len(np.unique(labels[ix])) == N_CLASSES, f"not all {N_CLASSES} classes are present in the {name} set"
for fold, (tr, va) in enumerate(cv_folds, start=1):
    assert len(np.unique(labels[tr])) == N_CLASSES and len(np.unique(labels[va])) == N_CLASSES
    print(f"Fold {fold}: train={len(tr)} ({distribution(tr)})  evaluation={len(va)} ({distribution(va)})")
print("Leakage check PASSED.")

split_table = pd.DataFrame({"file": file_names, "label": labels, "set": ""})
if GROUPED:
    split_table["group"] = families
    split_table["group_key"] = keys
split_table.loc[train_idx, "set"] = "train"
split_table.loc[val_idx, "set"] = "val"
split_table.loc[test_idx, "set"] = "test"
split_table["cv_fold"] = 0
for fold, (_, va) in enumerate(cv_folds, start=1):
    split_table.loc[va, "cv_fold"] = fold
if GROUPED:
    assert split_table.groupby("group")["set"].nunique().max() == 1, "a group is in more than one set"
split_table.to_csv(RESULT_DIR / "data_split.csv", index=False, encoding="utf-8-sig")
if _ARGS.split_only:
    print("--split-only: data split saved, no training was done.")
    sys.exit(0)

# ---------------------------------------------------------------------------------------------------------------
# TensorFlow, model, training
# ---------------------------------------------------------------------------------------------------------------
import os  # noqa: E402

os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "2")   # reduce TF info/warning output
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import seaborn as sns  # noqa: E402
import tensorflow as tf  # noqa: E402

gpus = tf.config.list_physical_devices("GPU")
for g in gpus:
    try:
        tf.config.experimental.set_memory_growth(g, True)
    except RuntimeError as e:
        print(e)
print("TensorFlow", tf.__version__, "| GPU:", gpus if gpus else "NONE (CPU)")
if MIXED and gpus:
    tf.keras.mixed_precision.set_global_policy("mixed_float16")
    print("Mixed precision: mixed_float16 (output layer float32)")
BaseModel = getattr(tf.keras.applications, KERAS_CLASS_NAME)

_CAFFE_MEAN = tf.constant([103.939, 116.779, 123.68])
_TORCH_MEAN = tf.constant([0.485, 0.456, 0.406])
_TORCH_STD = tf.constant([0.229, 0.224, 0.225])


def preprocess(img):
    """img: float32, 0-255, RGB. Same preprocessing as in the model's ImageNet training (keras preprocess_input)."""
    if PREPROCESSING == "caffe":
        return img[..., ::-1] - _CAFFE_MEAN         # RGB -> BGR, channel means are subtracted
    if PREPROCESSING == "tf":
        return img / 127.5 - 1.0                    # [-1, 1]
    if PREPROCESSING == "torch":
        return (img / 255.0 - _TORCH_MEAN) / _TORCH_STD
    return img                                      # EfficientNet: 0-255, scaling is inside the model


def save_preview(count):
    target = RESULT_DIR / "preview"
    target.mkdir(exist_ok=True)
    rng = np.random.default_rng(RANDOM_SEED)
    for k, name in enumerate(CLASS_NAMES):
        for i in rng.choice(np.where(labels == k)[0], size=min(count, int((labels == k).sum())), replace=False):
            img = _load_path(tf.constant(paths[i])).numpy()
            tf.io.write_file(str(target / f"{name}_{Path(file_names[i]).stem[:60]}.png"), tf.io.encode_png(img))
    print(f"Preview: {target} ({IMG}x{IMG})")


def label_array(ix):
    if BINARY:
        return labels[ix].astype("float32").reshape(-1, 1)
    return np.eye(N_CLASSES, dtype="float32")[labels[ix]]


def _load_path(path):
    img = tf.io.decode_image(tf.io.read_file(path), channels=3, expand_animations=False)
    img.set_shape([None, None, 3])
    img = tf.image.resize(tf.cast(img, tf.float32), (IMG, IMG), antialias=True)
    return tf.cast(tf.clip_by_value(tf.round(img), 0.0, 255.0), tf.uint8)


def load_images():
    """All images are decoded and resized ONCE per run (uint8); all trainings read from this array."""
    t0 = time.time()
    array = np.empty((n, IMG, IMG, 3), dtype=np.uint8)
    k = 0
    for chunk in tf.data.Dataset.from_tensor_slices(paths).map(_load_path, num_parallel_calls=tf.data.AUTOTUNE) \
            .batch(64).prefetch(2):
        array[k:k + len(chunk)] = chunk.numpy()
        k += len(chunk)
    assert k == n
    print(f"Images loaded: {n}, {array.nbytes / 1e9:.1f} GB, {time.time() - t0:.0f} s", flush=True)
    return array


IMAGES = None


def make_dataset(indices, training, seed=RANDOM_SEED):
    ds = tf.data.Dataset.from_tensor_slices((np.asarray(indices, dtype="int64"), label_array(indices)))
    if training:
        ds = ds.shuffle(buffer_size=len(indices), seed=seed)
    ds = ds.batch(BATCH)

    def _get(ix, y):
        img = tf.numpy_function(lambda i: IMAGES[i], [ix], tf.uint8)
        img.set_shape([None, IMG, IMG, 3])
        return preprocess(tf.cast(img, tf.float32)), y

    return ds.map(_get, num_parallel_calls=tf.data.AUTOTUNE).prefetch(tf.data.AUTOTUNE)


_MODEL_INFO_PRINTED = False


def create_model(lr=None):
    base = BaseModel(weights="imagenet", include_top=False, input_shape=(IMG, IMG, 3))
    base.trainable = True
    if TRAINABLE_FROM:
        start = next(i for i, l in enumerate(base.layers) if l.name.startswith(TRAINABLE_FROM))
    else:
        start = len(base.layers) - LAST_N_LAYERS if LAST_N_LAYERS > 0 else len(base.layers)
    for layer in base.layers[:start]:
        layer.trainable = False                     # frozen base; only the last layers are trained
    inputs = tf.keras.Input(shape=(IMG, IMG, 3))
    x = base(inputs, training=False)   # in models with BatchNorm (DenseNet/ResNet/Inception/MobileNet/NASNet/
                                       # EfficientNet) the BN statistics stay fixed; VGG has no BN, no effect
    x = tf.keras.layers.GlobalAveragePooling2D()(x)
    x = tf.keras.layers.Dense(DENSE_UNITS, activation=ACTIVATION,
                              kernel_regularizer=tf.keras.regularizers.l2(L2))(x)
    x = tf.keras.layers.Dropout(DROPOUT_RATE)(x)
    if BINARY:
        outputs = tf.keras.layers.Dense(1, activation="sigmoid", dtype="float32")(x)
        loss, ce = "binary_crossentropy", tf.keras.metrics.BinaryCrossentropy(name="ce")
    else:
        outputs = tf.keras.layers.Dense(N_CLASSES, activation="softmax", dtype="float32")(x)
        loss, ce = "categorical_crossentropy", tf.keras.metrics.CategoricalCrossentropy(name="ce")
    model = tf.keras.Model(inputs, outputs)
    global _MODEL_INFO_PRINTED
    if not _MODEL_INFO_PRINTED:
        trained = sum(int(np.prod(w.shape)) for w in model.trainable_weights)
        total = sum(int(np.prod(w.shape)) for w in model.weights)
        print(f"Model: base {len(base.layers)} layers, trained base layers {len(base.layers) - start} "
              f"(first: {base.layers[start].name if start < len(base.layers) else '-'}); "
              f"trained parameters {trained:,} / {total:,}")
        _MODEL_INFO_PRINTED = True
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=lr or LEARNING_RATE, clipnorm=1.0), loss=loss,
                  metrics=["accuracy", ce])
    return model


def probability_matrix(output):
    output = np.asarray(output, dtype="float64")
    if BINARY:
        p = output.reshape(-1)
        return np.stack([1.0 - p, p], axis=1)
    return output


def metrics(y_true, prob):
    y_pred = prob.argmax(axis=1)
    m = {"accuracy": float(accuracy_score(y_true, y_pred)),
         "balanced_accuracy": float(balanced_accuracy_score(y_true, y_pred)),
         "mcc": float(matthews_corrcoef(y_true, y_pred)),
         "cross_entropy": float(log_loss(y_true, prob, labels=list(range(N_CLASSES))))}
    for avg in ("macro", "micro", "weighted"):
        p, r, f1, _ = precision_recall_fscore_support(y_true, y_pred, average=avg, zero_division=0,
                                                      labels=list(range(N_CLASSES)))
        m.update({f"precision_{avg}": float(p), f"recall_{avg}": float(r), f"f1_{avg}": float(f1)})
    p, r, f1, support = precision_recall_fscore_support(y_true, y_pred, average=None, zero_division=0,
                                                        labels=list(range(N_CLASSES)))
    for k, name in enumerate(CLASS_NAMES):
        m.update({f"precision_{name}": float(p[k]), f"recall_{name}": float(r[k]), f"f1_{name}": float(f1[k]),
                  f"support_{name}": int(support[k])})
    try:
        m["roc_auc"] = float(roc_auc_score(y_true, prob[:, 1]) if BINARY else
                             roc_auc_score(y_true, prob, multi_class="ovr", average="macro"))
    except ValueError:
        m["roc_auc"] = float("nan")
    return m


def prediction_table(ix, prob, set_name):
    t = pd.DataFrame({"set": set_name, "file": [file_names[i] for i in ix], "true": labels[ix],
                      "pred": prob.argmax(axis=1)})
    for k, name in enumerate(CLASS_NAMES):
        t[f"prob_{name}"] = prob[:, k]
    return t


COLLAPSE_THRESHOLD = 0.95      # if this share of the validation predictions goes to one class, it counts as a "collapse"


def class_weights(ix):
    """class_weight='balanced' (sklearn): w_k = n / (K * n_k), from the class counts of the TRAINING set of this run.
    Applied to the training loss only; the validation loss (early stopping) and the reported metrics are unweighted."""
    from sklearn.utils.class_weight import compute_class_weight
    w = compute_class_weight("balanced", classes=np.arange(N_CLASSES), y=labels[ix])
    return {int(k): float(v) for k, v in enumerate(w)}


def train_and_evaluate(train_ix, early_stop_ix, eval_ix, seed, training_name):
    """Trains; if the model collapsed to a single class on the validation set, repeats the training once with lr/10."""
    lr = LEARNING_RATE
    weights = class_weights(train_ix)
    print("Class weights (balanced): " + "  ".join(f"{CLASS_NAMES[k]}={v:.3f}" for k, v in weights.items()), flush=True)
    for attempt in (1, 2):
        tf.keras.backend.clear_session()
        gc.collect()
        tf.keras.utils.set_random_seed(seed)
        model = create_model(lr)
        callbacks = [
            tf.keras.callbacks.EarlyStopping(monitor="val_ce", mode="min", patience=PATIENCE,
                                             restore_best_weights=True),
            tf.keras.callbacks.ReduceLROnPlateau(monitor="val_ce", mode="min", factor=0.5,
                                                 patience=LR_PATIENCE, min_lr=1e-7, verbose=1),
        ]
        t0 = time.time()
        history = model.fit(make_dataset(train_ix, training=True, seed=seed),
                            validation_data=make_dataset(early_stop_ix, training=False),
                            epochs=EPOCHS, callbacks=callbacks, verbose=2, class_weight=weights)
        train_sec = time.time() - t0
        val_prob = probability_matrix(model.predict(make_dataset(early_stop_ix, training=False), verbose=0))
        share = float(np.bincount(val_prob.argmax(axis=1), minlength=N_CLASSES).max() / len(early_stop_ix))
        if share < COLLAPSE_THRESHOLD or attempt == 2:
            break
        print(f"COLLAPSE: {100 * share:.0f}% of the validation predictions are in one class -> training is repeated "
              f"once with lr {lr / 10:g}", flush=True)
        lr = lr / 10
        # the model of the first attempt must not keep GPU memory: the model, the history (History.model) and the
        # callbacks (EarlyStopping keeps the best weights) are deleted together
        del model, history, callbacks, val_prob
        tf.keras.backend.clear_session()
        gc.collect()
    h = pd.DataFrame(history.history)
    h.insert(0, "epoch", np.arange(1, len(h) + 1))
    h.insert(0, "attempt", attempt)
    h.insert(0, "training", training_name)

    prob = probability_matrix(model.predict(make_dataset(eval_ix, training=False), verbose=0))
    result = metrics(labels[eval_ix], prob)
    result.update({"val_" + k: v for k, v in metrics(labels[early_stop_ix], val_prob).items()})
    best = int(h["val_ce"].idxmin())
    result.update({"n_epochs": len(h), "best_epoch": best + 1, "best_val_ce": float(h["val_ce"].min()),
                   "train_sec": round(train_sec, 1), "attempt": attempt, "lr_used": lr,
                   "class_weight": json.dumps({CLASS_NAMES[k]: round(v, 4) for k, v in weights.items()}),
                   "val_largest_class_share": share})
    del model
    tf.keras.backend.clear_session()
    gc.collect()
    return result, prob, val_prob, h


def append_csv(df, path, columns=None):
    if columns is not None:
        df = df.reindex(columns=columns)
    df.to_csv(path, mode="a", header=not path.exists(), index=False)


_example = metrics(np.arange(N_CLASSES), np.eye(N_CLASSES))
CV_COLUMNS = (["fold", "n_train", "n_inner_val", "n_eval"] + list(_example) + ["val_" + k for k in _example]
              + ["n_epochs", "best_epoch", "best_val_ce", "train_sec", "attempt", "lr_used", "class_weight",
                 "val_largest_class_share", "error"])


if _ARGS.preview:
    save_preview(_ARGS.preview)
    create_model()      # builds the model and checks the number of trained layers/parameters (no training)
    sys.exit(0)

IMAGES = load_images()

# ---- 5-fold CV (completed folds are skipped; config.json guarantees that the settings are the same) ----
CV_CSV = RESULT_DIR / "cv_fold_results.csv"
HISTORY_CSV = RESULT_DIR / "training_history.csv"
completed = set()
if CV_CSV.exists():
    previous = pd.read_csv(CV_CSV)
    previous = previous[previous["error"].isna() | (previous["error"].astype(str).str.strip() == "")]
    completed = set(int(k) for k in previous["fold"])
    print(f"Previously completed folds: {sorted(completed)} (will be skipped)")

for fold, (fold_train_idx, fold_eval_idx) in enumerate(cv_folds, start=1):
    if fold in completed:
        continue
    print(f"\n===== Fold {fold}/{CV_FOLDS}  {time.strftime('%H:%M:%S')} =====")
    inner_train_idx, inner_val_idx = inner_split(fold_train_idx, fold)
    leakage_check({"inner train": inner_train_idx, "inner validation": inner_val_idx, "fold evaluation": fold_eval_idx,
                   "test": test_idx}, f"CV fold {fold} (inner validation)")
    assert len(np.unique(labels[inner_train_idx])) == N_CLASSES and len(np.unique(labels[inner_val_idx])) == N_CLASSES
    row = {"fold": fold, "n_train": len(inner_train_idx), "n_inner_val": len(inner_val_idx),
           "n_eval": len(fold_eval_idx)}
    try:
        result, prob, _, h = train_and_evaluate(inner_train_idx, inner_val_idx, fold_eval_idx, RANDOM_SEED + fold,
                                                f"fold{fold}")
        row.update(result)
        row["error"] = ""
        append_csv(h, HISTORY_CSV)
        append_csv(prediction_table(fold_eval_idx, prob, f"fold{fold}"), RESULT_DIR / "predictions_cv.csv")
    except Exception as e:
        row["error"] = f"{type(e).__name__}: {e}"[:300]
        tf.keras.backend.clear_session()
        gc.collect()
    append_csv(pd.DataFrame([row]), CV_CSV, CV_COLUMNS)
    print(f"Fold {fold}: accuracy={row.get('accuracy', float('nan')):.4f}  F1(w/m)={row.get('f1_weighted', float('nan')):.4f}/"
          f"{row.get('f1_macro', float('nan')):.4f}  CE={row.get('cross_entropy', float('nan')):.4f}  "
          f"epochs={row.get('n_epochs', '-')}  {row['error']}")

cv = pd.read_csv(CV_CSV)
cv = cv[cv["error"].isna() | (cv["error"].astype(str).str.strip() == "")]
cv = cv.drop_duplicates(subset=["fold"], keep="last").sort_values("fold")
assert len(cv) == CV_FOLDS, f"not all {CV_FOLDS} folds are complete ({len(cv)}); run the script again (it resumes from the missing fold)."
MEASURES = ["accuracy", "balanced_accuracy", "mcc", "cross_entropy", "roc_auc"] + \
           [f"{m}_{o}" for o in ("macro", "micro", "weighted") for m in ("precision", "recall", "f1")]
cv_summary = {m: {"mean": float(cv[m].mean()), "std": float(cv[m].std(ddof=1))} for m in MEASURES}
print("\nCV mean ± std:")
for m in MEASURES:
    print(f"  {m:22s} {cv_summary[m]['mean']:.4f} ± {cv_summary[m]['std']:.4f}")

# ---- Final training: 70% train (+15% validation for early stopping), evaluated once on the 15% test set ----
print(f"\n===== Final training  {time.strftime('%H:%M:%S')} =====")
test_result, test_prob, val_prob, h = train_and_evaluate(train_idx, val_idx, test_idx, RANDOM_SEED, "final")
append_csv(h, HISTORY_CSV)
pd.concat([prediction_table(test_idx, test_prob, "test"), prediction_table(val_idx, val_prob, "validation")]) \
    .to_csv(RESULT_DIR / "predictions.csv", index=False, encoding="utf-8-sig")
y_true, y_pred = labels[test_idx], test_prob.argmax(axis=1)
print(classification_report(y_true, y_pred, target_names=CLASS_NAMES, zero_division=0, digits=4))

cm = confusion_matrix(y_true, y_pred, labels=list(range(N_CLASSES)))
pd.DataFrame(cm, index=CLASS_NAMES, columns=CLASS_NAMES).to_csv(RESULT_DIR / "confusion_matrix.csv")
fig, ax = plt.subplots(figsize=(4 + N_CLASSES, 3 + N_CLASSES))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=CLASS_NAMES, yticklabels=CLASS_NAMES, ax=ax)
ax.set_xlabel("Predicted")
ax.set_ylabel("Actual")
ax.set_title(f"{NAME}\n{MODEL_NAME} - Confusion Matrix (held-out test)")
plt.tight_layout()
plt.savefig(RESULT_DIR / "confusion_matrix.png", dpi=150)
plt.close(fig)

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
for ax, (a, b, title) in zip(axes, (("ce", "val_ce", "Cross-entropy (pure)"), ("loss", "val_loss", "Loss (CE + L2)"),
                                    ("accuracy", "val_accuracy", "Accuracy"))):
    ax.plot(h["epoch"], h[a], label="train")
    ax.plot(h["epoch"], h[b], label="validation")
    ax.set_title(title)
    ax.set_xlabel("epoch")
    ax.legend()
plt.suptitle(f"{NAME} - final training")
plt.tight_layout()
plt.savefig(RESULT_DIR / "training_curves.png", dpi=120)
plt.close(fig)

CI_RESAMPLES, CI_SEED = 1000, 42


def bootstrap_ci(y_true, prob):
    """95% bootstrap confidence interval on the test set: the test samples are resampled with replacement CI_RESAMPLES
    times, the metric is computed each time; the 2.5% and 97.5% percentiles are taken. No training, saved predictions."""
    import warnings
    y_true = np.asarray(y_true)
    y_pred = np.asarray(prob).argmax(axis=1)
    label_list = list(range(N_CLASSES))
    rng = np.random.default_rng(CI_SEED)
    record = {k: [] for k in ("accuracy", "f1_weighted", "f1_macro", "mcc", "balanced_accuracy")}
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        for _ in range(CI_RESAMPLES):
            i = rng.integers(0, len(y_true), len(y_true))
            t, p = y_true[i], y_pred[i]
            record["accuracy"].append(accuracy_score(t, p))
            record["f1_weighted"].append(precision_recall_fscore_support(t, p, average="weighted", labels=label_list,
                                                                         zero_division=0)[2])
            record["f1_macro"].append(precision_recall_fscore_support(t, p, average="macro", labels=label_list,
                                                                      zero_division=0)[2])
            record["mcc"].append(matthews_corrcoef(t, p))
            record["balanced_accuracy"].append(balanced_accuracy_score(t, p))
    return {k: {"lower": float(np.percentile(v, 2.5)), "upper": float(np.percentile(v, 97.5))} for k, v in record.items()}


def class_distribution(ix):
    count = {name: int((labels[ix] == k).sum()) for k, name in enumerate(CLASS_NAMES)}
    return {"count": count, "ratio": {name: round(v / max(1, len(ix)), 4) for name, v in count.items()},
            "total": int(len(ix))}


test_ci = bootstrap_ci(labels[test_idx], test_prob)
set_distribution = {"all": class_distribution(idx_all), "train": class_distribution(train_idx),
                    "val": class_distribution(val_idx), "test": class_distribution(test_idx)}
for name, d in set_distribution.items():
    print(f"Class distribution {name:5s}: {d['count']}  ratio {d['ratio']}")

select = lambda d, prefix="": {m: d[prefix + m] for m in MEASURES}  # noqa: E731
per_class = lambda d, prefix="": {name: {k: d[f"{prefix}{k}_{name}"] for k in ("precision", "recall", "f1", "support")}  # noqa: E731
                                  for name in CLASS_NAMES}
result = {
    "run": NAME, "config_hash": CONFIG_HASH, "config": CONFIG, "subdataset": SUBDATASET, "llm": LLM,
    "process_id_description": PROCESS, "classes": {name: k for k, name in enumerate(CLASS_NAMES)},
    "data": {**{s: len(class_files[s]) for s in CLASSES}, "total": n, "excluded": excluded},
    "split": {"train": len(train_idx), "val": len(val_idx), "test": len(test_idx),
              "method": ("group-based: two-stage GroupShuffleSplit 70/15/15, CV StratifiedGroupKFold" if GROUPED else
                         "stratified random 70/15/15, CV StratifiedKFold") + ", random_state=42"},
    "set_class_distribution": set_distribution,
    "groups": group_info,
    "metric_note": "micro P = micro R = micro F1 = accuracy (mathematically equal in single-label classification). "
                   "cross_entropy = pure classification loss (no L2 penalty), computed from the probabilities.",
    "cross_validation": {"n_splits": CV_FOLDS, "mean": {m: cv_summary[m]["mean"] for m in MEASURES},
                         "std": {m: cv_summary[m]["std"] for m in MEASURES},
                         "folds": cv[["fold"] + MEASURES + ["n_epochs", "best_epoch"]].to_dict(orient="records")},
    "validation_metrics": select(test_result, "val_"), "validation_per_class": per_class(test_result, "val_"),
    "held_out_test_metrics": select(test_result), "test_per_class": per_class(test_result),
    "held_out_test_ci_95": test_ci,
    "ci_method": f"bootstrap, {CI_RESAMPLES} resamples, percentiles 2.5%-97.5%, seed {CI_SEED}; the test predictions "
                 f"are resampled with replacement (no retraining)",
    "test_n_epochs": test_result["n_epochs"], "test_best_epoch": test_result["best_epoch"],
    "final_training_attempt": test_result["attempt"], "final_training_lr": test_result["lr_used"],
    "final_training_class_weight": json.loads(test_result["class_weight"]),
    "cv_retried_folds": [int(k) for k in cv.loc[cv["attempt"] == 2, "fold"]],
    "final_training_sec": test_result["train_sec"], "confusion_matrix": cm.tolist(),
}
with open(RESULT_DIR / "results.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f"\n{NAME}  {MODEL_NAME} ({ACTIVATION}, dropout {DROPOUT_RATE}, lr {LEARNING_RATE:g})")
for title, d in (("CV mean", {m: cv_summary[m]["mean"] for m in MEASURES}), ("VALIDATION", select(test_result, "val_")),
                 ("TEST", select(test_result))):
    print(f"{title:10s} acc={d['accuracy']:.4f}  F1 w/m/micro={d['f1_weighted']:.4f}/{d['f1_macro']:.4f}/"
          f"{d['f1_micro']:.4f}  P_w={d['precision_weighted']:.4f}  R_w={d['recall_weighted']:.4f}  "
          f"CE={d['cross_entropy']:.4f}  AUC={d['roc_auc']:.4f}  MCC={d['mcc']:.4f}")
print("TEST 95% CI: " + "  ".join(f"{k}=[{v['lower']:.4f}, {v['upper']:.4f}]" for k, v in test_ci.items()))
print(f"Outputs: {RESULT_DIR}\n{time.strftime('%Y-%m-%d %H:%M:%S')} FINISHED")
