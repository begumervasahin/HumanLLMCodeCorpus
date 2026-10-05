import os
import collections
import pandas as pd
import csv
DATA_DIR = "data"
MBTI_RAW_CSV_PATH = os.path.join(DATA_DIR, "mbti_1.csv")
MBTI_CLEAN_CSV_PATH = os.path.join(DATA_DIR, "mbti_clean.csv")
MBTI_UNCLEAN_CSV_PATH = os.path.join(DATA_DIR, "mbti_unclean.csv")
MBTI_TO_FREQUENCY_DICT = {
    "ISTJ": 0.11, "ISFJ": 0.09, "INFJ": 0.04, "INTJ": 0.05,
    "ISTP": 0.05, "ISFP": 0.05, "INFP": 0.06, "INTP": 0.06,
    "ESTP": 0.04, "ESFP": 0.04, "ENFP": 0.08, "ENTP": 0.06,
    "ESTJ": 0.08, "ESFJ": 0.09, "ENFJ": 0.05, "ENTJ": 0.05,
}
df = pd.read_csv(MBTI_RAW_CSV_PATH)
type_counts = collections.Counter(df["type"])
min_relative_frequency = float("inf")
limiting_type = None
for mbti_type, count in type_counts.items():
    relative_frequency = count / MBTI_TO_FREQUENCY_DICT[mbti_type]
    if relative_frequency < min_relative_frequency:
        min_relative_frequency = relative_frequency
        limiting_type = mbti_type
type_groups = collections.defaultdict(list)
for _, row in df.iterrows():
    type_groups[row["type"]].append(row)
unclean_data = []
for mbti_type, posts_list in type_groups.items():
    start_index = int(round(min_relative_frequency * MBTI_TO_FREQUENCY_DICT[mbti_type]))
    unclean_data.append(posts_list[start_index:])
with open(MBTI_UNCLEAN_CSV_PATH, "w") as unclean_file:
    writer = csv.writer(unclean_file)
    writer.writerow(["type", "posts"])
    for mbti_data in unclean_data:
        writer.writerows([[post["type"], post["posts"]] for post in mbti_data])
with open(MBTI_CLEAN_CSV_PATH, "w") as clean_file:
    writer = csv.writer(clean_file)
    writer.writerow(["type", "posts"])
    for mbti_type, posts in type_groups.items():
        if mbti_type != limiting_type:
            writer.writerows([[post["type"], post["posts"]] for post in posts])