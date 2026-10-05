# HumanLLMCodeCorpus — Experiments, Results and Data

Code, data and results for the paper **"Comparing Human and LLMs Programming Styles: Insights from the Novel
HumanLLMCodeCorpus Dataset"** (IEEE Access, revised version).

The corpus contains human-written Python scripts collected from GitHub (pre-2019) and, for every script, five
versions rewritten by **GPT-3.5** and **GPT-4o** with five prompting strategies (**V1–V5**). Each script and its versions
were passed through different preprocessing pipelines (*Process IDs*), which gives **18 processed subdatasets**.
The repository contains every training script, the per-run results, and the result tables reported in the paper.

---

## Repository layout

```
.
├── README.md
├── HumanLLMCodeCorpus_Classification_Results.xlsx   # all result tables of the paper (Tables 9-11, Sniffer/Sensor, style)
├── HumanLLMCodeCorpus_Style_Metrics.py              # stylometric analysis (style metrics + significance tests)
├── Data/
│   └── Subdataset_1 ... Subdataset_18/
│       ├── Human-written_raw/                       # human-written samples (label 0)
│       └── v1/ v2/ v3/ v4/ v5/                      # LLM versions (label 1 in binary runs)
├── Experiments/                                     # one stand-alone script per run
│   ├── subdataset1 ... subdataset18/
│   │   ├── Group-Based Split/
│   │   └── Snippet-Level Split/
│   ├── sniffer_fine-tune/      sensor_fine-tune/    # GPTSniffer / CodeGPTSensor, fine-tuned
│   └── sniffer_no_fine-tune/   sensor_no_fine-tune/ # same models without fine-tuning (control experiment)
└── Results/                                         # outputs of every run
    ├── Group-Based Split/
    └── Snippet-Level Split/
```

---

## Subdatasets

`subdataset1–9` are built from the **GPT-3.5** versions and `subdataset10–18` from the **GPT-4o** versions; subdataset
*N* and *N+9* use the same preprocessing pipeline (Process ID).

| Subdataset (GPT-3.5 / GPT-4o) | Process ID | Preprocessing pipeline | Representation | Classifier family |
|---|---|---|---|---|
| 1 / 10 | 1 (3-1-4) | Code similarity detection + high-level common format transformation | Screenshot (PNG) | CNN |
| 2 / 11 | 2 (3-1-5) | Code similarity detection + high-level common format transformation | AST graph (PNG) | CNN |
| 3 / 12 | 3 (3-2-4) | Code similarity detection + low-level common format transformation | Screenshot (PNG) | CNN |
| 4 / 13 | 4 (3-2-5) | Code similarity detection + low-level common format transformation | AST graph (PNG) | CNN |
| 5 / 14 | 5 (3-4) | Code similarity detection | Screenshot (PNG) | CNN |
| 6 / 15 | 6 (3-5) | Code similarity detection | AST graph (PNG) | CNN |
| 7 / 16 | 7 (3-1) | Code similarity detection + high-level common format transformation | Source code → CodeBERT / CodeT5 embeddings | LR / SVM / AdaBoost; GPTSniffer, CodeGPTSensor |
| 8 / 17 | 8 (3-2) | Code similarity detection + low-level common format transformation | Source code → CodeBERT / CodeT5 embeddings | LR / SVM / AdaBoost; GPTSniffer, CodeGPTSensor |
| 9 / 18 | 9 (3) | Code similarity detection only (deduplication) | Source code → CodeBERT / CodeT5 embeddings | LR / SVM / AdaBoost; GPTSniffer, CodeGPTSensor |

### `Data/`

Every subdataset folder has the same structure: `Human-written_raw/` (label 0) and `v1/ … v5/` (the LLM versions).

* **Screenshots** (subdatasets 1, 3, 5, 10, 12, 14) and **AST graphs** (2, 4, 6, 11, 13, 15) are PNG images.
* **Source code** (7, 8, 9, 16, 17, 18) is stored as text files (`.py` / `.txt`).
* A sample and its versions share the same source-file stem in the file name, e.g.
  `…_10_content_<author>_<repo>_<file>.py` (human) and `…_v1_10_content_<author>_<repo>_<file>.py` (V1).
  This *family key* (`<index>_content_<author>_<repo>_<file>`) is what the group-based split uses.
* **Subdataset 11** contains only `v4` and `v5` (no V1–V3 graphs exist for this pipeline). Its human-written AST graphs
  were regenerated on 2026-10-04 with the original graph-drawing code at the same size and style as `v4`/`v5`
  (400×400), because the previously stored human graphs had been drawn at a different resolution (1600×1600).
