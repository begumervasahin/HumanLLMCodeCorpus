#!/usr/bin/env python3
# subdataset9_embedding_human_vs_v4_group_cv
# processed_subdataset9 (embedding, CodeBERT) -- Human-written / V4 -- Group-Based Split
# Usage:  python subdataset9_embedding_human_vs_v4_group_cv.py                         (Windows or Linux; only numpy, pandas, scikit-learn are needed)
#         python subdataset9_embedding_human_vs_v4_group_cv.py --split-only            (no training; only the data split is computed and saved)
#         python subdataset9_embedding_human_vs_v4_group_cv.py --embeddings <folder>   (embedding folder; default: <repository>/Data/Embeddings/Subdataset_9)
# Results: the results/ folder next to this file.
#
# Changes relative to the original notebook: hyperparameters are not taken from the table in the paper; in every
# training run they are selected by a 3-fold inner CV on the training set ONLY (group-based in the group-based split);
# model type and embedding are the same; class weights balanced; LR max_iter 5000; probability (Platt) enabled for
# SVM; macro/micro/weighted + per-class metrics + MCC/AUC/CE; 95% bootstrap confidence interval on the test set;
# class distribution of each set; predictions are saved; misplaced vs1-vs5 files in the human-written folder are not used.
import argparse
import hashlib
import json
import pickle
import re
import sys
import time
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
import sklearn
from sklearn.ensemble import AdaBoostClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, balanced_accuracy_score, classification_report, confusion_matrix,
                             log_loss, matthews_corrcoef, precision_recall_fscore_support, roc_auc_score)
from sklearn.model_selection import (GridSearchCV, GroupShuffleSplit, StratifiedGroupKFold, StratifiedKFold,
                                     train_test_split)
from sklearn.multiclass import OneVsRestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.utils.class_weight import compute_sample_weight

SCRIPT_VERSION = "2026-10-02-ml1"

# =================================================================================================================
# SETTINGS OF THIS RUN
# =================================================================================================================
NAME = 'subdataset9_embedding_human_vs_v4_group_cv'
SUBDATASET = 9
CLASSES = ['human', 'v4']                # label = position in this list (0 = human-written)
SPLIT = 'group'                     # 'group' = Group-Based Split, 'snippet' = Snippet-Level Split
LLM, PROCESS = 'GPT-3.5', 'Process ID 9 (3): Code Similarity Detection only (deduplication)'
EMBEDDING, EMBEDDING_NAME = 'codebert', 'CodeBERT'
MODEL_NAME = 'LogisticRegression'
LR_SOLVER = 'liblinear'               # LogisticRegression only (solver in the table of the paper)
TABLE_HP = {'C': 0.1}   # table in the paper (for information; selected by inner CV in this code)
EXCLUDE_RE = r"^(?:\d+_)?vs[1-5]_"   # samples in the human-written folder whose names mark an LLM version are not used
MIN_MATCH_RATIO, MAX_GROUP_RATIO = 0.50, 0.75
# =================================================================================================================
TEST_RATIO, VAL_RATIO, CV_FOLDS, INNER_CV_FOLDS, RANDOM_SEED = 0.15, 0.15, 5, 3, 42
MERGE_IDENTICAL_CONTENT = True
RATIO_TOLERANCE = 0.03
# hyperparameter grid: in every training run selected by an INNER_CV_FOLDS-fold inner CV on that run's training set ONLY
GRID = {
    "LogisticRegression": {"C": [0.001, 0.01, 0.1, 1, 10, 100]},
    "SVM": {"C": [0.01, 0.1, 1, 10]},
    "AdaBoost": {"n_estimators": [50, 100, 200], "learning_rate": [0.1, 0.5, 1.0]},
}[MODEL_NAME]
SELECTION_METRIC = "f1_weighted"

_p = argparse.ArgumentParser()
_p.add_argument("--split-only", action="store_true")
_p.add_argument("--embeddings", help="embedding folder of this subdataset (default: <repository>/Data/Embeddings/Subdataset_N)")
_ARGS = _p.parse_args()

SPLIT_FOLDER = {"snippet": "Snippet-Level Split", "group": "Group-Based Split"}
N_CLASSES = len(CLASSES)
BINARY = N_CLASSES == 2
CLASS_NAMES = ["Human-written"] + [s.upper() for s in CLASSES[1:]]
GROUPED = SPLIT == "group"

