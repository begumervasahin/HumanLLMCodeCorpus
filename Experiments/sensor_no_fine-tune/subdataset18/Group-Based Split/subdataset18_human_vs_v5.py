# -*- coding: utf-8 -*-
"""CodeGPTSensor -- processed_subdataset18 -- Human-written vs V5 -- NO FINE-TUNING (control experiment)
Group-Based Split: group-based GroupShuffleSplit 70%/15%/15%, random_state=42
Produces F1 / Precision / Recall / Accuracy separately for the validation and the test set.

This file runs ON ITS OWN; it does not depend on any other code (all code is below).
Usage: python subdataset18_human_vs_v5.py --data <data folder>
       <data folder> must contain the original data release folders "VEKTÖR" (file lists) and
       "Düz KODLAR PY" (source code texts); these folder names are kept as in the original data release.

TWO SPLIT TYPES
---------------
"group"    (Group-Based Split folder)
    SAME method as the feature-based ML experiments (Table 10):
    group-based GroupShuffleSplit, 70% train / 15% val / 15% test, random_state=42.
    Group = files derived from the same original human-written file (human-written + LLM version). All files of a
    group are in ONLY ONE of train/val/test; leakage is checked in the code with assert.
    Validation = the 15% val set, Test = the 15% test set.

"snippet"  (Snippet-Level Split folder)
    SAME method as the original 2025 embedding experiments:
    train_test_split(test_size=0.2, random_state=42, stratify=y)  ->  80% train / 20% test.
    FIXED VALIDATION set: the 80% train part is split once more with the same method
    (test_size=0.2, random_state=42, stratify)  ->  in total 64% train / 16% val / 20% test.
    Validation = this 16% set, Test = the 20% test set.
    ADDITIONAL INFORMATION: the StratifiedKFold(n_splits=5, shuffle=True, random_state=42) folds that correspond to the
    GridSearchCV cv of those experiments are also computed on the 80% part ("cv" block in the JSON).

DATA
----
File lists: <data folder>\\VEKTÖR\\<subdataset folder>\\<v>vektor\\metadata_<v>.csv
    (lists produced by the embedding notebook = the files used by the Table 10 ML experiments). The order is also the
    metadata order (first human-written, then the version) -- so the split falls on exactly the same indices as in
    the ML experiments.
File texts: read from <data folder>\\Düz KODLAR PY\\<folder>\\<Topic>\\<file>.
    Files that are in the list but not on disk (only in processed_subdataset18) are excluded from the evaluation
    AFTER the split has been computed, and their numbers are written to the results file.
    Empty files are KEPT in the evaluation because they are also present in the ML experiments (their number is reported).

GROUP KEY (from the file name)
------------------------------
processed_subdataset9, 18  : file name  "v1_10_content_..."        -> key: the leading "v1_" is removed
                             (same as the FAMILY_RE of the ML notebooks:  ^v\\d_\\s*)
processed_subdataset7,8,16,17: file name "51_v1_10_content_..._cleaned.py" (human-written: "10_13_content_...")
                             -> key: the leading index number and, if present, "v1_" are removed
                             (same as the FAMILY_RE of the CNN notebooks:  ^\\d+_(v\\d_)?)
    NOTE: since the ML notebooks also used the key of 9/18 for 7/8/16/17, no group matching happened there
    (number of groups = number of files -> in effect a file-level random split). Here the correct key is used for
    every subdataset, and the script stops with an ERROR if the match ratio is low.

MODEL (NO fine-tuning, control experiment)
------------------------------------------
GPTSniffer    : microsoft/codebert-base + classification layer (AutoModelForSequenceClassification)
CodeGPTSensor : microsoft/unixcoder-base-nine + attention-mask mean pooling + Linear(hidden, 2)
The classification layer is initialised randomly; no gradient step is taken. For reproducibility
torch/numpy/random seed = 42 (earlier runs had no seed, so the numbers changed in every run).

OUTPUTS (to the results/ folder next to this file)
--------------------------------------------------
<name>_results.json     : all metrics (val, test, [snippet: 5 folds + mean], weighted/macro/binary,
                          confusion matrix), split sizes, numbers of missing/empty files, environment information
<name>_summary.txt      : readable summary
<name>_split.csv        : the set of each file (train/val/test [+ snippet: cv_fold])
<name>_predictions.csv  : true label, prediction, P(LLM) for every evaluated file
"""
from __future__ import annotations