* The CodeBERT/CodeT5 **embedding vectors** used by the embedding-based scripts are **not included** (size). Those scripts
  expect them in `Data/Embeddings/Subdataset_N/<class folder>/{metadata.csv, codebert/vectors.pkl, codet5/vectors.pkl}`,
  or in a folder passed with `--embeddings`.

---

## Experiments (`Experiments/`)

Every run is a **single, self-contained Python script** (no shared modules); it can be run on its own and writes its
outputs to a `results/` folder next to itself. The copies of these outputs used in the paper are collected in
`Results/` (see below).

### Script naming

| Pattern | Meaning |
|---|---|
| `subdatasetN_<repr>_human_vs_vK_<split>_cv.py` | binary classification: human-written vs version K |
| `subdatasetN_<repr>_6class_<split>_cv.py` | 6-class classification: human-written, V1, …, V5 |
| `<repr>` | `screenshot`, `graph` (CNN on images) or `embedding` (classic ML on code embeddings) |
| `<split>` | `group` = **Group-Based Split**, `snippet` = **Snippet-Level Split** |

### Data splits (all runs)

* **Group-Based Split** — family-based: a human-written script and all of its LLM versions always end up in the same
  set (no leakage of the same source program between train and test). Two-stage `GroupShuffleSplit` 70/15/15 and
  `StratifiedGroupKFold` (5 folds) for cross-validation.
* **Snippet-Level Split** — stratified random 70/15/15 and `StratifiedKFold` (5 folds).
* Seed 42 everywhere. Every trained run reports 5-fold cross-validation on the train+validation part, then a final
  training and evaluation on the **held-out test set** (with a 95 % bootstrap confidence interval).
* Exception — the GPTSniffer/CodeGPTSensor **no-fine-tuning** control runs (no training): group-based 70/15/15 as
  above, but snippet-level 64/16/20 (`train_test_split` 80/20, then 20 % of the training part as validation), and
  only validation/test metrics.

### CNN runs (subdatasets 1–6, 10–15) — Table 9 and Table 11

ImageNet-pretrained backbones (VGG16/19, ResNet50, InceptionV3, MobileNetV2, NASNetMobile, DenseNet169,
EfficientNetB0); the backbone is frozen except for its last block. Input 320×320 (antialiased resize, no cropping),
model-specific ImageNet preprocessing, dense head (512 units, L2 1e-4), Adam (lr 1e-4, clipnorm 1.0), at most 20
epochs with early stopping on validation cross-entropy (patience 4) and ReduceLROnPlateau, balanced class weights,
mixed precision, and one automatic retry with lr/10 if a run collapses to a single class. The backbone, activation
and dropout of each run follow Table 9 of the paper and are recorded in each run's `config.json`.
Requirements: TensorFlow 2.x with a GPU, scikit-learn, pandas, numpy, matplotlib.

```
python "Experiments/subdataset13/Group-Based Split/subdataset13_graph_human_vs_v4_group_cv.py"
python <script> --split-only        # only computes and saves the data split
python <script> --data <folder>     # data folder other than Data/Subdataset_N
```

### Embedding-based ML runs (subdatasets 7–9, 16–18) — Table 10 and Table 11

