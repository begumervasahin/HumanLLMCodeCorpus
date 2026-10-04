import os
import collections
import pandas as pd
import csv
DATA_DIR = "data"
MBTI_RAW_CSV_PATH = os.path.join(DATA_DIR, "mbti_1.csv")
MBTI_CLEAN_CSV_PATH = os.path.join(DATA_DIR, "mbti_clean.csv")
MBTI_UNCLEAN_CSV_PATH = os.path.join(DATA_DIR, "mbti_unclean.csv")
MBTI_TO_FREQUENCY_DICT = {
    "ISTJ": 0.11,
    "ISFJ": 0.09,
    "INFJ": 0.04,
    "INTJ": 0.05,
    "ISTP": 0.05,
    "ISFP": 0.05,
    "INFP": 0.06,
    "INTP": 0.06,
    "ESTP": 0.04,
    "ESFP": 0.04,
    "ENFP": 0.08,
    "ENTP": 0.06,
    "ESTJ": 0.08,
    "ESFJ": 0.09,
    "ENFJ": 0.05,
    "ENTJ": 0.05,
}
df = pd.read_csv(MBTI_RAW_CSV_PATH)
counts = collections.defaultdict(int)
for mbti_type in df["type"]:
    counts[mbti_type] += 1
limiting_type = None
min_size = float("infinity")
for mbti_type, count in counts.items():
    size = count / MBTI_TO_FREQUENCY_DICT[mbti_type]
    if size < min_size:
        min_size = size
        limiting_type = mbti_type
grouped_data = collections.defaultdict(list)
for _, row in df.iterrows():
    grouped_data[row["type"]].append(row)
unclean_data = []
for mbti_type, freq in MBTI_TO_FREQUENCY_DICT.items():
    type_data = grouped_data[mbti_type]
    start_idx = int(round(min_size * freq))
    unclean_data.extend(type_data[start_idx:])
with open(MBTI_UNCLEAN_CSV_PATH, "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["type", "posts"])
    for entry in unclean_data:
        writer.writerow([entry["type"], entry["posts"]])
clean_data = []
for mbti_type, type_data in grouped_data.items():
    if mbti_type != limiting_type:
        clean_data.extend(type_data)
with open(MBTI_CLEAN_CSV_PATH, "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["type", "posts"])
    for entry in clean_data:
        writer.writerow([entry["type"], entry["posts"]])