import argparse
import json
import os
import random
import re
import sys
import time
from collections import Counter
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import (accuracy_score, confusion_matrix, f1_score,
                             precision_score, recall_score)
from sklearn.model_selection import GroupShuffleSplit, StratifiedKFold, train_test_split

# ----------------------------------------------------------------------------- paths / settings
# folder names of the original data release (they are data names, so they are kept unchanged)
VECTORS_DIR_NAME = "VEKTÖR"
CODE_DIR_NAME = "Düz KODLAR PY"
HUMAN_TOKEN = "ham"               # name of the human-written lists in the original data release ("hamvektor", "metadata_ham.csv")
DATA_ROOT = None                  # set from --data (see run())

GROUP_RE_ML = r"^v\d_\s*"         # processed_subdataset9, 18   (key of the Table 10 ML notebooks)
GROUP_RE_CNN = r"^\d+_(v\d_)?"    # processed_subdataset7,8,16,17 (key of the Table 9 CNN notebooks)

# subdataset -> settings. process_id: sub for GPT-3.5, sub-9 for GPT-4o (Table 8 of the paper)
CFG = {
    7:  dict(llm="GPT-3.5", format="high", process_id=7,
             vectors="high + benzerlik + 3,5  ml için ayrılmıs", code="GPT3.5 sonuçlar high", ext=".py",  group_re=GROUP_RE_CNN),
    8:  dict(llm="GPT-3.5", format="low", process_id=8,
             vectors="low + benzerlik + 3,5  ml için ayrılmıs",  code="Gpt3.5 sonuçlar low",  ext=".py",  group_re=GROUP_RE_CNN),
    9:  dict(llm="GPT-3.5", format="similarity_only", process_id=9,
             vectors="Benzerlik+3.5 ml için ayrılmıs",           code="gpt3.5",               ext=".txt", group_re=GROUP_RE_ML),
    16: dict(llm="GPT-4o",  format="high", process_id=7,
             vectors="high+ benzerlik + 4o  ml için ayrılmıs",   code="GPT4o sonuçlar high",  ext=".py",  group_re=GROUP_RE_CNN),
    17: dict(llm="GPT-4o",  format="low", process_id=8,
             vectors="low + benzerlik + 4o  ml için ayrılmıs",   code="GPT4o sonuçlar low",   ext=".py",  group_re=GROUP_RE_CNN),
    18: dict(llm="GPT-4o",  format="similarity_only", process_id=9,
             vectors="Benzerlik+4o Ml için ayrılmıs",            code="GPT4o",                ext=".txt", group_re=GROUP_RE_ML),
}
ARCHITECTURES = {
    "sniffer": dict(name="GPTSniffer",    model="microsoft/codebert-base"),
    "sensor":  dict(name="CodeGPTSensor", model="microsoft/unixcoder-base-nine"),
}
SEED = 42
BATCH_SIZE = 16
MAX_LEN = 512
EVALUATE_TRAIN_SET_TOO = False           # set to True if metrics are also wanted for the train set in the "group" split
MIN_GROUP_MATCH_RATIO = 0.80             # at least this ratio of human/version pairs must fall into the same group


def _utf8_console():
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8")
        except Exception:
            pass


# ----------------------------------------------------------------------------- data
def file_list(sub: int, ver: str) -> list[str]:
    """File names in the VEKTÖR metadata, IN METADATA ORDER (same order as in the ML experiments)."""
    p = DATA_ROOT / VECTORS_DIR_NAME / CFG[sub]["vectors"] / f"{ver}vektor" / f"metadata_{ver}.csv"
    return pd.read_csv(p)["filename"].astype(str).tolist()


def disk_map(sub: int) -> dict[str, list[tuple[str, Path]]]:
    """file name -> [(topic, full path), ...]  (the same name can be in more than one topic; paths sorted)."""
    base = DATA_ROOT / CODE_DIR_NAME / CFG[sub]["code"]
    ext = CFG[sub]["ext"].lower()
    mapping: dict[str, list[tuple[str, Path]]] = {}
    for topic in sorted(p for p in base.iterdir() if p.is_dir()):
        for f in sorted(topic.iterdir()):
            if f.is_file() and f.suffix.lower() == ext:
                mapping.setdefault(f.name, []).append((topic.name, f))
    return mapping


def match_paths(names: list[str], mapping: dict) -> list[tuple[str | None, Path | None]]:
    """Matches every metadata row to the file on disk. If the same name occurs k times, the k copies on disk
    (different topics, in path order) are assigned in order. If it is not on disk: (None, None)."""
    counter: Counter = Counter()
    out = []
    for name in names:
        k = counter[name]
        counter[name] += 1
        copies = mapping.get(name, [])
        out.append(copies[k] if k < len(copies) else (None, None))
    return out