`StandardScaler` + Logistic Regression / linear SVM / AdaBoost on CodeBERT or CodeT5 embeddings, balanced class
weights. The hyperparameter (C, or AdaBoost's n_estimators / learning_rate) is selected in every training run by a
3-fold inner cross-validation on that run's training set only. Exception: the **6-class SVM runs of subdatasets 8,
17 and 18** use a fixed `C = 0.01` (the value selected most often in the binary runs of the same subdatasets); this is
recorded as `fixed_hp` in their `config.json`.
Requirements: scikit-learn, pandas, numpy (CPU).

```
python "Experiments/subdataset7/Group-Based Split/subdataset7_embedding_human_vs_v1_group_cv.py" --embeddings <folder>
```

### GPTSniffer and CodeGPTSensor (subdatasets 7–9, 16–18) — Sniffer/Sensor table

| Folder | Model | What it does |
|---|---|---|
| `sniffer_fine-tune/` | GPTSniffer — `microsoft/codebert-base` | full fine-tuning (encoder + classification head), lr 2e-5, ≤ 5 epochs, early stopping, balanced class weights, 5-fold CV + final training, held-out test with 95 % CI |
| `sensor_fine-tune/` | CodeGPTSensor — `microsoft/unixcoder-base-nine` | same protocol; loss = cross-entropy + triplet loss |
| `sniffer_no_fine-tune/` | GPTSniffer | **control experiment:** pretrained model with its untrained head, forward pass only (no training) |
| `sensor_no_fine-tune/` | CodeGPTSensor | **control experiment**, as above |

Fine-tuned runs use the same data split as the embedding-based ML runs; source code is normalised identically for
both classes before tokenisation. Requirements: PyTorch, transformers, scikit-learn, a GPU. The no-fine-tuning control
runs are expected to stay at chance level.

### Style metrics — `HumanLLMCodeCorpus_Style_Metrics.py`

Stylometric comparison of human-written, GPT-3.5 and GPT-4o code (lines of code, comment ratio, docstring coverage,
identifier length, single-letter identifier ratio, snake_case ratio, maximum nesting depth, cyclomatic complexity,
functions per file). Each human file is paired with its own V1–V5 versions; differences are tested with two-sided
Wilcoxon signed-rank tests, matched-pairs rank-biserial correlation as effect size and Holm correction. Comment ratio
is reported descriptively only, because comments and blank lines had been removed from the human-written files
during dataset preparation. Requirements: lizard, scipy, pandas, matplotlib, openpyxl.

---

## Results (`Results/`)

`Results/<Split>/<run name>/` holds the outputs of one run; the Sniffer/Sensor runs are grouped in
`sniffer_fine-tune/`, `sensor_fine-tune/`, `sniffer_no_fine-tune/` and `sensor_no_fine-tune/` sub-folders.

| File | Content |
|---|---|
| `results.json` | all metrics: validation, held-out test (+ 95 % CI), cross-validation folds (mean ± std); weighted / macro / micro precision, recall, F1, accuracy, MCC, ROC-AUC, cross-entropy; per-class metrics; confusion matrix; selected hyperparameters |
| `config.json` | the exact settings of the run (with a hash; a re-run with different settings does not reuse old folds) |
| `cv_fold_results.csv` | metrics of each cross-validation fold |
| `data_split.csv` | the set (train / validation / test) and CV fold of every sample |
| `predictions.csv`, `predictions_cv.csv` | per-sample predictions and class probabilities (test/validation and CV folds) |
| `confusion_matrix.csv/.png` | held-out test confusion matrix |
| `training_history.csv`, `training_curves.png` | CNN training curves |
| `run.log` | full console log of the run |

Some runs were produced by the original (Turkish-language) version of the scripts and use Turkish file and key names:
the fine-tuned Sniffer/Sensor runs and the subdataset 11 runs (`sonuc.json` = results, `ayarlar.json` = settings,
`cv_kat_sonuclari.csv` = CV folds, `veri_ayrimi.csv` = data split, `tahminler*.csv` = predictions, `calisma.log` = log,
`ham` = human-written). The no-fine-tuning runs write `<run>_results.json`, `<run>_predictions.csv` and `<run>_split.csv`.
The metrics are the same in all formats.

---

## Result tables — `HumanLLMCodeCorpus_Classification_Results.xlsx`

| Sheet | Paper | Content |
|---|---|---|
| `TABLO 9` | Table 9 | binary CNN classification (screenshot and AST-graph subdatasets) |
| `TABLO 10` | Table 10 | binary classification with CodeBERT/CodeT5 embeddings + LR / SVM / AdaBoost |
| `TABLO 11` | Table 11 | 6-class classification (embedding-based ML and CNN) |
| `CodeGPTSensor ve GPTSniffer` | Sniffer/Sensor table | rows 2–121: fine-tuned; rows 122–241: without fine-tuning (control) |
| `Style_Metrics` | style analysis | style metrics and significance tests |

Every metric cell is written as **`validation/test`** (e.g. `0.7154/0.7341`), truncated (not rounded) to four decimals;
F1, Precision and Recall columns are weighted averages, followed by macro and micro columns (micro = accuracy for
single-label classification). `Params` lists the hyperparameters actually used in the final training of each run.
Every value can be traced back to the `results.json` of the corresponding run in `Results/`.

---

## Notes and limitations

* All runs use a single seed (42); variability is reported through 5-fold cross-validation and a bootstrap CI on the
  held-out test set.
* The human-written code was collected from repositories created before 2019; this reduces, but does not fully rule
  out, the chance of LLM-generated content in the human class.
* In the similarity-detection subdatasets the human-written files were cleaned differently from the LLM versions
  (comments and blank lines removed); the fine-tuned Sniffer/Sensor runs therefore normalise the code of both classes
  before training, and comment-based style metrics are not compared between human and LLM code.
* Subdataset 11 has only V4 and V5, and its human-written AST graphs were regenerated (see *Data* above).