# ---- Embedding folder: <repository>/Data/Embeddings/Subdataset_N/<class folder>/ (or --embeddings) ----
#      <class folder>/metadata.csv, <class folder>/codebert/vectors.pkl, <class folder>/codet5/vectors.pkl
CLASS_FOLDERS = {"human": "Human-written_raw", "v1": "v1", "v2": "v2", "v3": "v3", "v4": "v4", "v5": "v5"}
REPO_ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = Path(_ARGS.embeddings) if _ARGS.embeddings else REPO_ROOT / "Data" / "Embeddings" / f"Subdataset_{SUBDATASET}"
if not DATA_DIR.is_dir():
    sys.exit(f"Embedding folder not found: {DATA_DIR}. Pass the embedding folder of this subdataset with --embeddings.")
RESULT_DIR = Path(__file__).resolve().parent / "results" / NAME
RESULT_DIR.mkdir(parents=True, exist_ok=True)

CONFIG = {
    "script_version": SCRIPT_VERSION, "subdataset": SUBDATASET, "classes": CLASSES, "split": SPLIT,
    "data_folder": f"Data/Embeddings/Subdataset_{SUBDATASET}", "embedding": EMBEDDING_NAME, "model": MODEL_NAME,
    "lr_solver": LR_SOLVER, "grid": GRID,
    "selection": f"{INNER_CV_FOLDS}-fold inner CV ({'StratifiedGroupKFold' if GROUPED else 'StratifiedKFold'}), "
                 f"criterion {SELECTION_METRIC}, on the training set only",
    "class_weight": "balanced", "scaling": "StandardScaler (fit on the training set only in every training run)",
    "exclude_regex": EXCLUDE_RE, "test_ratio": TEST_RATIO, "val_ratio": VAL_RATIO, "cv_folds": CV_FOLDS,
    "seed": RANDOM_SEED,
    "min_match_ratio": MIN_MATCH_RATIO if GROUPED else None, "max_group_ratio": MAX_GROUP_RATIO if GROUPED else None,
}
CONFIG_HASH = hashlib.md5(json.dumps(CONFIG, sort_keys=True).encode()).hexdigest()[:12]


class _Tee:
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
sys.stdout = _Tee(sys.stdout, _log)
sys.stderr = _Tee(sys.stderr, _log)
print(f"\n{'=' * 100}\n{time.strftime('%Y-%m-%d %H:%M:%S')}  {NAME}  (config hash {CONFIG_HASH}, sklearn {sklearn.__version__})")

if (RESULT_DIR / "results.json").exists() and not _ARGS.split_only:
    print("results.json already exists -> this run is complete, skipping. To run it again, delete the folder:", RESULT_DIR)
    sys.exit(0)
CONFIG_FILE = RESULT_DIR / "config.json"
if CONFIG_FILE.exists():
    old = json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
    if old.get("config_hash") != CONFIG_HASH:
        sys.exit(f"STOPPED: the previous run in this folder used DIFFERENT settings ({old.get('config_hash')} != {CONFIG_HASH}). "
                 f"Delete or move the folder: {RESULT_DIR}")