def read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="ignore")


# ----------------------------------------------------------------------------- split
def split_group(names: list[str], y: np.ndarray, group_re: str):
    """Exactly the same code as in the Table 10 ML experiments (group-based GroupShuffleSplit 70/15/15)."""
    rx = re.compile(group_re)
    group = np.array([rx.sub("", name, count=1) for name in names])
    idx = np.arange(len(y))
    gss1 = GroupShuffleSplit(n_splits=1, test_size=0.15, random_state=SEED)
    trainval, test = next(gss1.split(idx, y, groups=group))
    gss2 = GroupShuffleSplit(n_splits=1, test_size=0.15 / 0.85, random_state=SEED)
    tr, va = next(gss2.split(trainval, y[trainval], groups=group[trainval]))
    train, val = trainval[tr], trainval[va]

    # leakage check (guaranteed by GroupShuffleSplit -- verified anyway)
    s_tr, s_va, s_te = set(group[train]), set(group[val]), set(group[test])
    assert not (s_tr & s_va), "LEAKAGE: train/val share a group"
    assert not (s_tr & s_te), "LEAKAGE: train/test share a group"
    assert not (s_va & s_te), "LEAKAGE: val/test share a group"

    # does the group key fit this file name format? (if not, the split is in effect random -> STOP)
    human_groups = set(group[y == 0]); version_groups = set(group[y == 1])
    matched = len(human_groups & version_groups)
    ratio = matched / max(1, min(len(human_groups), len(version_groups)))
    if ratio < MIN_GROUP_MATCH_RATIO:
        raise RuntimeError(
            f"GROUP KEY MISMATCH: with regex {group_re!r} the human/version match ratio is {ratio:.2f} "
            f"(matched groups={matched}). In this state the split is NOT group-based. Check group_re in CFG.")
    info = dict(regex=group_re, n_groups=int(len(set(group))), n_human_groups=len(human_groups),
                n_version_groups=len(version_groups), n_matched_groups=matched, match_ratio=round(ratio, 4),
                leakage_check="OK", n_groups_train=len(s_tr), n_groups_val=len(s_va), n_groups_test=len(s_te))
    return train, val, test, group, info


def split_snippet(y: np.ndarray):
    """Split of the 2025 embedding experiments: train_test_split(test_size=0.2, random_state=42, stratify=y)
    -> 80% train / 20% test. Fixed validation: the 80% train part is split once more with the same method
    -> 64% train / 16% val / 20% test. Additionally: StratifiedKFold(5, shuffle, 42) folds on the 80% part
    (the GridSearchCV cv of the 2025 experiments)."""
    idx = np.arange(len(y))
    train80, test = train_test_split(idx, test_size=0.2, random_state=SEED, stratify=y)
    train, val = train_test_split(train80, test_size=0.2, random_state=SEED, stratify=y[train80])
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)
    folds = [train80[va] for _, va in skf.split(train80, y[train80])]   # validation part of each fold
    return train, val, test, folds


# ----------------------------------------------------------------------------- metrics
def metrics(y_true, y_pred) -> dict:
    y_true = np.asarray(y_true, dtype=int); y_pred = np.asarray(y_pred, dtype=int)
    if len(y_true) == 0:
        return dict(n=0)
    cm = confusion_matrix(y_true, y_pred, labels=[0, 1])
    d = dict(
        n=int(len(y_true)), n_human=int((y_true == 0).sum()), n_llm=int((y_true == 1).sum()),
        f1_weighted=float(f1_score(y_true, y_pred, average="weighted", zero_division=0)),
        precision_weighted=float(precision_score(y_true, y_pred, average="weighted", zero_division=0)),
        recall_weighted=float(recall_score(y_true, y_pred, average="weighted", zero_division=0)),
        accuracy=float(accuracy_score(y_true, y_pred)),
        f1_macro=float(f1_score(y_true, y_pred, average="macro", zero_division=0)),
        precision_macro=float(precision_score(y_true, y_pred, average="macro", zero_division=0)),
        recall_macro=float(recall_score(y_true, y_pred, average="macro", zero_division=0)),
        f1_binary_llm=float(f1_score(y_true, y_pred, pos_label=1, zero_division=0)),
        precision_binary_llm=float(precision_score(y_true, y_pred, pos_label=1, zero_division=0)),
        recall_binary_llm=float(recall_score(y_true, y_pred, pos_label=1, zero_division=0)),
        confusion_matrix=dict(TN=int(cm[0, 0]), FP=int(cm[0, 1]), FN=int(cm[1, 0]), TP=int(cm[1, 1]),
                              description="0=human-written, 1=LLM; TN: human->human, FP: human->LLM, FN: LLM->human, TP: LLM->LLM"),
        pred_dist={"0": int((y_pred == 0).sum()), "1": int((y_pred == 1).sum())},
    )
    return d


