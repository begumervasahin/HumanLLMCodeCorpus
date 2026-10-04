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
for mbti in df["type"]:
    counts[mbti] += 1
limiting_type = None
min_size = float("infinity")
for mbti in counts.keys():
    size = counts[mbti] / MBTI_TO_FREQUENCY_DICT[mbti]
    if size < min_size:
        min_size = size
        limiting_type = mbti
dic = collections.defaultdict(list)
for index, row in df.iterrows():
    dic[row["type"]].append(row)
clean_data = []
unclean_data = []
for mbti in MBTI_TO_FREQUENCY_DICT.keys():
    list1 = dic[mbti]
    clean_count = int(round(min_size * MBTI_TO_FREQUENCY_DICT[mbti]))
    clean_data.extend(list1[:clean_count])
    unclean_data.extend(list1[clean_count:])
with open(MBTI_CLEAN_CSV_PATH, "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["type", "posts"])
    for row in clean_data:
        writer.writerow([row["type"], row["posts"]])
with open(MBTI_UNCLEAN_CSV_PATH, "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["type", "posts"])
    for row in unclean_data:
        writer.writerow([row["type"], row["posts"]])
print("Clean and unclean data have been written to their respective CSV files.")