CONFIG_FILE.write_text(json.dumps({**CONFIG, "config_hash": CONFIG_HASH}, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Data  : {DATA_DIR}  ({EMBEDDING_NAME})")
print(f"Model : {MODEL_NAME}  grid {GRID}  class weight balanced")
print(f"Output: {RESULT_DIR}")

# ---------------------------------------------------------------------------------------------------------------
# Load the embeddings + label (label = position in CLASSES: 0 = human-written)
# ---------------------------------------------------------------------------------------------------------------
def read_pkl(path):
    with open(path, "rb") as f:
        return pickle.load(f)


X_parts, name_parts, label_parts, content_parts = [], [], [], []
for k, s in enumerate(CLASSES):
    d = DATA_DIR / CLASS_FOLDERS[s]
    vec, meta, content_vec = d / EMBEDDING / "vectors.pkl", d / "metadata.csv", d / "codebert" / "vectors.pkl"
    for path in (vec, meta, content_vec):
        assert path.is_file(), f"File not found: {path}"
    v, m, cv_ = read_pkl(vec), pd.read_csv(meta), read_pkl(content_vec)
    assert v.ndim == 2 and len(m) == len(v) == len(cv_), f"{s}: different number of rows in vectors/metadata"
    X_parts.append(v)
    name_parts += list(m["filename"])
    label_parts.append(np.full(len(v), k))
    content_parts.append(cv_)
X = np.vstack(X_parts)
file_names = [str(a) for a in name_parts]
labels = np.concatenate(label_parts).astype(int)
# "identical content" = md5 of the CodeBERT vector (same criterion as in the original embedding notebooks)
contents = np.array([hashlib.md5(np.ascontiguousarray(r).tobytes()).hexdigest() for r in np.vstack(content_parts)])

excluded = []
if EXCLUDE_RE:
    keep = np.array([not (lab == 0 and re.match(EXCLUDE_RE, name)) for name, lab in zip(file_names, labels)])
    excluded = [name for name, t in zip(file_names, keep) if not t]
    X, labels, contents = X[keep], labels[keep], contents[keep]
    file_names = [name for name, t in zip(file_names, keep) if t]
    print(f"{len(excluded)} samples in the human-written folder whose names mark an LLM version were NOT used (data unchanged): {excluded}")
n = len(labels)
for k, name in enumerate(CLASS_NAMES):
    print(f"{name:3s} (label {k}): {int((labels == k).sum())} samples")
print(f"Total {n} samples, {X.shape[1]} features ({X.dtype})")


def distribution(ix):
    return " ".join(f"{name}={int((labels[ix] == k).sum())}" for k, name in enumerate(CLASS_NAMES))


# ---------------------------------------------------------------------------------------------------------------
# Data split (same rule as in the image-based scripts)
# ---------------------------------------------------------------------------------------------------------------
idx_all = np.arange(n)
group_info = {}
families = keys = None
if GROUPED:
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
    suspicious = [name for name, e, s in zip(file_names, labels, name_versions)
                  if (e == 0 and s is not None) or (e != 0 and s != CLASSES[e].lstrip("v"))]
    group_info["files_with_folder_name_version_mismatch"] = len(suspicious)
    print(f"Samples whose folder and version tag in the name do not match (data unchanged): {len(suspicious)}")

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
else:
    dev_idx, test_idx = train_test_split(idx_all, test_size=TEST_RATIO, random_state=RANDOM_SEED, stratify=labels)
    train_idx, val_idx = train_test_split(dev_idx, test_size=VAL_RATIO / (1.0 - TEST_RATIO),
                                          random_state=RANDOM_SEED, stratify=labels[dev_idx])
    skf = StratifiedKFold(n_splits=CV_FOLDS, shuffle=True, random_state=RANDOM_SEED)
    cv_folds = [(dev_idx[tr], dev_idx[va]) for tr, va in skf.split(dev_idx, labels[dev_idx])]
    for a, b in ((train_idx, val_idx), (train_idx, test_idx), (val_idx, test_idx)):
        assert not set(a.tolist()) & set(b.tolist()), "the sets contain the same sample"

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
# Model, hyperparameter selection, metrics
# ---------------------------------------------------------------------------------------------------------------
def build_model():
    """StandardScaler -> classifier. Class weights: class_weight='balanced' for LR/SVM,
    balanced sample_weight during training for AdaBoost."""
    if MODEL_NAME == "LogisticRegression":
        lr = LogisticRegression(penalty="l2", solver=LR_SOLVER, max_iter=5000, class_weight="balanced",
                                random_state=RANDOM_SEED)
        clf = lr if BINARY else OneVsRestClassifier(lr)      # one-vs-rest as in the original 6-class code
    elif MODEL_NAME == "SVM":
        clf = SVC(kernel="linear", class_weight="balanced", cache_size=1000, random_state=RANDOM_SEED)
    else:
        clf = AdaBoostClassifier(random_state=RANDOM_SEED)
    return Pipeline([("scaler", StandardScaler()), ("clf", clf)])


def grid_names():
    prefix = "clf__estimator__" if (MODEL_NAME == "LogisticRegression" and not BINARY) else "clf__"
    return {prefix + k: v for k, v in GRID.items()}


def train(train_ix):
    """Selects the hyperparameters by inner CV on the training set ONLY, then refits on the whole training set."""
    Xt, yt = X[train_ix], labels[train_ix]
    fit_extra = {"clf__sample_weight": compute_sample_weight("balanced", yt)} if MODEL_NAME == "AdaBoost" else {}
    if GROUPED:
        inner_cv = StratifiedGroupKFold(n_splits=INNER_CV_FOLDS, shuffle=True, random_state=RANDOM_SEED)
        groups = families[train_ix]
    else:
        inner_cv = StratifiedKFold(n_splits=INNER_CV_FOLDS, shuffle=True, random_state=RANDOM_SEED)
        groups = None
    gs = GridSearchCV(build_model(), grid_names(), scoring=SELECTION_METRIC, cv=inner_cv, n_jobs=-1, refit=False)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        gs.fit(Xt, yt, groups=groups, **fit_extra)
    selected = gs.best_params_
    model = build_model()
    model.set_params(**selected)
    if MODEL_NAME == "SVM":
        model.set_params(clf__probability=True)     # for probabilities (cross-entropy, AUC); predictions from predict()
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        model.fit(Xt, yt, **fit_extra)
    return model, {k.split("__")[-1]: v for k, v in selected.items()}, float(gs.best_score_)


def metrics(y_true, y_pred, prob):
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


def predict(model, ix):
    return model.predict(X[ix]).astype(int), np.asarray(model.predict_proba(X[ix]), dtype="float64")


def prediction_table(ix, y_pred, prob, set_name):
    t = pd.DataFrame({"set": set_name, "file": [file_names[i] for i in ix], "true": labels[ix], "pred": y_pred})
    for k, name in enumerate(CLASS_NAMES):
        t[f"prob_{name}"] = prob[:, k]
    return t


def append_csv(df, path, columns=None):
    if columns is not None:
        df = df.reindex(columns=columns)
    df.to_csv(path, mode="a", header=not path.exists(), index=False)


_example = metrics(np.arange(N_CLASSES), np.arange(N_CLASSES), np.eye(N_CLASSES))
CV_COLUMNS = ["fold", "n_train", "n_eval"] + list(_example) + ["selected_hp", "inner_cv_score", "time_sec", "error"]

# ---- 5-fold CV (completed folds are skipped) ----
CV_CSV = RESULT_DIR / "cv_fold_results.csv"
completed = set()
if CV_CSV.exists():
    previous = pd.read_csv(CV_CSV)
    previous = previous[previous["error"].isna() | (previous["error"].astype(str).str.strip() == "")]
    completed = set(int(k) for k in previous["fold"])
    print(f"Previously completed folds: {sorted(completed)} (will be skipped)")
for fold, (fold_train_idx, fold_eval_idx) in enumerate(cv_folds, start=1):
    if fold in completed:
        continue
    print(f"\n===== Fold {fold}/{CV_FOLDS}  {time.strftime('%H:%M:%S')} =====", flush=True)
    row = {"fold": fold, "n_train": len(fold_train_idx), "n_eval": len(fold_eval_idx)}
    t0 = time.time()
    try:
        model, selected, inner_score = train(fold_train_idx)
        y_pred, prob = predict(model, fold_eval_idx)
        row.update(metrics(labels[fold_eval_idx], y_pred, prob))
        row.update({"selected_hp": json.dumps(selected), "inner_cv_score": inner_score, "error": ""})
        append_csv(prediction_table(fold_eval_idx, y_pred, prob, f"fold{fold}"), RESULT_DIR / "predictions_cv.csv")
    except Exception as e:
        row["error"] = f"{type(e).__name__}: {e}"[:300]
    row["time_sec"] = round(time.time() - t0, 1)
    append_csv(pd.DataFrame([row]), CV_CSV, CV_COLUMNS)
    print(f"Fold {fold}: accuracy={row.get('accuracy', float('nan')):.4f}  "
          f"F1(w/m)={row.get('f1_weighted', float('nan')):.4f}/{row.get('f1_macro', float('nan')):.4f}  "
          f"selected {row.get('selected_hp', '-')}  {row['time_sec']} s  {row['error']}", flush=True)

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

# ---- Final training: 70% train -> evaluated once on the 15% test set (and on the 15% validation set) ----
print(f"\n===== Final training  {time.strftime('%H:%M:%S')} =====", flush=True)
t0 = time.time()
final_model, final_selected, final_inner_score = train(train_idx)
test_pred, test_prob = predict(final_model, test_idx)
val_pred, val_prob = predict(final_model, val_idx)
test_m = metrics(labels[test_idx], test_pred, test_prob)
val_m = metrics(labels[val_idx], val_pred, val_prob)
pd.concat([prediction_table(test_idx, test_pred, test_prob, "test"),
           prediction_table(val_idx, val_pred, val_prob, "validation")]).to_csv(RESULT_DIR / "predictions.csv", index=False,
                                                                                encoding="utf-8-sig")
print(f"Selected hyperparameters: {final_selected}  (inner CV {SELECTION_METRIC} {final_inner_score:.4f})  {time.time() - t0:.0f} s")
print(classification_report(labels[test_idx], test_pred, target_names=CLASS_NAMES, zero_division=0, digits=4))
cm = confusion_matrix(labels[test_idx], test_pred, labels=list(range(N_CLASSES)))
pd.DataFrame(cm, index=CLASS_NAMES, columns=CLASS_NAMES).to_csv(RESULT_DIR / "confusion_matrix.csv")
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(4 + N_CLASSES, 3 + N_CLASSES))
    ax.imshow(cm, cmap="Blues")
    for i in range(N_CLASSES):
        for j in range(N_CLASSES):
            ax.text(j, i, str(cm[i, j]), ha="center", va="center")
    ax.set_xticks(range(N_CLASSES), CLASS_NAMES)
    ax.set_yticks(range(N_CLASSES), CLASS_NAMES)
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    ax.set_title(f"{NAME}\n{MODEL_NAME} ({EMBEDDING_NAME}) - Confusion Matrix (held-out test)")
    plt.tight_layout()
    plt.savefig(RESULT_DIR / "confusion_matrix.png", dpi=150)
    plt.close(fig)
except Exception as e:      # the plot is optional; the CSV has been saved
    print("confusion_matrix.png could not be drawn:", e)

CI_RESAMPLES, CI_SEED = 1000, 42


def bootstrap_ci(y_true, y_pred):
    y_true, y_pred = np.asarray(y_true), np.asarray(y_pred)
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


test_ci = bootstrap_ci(labels[test_idx], test_pred)
set_distribution = {"all": class_distribution(idx_all), "train": class_distribution(train_idx),
                    "val": class_distribution(val_idx), "test": class_distribution(test_idx)}
for name, d in set_distribution.items():
    print(f"Class distribution {name:5s}: {d['count']}  ratio {d['ratio']}")
select = lambda d: {m: d[m] for m in MEASURES}  # noqa: E731
per_class = lambda d: {name: {k: d[f"{k}_{name}"] for k in ("precision", "recall", "f1", "support")}  # noqa: E731
                       for name in CLASS_NAMES}
result = {
    "run": NAME, "config_hash": CONFIG_HASH, "config": CONFIG, "sklearn": sklearn.__version__,
    "subdataset": SUBDATASET, "llm": LLM, "process_id_description": PROCESS, "embedding": EMBEDDING_NAME,
    "model": MODEL_NAME, "paper_table_hyperparameters": TABLE_HP, "final_training_selected_hp": final_selected,
    "final_training_inner_cv_score": final_inner_score,
    "classes": {name: k for k, name in enumerate(CLASS_NAMES)},
    "data": {**{s: int((labels == k).sum()) for k, s in enumerate(CLASSES)}, "total": n, "excluded": excluded},
    "split": {"train": len(train_idx), "val": len(val_idx), "test": len(test_idx),
              "method": ("group-based: two-stage GroupShuffleSplit 70/15/15, CV StratifiedGroupKFold" if GROUPED else
                         "stratified random 70/15/15, CV StratifiedKFold") + ", random_state=42"},
    "set_class_distribution": set_distribution, "groups": group_info,
    "metric_note": "micro P = micro R = micro F1 = accuracy (equal in single-label classification). Predictions from "
                   "predict(), cross_entropy and AUC from predict_proba() (Platt probabilities for SVM).",
    "cross_validation": {"n_splits": CV_FOLDS, "mean": {m: cv_summary[m]["mean"] for m in MEASURES},
                         "std": {m: cv_summary[m]["std"] for m in MEASURES},
                         "folds": cv[["fold"] + MEASURES + ["selected_hp"]].to_dict(orient="records")},
    "validation_metrics": select(val_m), "validation_per_class": per_class(val_m),
    "held_out_test_metrics": select(test_m), "test_per_class": per_class(test_m),
    "held_out_test_ci_95": test_ci,
    "ci_method": f"bootstrap, {CI_RESAMPLES} resamples, percentiles 2.5%-97.5%, seed {CI_SEED}; the test predictions "
                 f"are resampled with replacement",
    "confusion_matrix": cm.tolist(),
}
with open(RESULT_DIR / "results.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
print(f"\n{NAME}  {MODEL_NAME} ({EMBEDDING_NAME}) selected {final_selected}")
for title, d in (("CV mean", {m: cv_summary[m]["mean"] for m in MEASURES}), ("VALIDATION", val_m), ("TEST", test_m)):
    print(f"{title:10s} acc={d['accuracy']:.4f}  F1 w/m/micro={d['f1_weighted']:.4f}/{d['f1_macro']:.4f}/"
          f"{d['f1_micro']:.4f}  P_w={d['precision_weighted']:.4f}  R_w={d['recall_weighted']:.4f}  "
          f"CE={d['cross_entropy']:.4f}  AUC={d['roc_auc']:.4f}  MCC={d['mcc']:.4f}")
print("TEST 95% CI: " + "  ".join(f"{k}=[{v['lower']:.4f}, {v['upper']:.4f}]" for k, v in test_ci.items()))
print(f"Outputs: {RESULT_DIR}\n{time.strftime('%Y-%m-%d %H:%M:%S')} FINISHED")