def _mean_std(fold_metrics: list[dict]) -> tuple[dict, dict]:
    keys = [k for k in fold_metrics[0] if isinstance(fold_metrics[0][k], float)]
    mean = {k: float(np.mean([m[k] for m in fold_metrics])) for k in keys}
    std = {k: float(np.std([m[k] for m in fold_metrics])) for k in keys}
    mean["n"] = int(np.sum([m["n"] for m in fold_metrics]))
    return mean, std


# ----------------------------------------------------------------------------- model
def _set_seed():
    random.seed(SEED); np.random.seed(SEED)
    import torch
    torch.manual_seed(SEED); torch.cuda.manual_seed_all(SEED)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


def build_model(architecture: str):
    import torch
    from transformers import AutoModel, AutoModelForSequenceClassification, AutoTokenizer
    _set_seed()
    model_name = ARCHITECTURES[architecture]["model"]
    tok = AutoTokenizer.from_pretrained(model_name)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    if architecture == "sniffer":
        model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)

        def forward(batch):
            return model(**batch).logits
    else:
        class CodeGPTSensor(torch.nn.Module):
            """UniXcoder encoder + attention-mask mean pooling + linear classification layer."""
            def __init__(self, name):
                super().__init__()
                self.encoder = AutoModel.from_pretrained(name)
                self.classifier = torch.nn.Linear(self.encoder.config.hidden_size, 2)

            def forward(self, input_ids, attention_mask):
                h = self.encoder(input_ids=input_ids, attention_mask=attention_mask).last_hidden_state
                m = attention_mask.unsqueeze(-1).float()
                emb = (h * m).sum(1) / m.sum(1).clamp(min=1e-9)
                return self.classifier(emb)

        model = CodeGPTSensor(model_name)

        def forward(batch):
            return model(input_ids=batch["input_ids"], attention_mask=batch["attention_mask"])
    model.to(device).eval()
    return tok, model, forward, device


def predict(texts: list[str], tok, model, forward, device) -> tuple[np.ndarray, np.ndarray]:
    """(prediction, P(LLM)) for every text. No fine-tuning: forward pass only."""
    import torch
    preds, probs = [], []
    with torch.no_grad():
        for i in range(0, len(texts), BATCH_SIZE):
            enc = tok(texts[i:i + BATCH_SIZE], truncation=True, max_length=MAX_LEN,
                      padding="max_length", return_tensors="pt")
            enc = {k: v.to(device) for k, v in enc.items() if k in ("input_ids", "attention_mask")}
            logits = forward(enc)
            p = torch.softmax(logits, dim=1)[:, 1]
            preds.extend(torch.argmax(logits, dim=1).cpu().numpy().tolist())
            probs.extend(p.cpu().numpy().tolist())
            if (i // BATCH_SIZE) % 50 == 0:
                print(f"    {min(i + BATCH_SIZE, len(texts))}/{len(texts)}", flush=True)
    return np.array(preds), np.array(probs)


# ----------------------------------------------------------------------------- main flow
def prepare_data(sub: int, version: int, split_type: str):
    """Loads the lists, builds the split, matches the paths on disk. Needs no model (also used for checks)."""
    cfg = CFG[sub]
    vk = f"v{version}"
    human = file_list(sub, HUMAN_TOKEN)
    ver = file_list(sub, vk)
    names = human + ver
    y = np.array([0] * len(human) + [1] * len(ver))
    mapping = disk_map(sub)
    paths = match_paths(names, mapping)
    df = pd.DataFrame({
        "file": names, "label": y, "label_name": np.where(y == 0, "human", vk),
        "topic": [k for k, _ in paths], "path": [str(p) if p else None for _, p in paths],
        "on_disk": [p is not None for _, p in paths],
    })
    if split_type == "group":
        train, val, test, group, group_info = split_group(names, y, cfg["group_re"])
        df["group"] = group
        df["set"] = ""
        df.loc[train, "set"] = "train"; df.loc[val, "set"] = "val"; df.loc[test, "set"] = "test"
        extra = dict(groups=group_info)
    elif split_type == "snippet":
        train, val, test, folds = split_snippet(y)
        df["set"] = ""
        df.loc[train, "set"] = "train"; df.loc[val, "set"] = "val"; df.loc[test, "set"] = "test"
        df["cv_fold"] = 0                       # the 5 CV folds on the 80% (train+val) part; 0 for test
        for k, fold in enumerate(folds, start=1):
            df.loc[fold, "cv_fold"] = k
        extra = dict(n_cv_folds=5)
    else:
        raise ValueError(split_type)
    return df, extra


def run(architecture: str, subdataset: int, version: int, split_type: str, output_dir: Path, data_root: Path):
    global DATA_ROOT
    DATA_ROOT = Path(data_root)
    _utf8_console()
    t0 = time.time()
    cfg = CFG[subdataset]; arch = ARCHITECTURES[architecture]
    vk = f"v{version}"
    name = f"subdataset{subdataset}_{architecture}_{split_type}_human_vs_{vk}"
    output_dir = Path(output_dir); output_dir.mkdir(parents=True, exist_ok=True)
    print("=" * 78)
    print(f"{arch['name']} -- processed_subdataset{subdataset} ({cfg['llm']} / {cfg['format']}) -- Human-written vs V{version} -- split: {split_type}")
    print("=" * 78)

    df, extra = prepare_data(subdataset, version, split_type)
    n_missing = df.groupby("set")["on_disk"].apply(lambda s: int((~s).sum())).to_dict()
    print(f"Listed: human={int((df.label == 0).sum())}  {vk}={int((df.label == 1).sum())}  |  not found on disk: {n_missing}")
    if split_type == "group":
        a = extra["groups"]
        print(f"Groups: {a['n_groups']} groups, human/version matched={a['n_matched_groups']} (ratio {a['match_ratio']}), leakage check OK")
    sizes = df["set"].value_counts().to_dict()
    print(f"Split: {sizes}")

    # which files are evaluated
    if split_type == "group":
        sets = ["val", "test"] + (["train"] if EVALUATE_TRAIN_SET_TOO else [])
    else:
        sets = ["train", "val", "test"]    # snippet: the whole 80% (train+val) is needed for the CV folds
    ev = df[df["set"].isin(sets) & df["on_disk"]].copy()
    texts = [read_text(Path(p)) for p in ev["path"]]
    ev["empty_file"] = [not t.strip() for t in texts]
    print(f"Files to evaluate: {len(ev)} (empty files: {int(ev.empty_file.sum())})")

    print(f"Loading model: {arch['model']} (NO fine-tuning, seed={SEED})")
    tok, model, forward, device = build_model(architecture)
    print(f"Device: {device}")
    preds, probs = predict(texts, tok, model, forward, device)
    ev["pred"] = preds; ev["p_llm"] = probs

    result = dict(
        run=name, architecture=arch["name"], model_name=arch["model"], fine_tuning="none (control experiment)", seed=SEED,
        subdataset=subdataset, process_id=cfg["process_id"], llm=cfg["llm"], format=cfg["format"],
        comparison=f"binary: human vs {vk}", split_type=split_type,
        split_description=("group-based GroupShuffleSplit 70/15/15, random_state=42 (same as the Table 10 ML experiments)"
                           if split_type == "group" else
                           "train_test_split(test_size=0.2, random_state=42, stratify=y) -> 80%/20% (same as the 2025 embedding experiments); "
                           "validation = 20% split off the 80% train part with the same method -> in total 64% train / 16% val / 20% test; "
                           "additionally: StratifiedKFold(5, shuffle, 42) folds on the 80% part"),
        data=dict(file_list=f"{VECTORS_DIR_NAME}/{cfg['vectors']}", text_folder=f"{CODE_DIR_NAME}/{cfg['code']}",
                  n_human_listed=int((df.label == 0).sum()), n_version_listed=int((df.label == 1).sum()),
                  missing_on_disk_per_set=n_missing,
                  missing_on_disk_total=int((~df.on_disk).sum()),
                  empty_files_evaluated=int(ev.empty_file.sum())),
        split={k: int(v) for k, v in sizes.items()},
        **extra,
    )
    for k in sets:
        part = ev[ev.set == k]
        result[f"{k}_metrics"] = metrics(part.label, part.pred)
        result[f"{k}_metrics"]["n_evaluated"] = int(len(part))
    if split_type == "snippet":
        folds = []
        for fold in range(1, 6):
            part = ev[ev.cv_fold == fold]                      # folds on the 80% (train+val) part
            m = metrics(part.label, part.pred); m["fold"] = fold
            folds.append(m)
        mean, std = _mean_std(folds)
        result["cv"] = dict(n_splits=5,
                            method="StratifiedKFold(n_splits=5, shuffle=True, random_state=42) -- on the 80% train+val part "
                                   "(the GridSearchCV cv of the 2025 experiments). ADDITIONAL INFORMATION: the reported validation values come from the fixed validation set.",
                            folds=folds, mean=mean, std=std)
    result["time_sec"] = round(time.time() - t0, 1)
    result["date"] = time.strftime("%Y-%m-%d %H:%M:%S")
    result["device"] = device

    # ---- write
    with open(output_dir / f"{name}_results.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    df.drop(columns=["path"]).to_csv(output_dir / f"{name}_split.csv", index=False, encoding="utf-8-sig")
    ev[["file", "topic", "set"] + (["cv_fold"] if split_type == "snippet" else ["group"]) +
       ["label", "label_name", "pred", "p_llm", "empty_file"]].to_csv(
        output_dir / f"{name}_predictions.csv", index=False, encoding="utf-8-sig")

    def block(m, title):
        return (f"--- {title} (n={m['n']}: human={m['n_human']}, llm={m['n_llm']}) ---\n"
                f"F1 (weighted) : {m['f1_weighted']:.4f}   Precision (weighted): {m['precision_weighted']:.4f}   "
                f"Recall (weighted): {m['recall_weighted']:.4f}   Accuracy: {m['accuracy']:.4f}\n"
                f"F1 (macro)    : {m['f1_macro']:.4f}   Precision (macro)   : {m['precision_macro']:.4f}   "
                f"Recall (macro)   : {m['recall_macro']:.4f}\n"
                f"Confusion [TN,FP,FN,TP]: [{m['confusion_matrix']['TN']},{m['confusion_matrix']['FP']},"
                f"{m['confusion_matrix']['FN']},{m['confusion_matrix']['TP']}]   prediction distribution: {m['pred_dist']}\n")
    report = [f"{arch['name']} -- processed_subdataset{subdataset} ({cfg['llm']}, {cfg['format']}) -- Human-written vs V{version}",
              f"Split: {result['split_description']}", f"Fine-tuning: NONE (control experiment), seed={SEED}, model={arch['model']}",
              f"Split sizes: {result['split']}   not found on disk: {n_missing}", ""]
    report.append(block(result["val_metrics"], "VALIDATION" + (" (fixed set: 20% split off the 80% train part)" if split_type == "snippet" else "")))
    report.append(block(result["test_metrics"], "TEST (never seen)"))
    if "train_metrics" in result:
        report.append(block(result["train_metrics"], "TRAIN (for information)"))
    if split_type == "snippet":
        report.append("ADDITIONAL INFORMATION -- 5 folds corresponding to the GridSearchCV cv of the 2025 experiments (on the 80% train+val part):")
        for m in result["cv"]["folds"]:
            report.append(block(m, f"CV fold {m['fold']}"))
        o, s = result["cv"]["mean"], result["cv"]["std"]
        report.append(f"--- CV 5 folds MEAN ± std ---\nF1 (weighted): {o['f1_weighted']:.4f} ± {s['f1_weighted']:.4f}   "
                      f"Precision: {o['precision_weighted']:.4f} ± {s['precision_weighted']:.4f}   "
                      f"Recall: {o['recall_weighted']:.4f} ± {s['recall_weighted']:.4f}   Accuracy: {o['accuracy']:.4f} ± {s['accuracy']:.4f}\n")
    report.append(f"Time: {result['time_sec']} s   Device: {device}   Date: {result['date']}")
    text = "\n".join(report)
    (output_dir / f"{name}_summary.txt").write_text(text, encoding="utf-8")
    print("\n" + text)
    print(f"\nOutputs: {output_dir / (name + '_results.json')}")
    return result


if __name__ == "__main__":
    _p = argparse.ArgumentParser()
    _p.add_argument("--data", required=True,
                    help="data folder that contains the original release folders 'VEKTÖR' and 'Düz KODLAR PY'")
    _args = _p.parse_args()
    run(architecture="sensor", subdataset=18, version=5, split_type="group",
        output_dir=Path(__file__).resolve().parent / "results", data_root=Path(_args.data))
