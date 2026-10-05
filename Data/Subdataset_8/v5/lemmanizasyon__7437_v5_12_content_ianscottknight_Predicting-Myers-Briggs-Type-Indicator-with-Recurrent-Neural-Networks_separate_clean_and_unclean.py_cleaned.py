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
    "ESTJ": 0.08, "ESFJ": 0.09, "ENFJ": 0.05, "ENTJ": 0.05
}
def read_raw_data(csv_path):
    return pd.read_csv(csv_path)
def count_mbti_occurrences(data):
    counts = collections.defaultdict(int)
    for mbti in data["type"]:
        counts[mbti] += 1
    return counts
def group_data_by_mbti(data):
    groups = collections.defaultdict(list)
    for index, row in data.iterrows():
        groups[row["type"]].append(row)
    return groups
def prepare_unclean_data(groups, min_size):
    unclean_data = []
    for mbti, data_list in groups.items():
        slice_index = int(round(min_size * MBTI_TO_FREQUENCY_DICT[mbti]))
        unclean_data.extend(data_list[slice_index:])
    return unclean_data
def prepare_clean_data(groups, min_size):
    clean_data = []
    for mbti in MBTI_TO_FREQUENCY_DICT.keys():
        data_list = groups[mbti]
        clean_data.extend(data_list[:int(round(min_size * MBTI_TO_FREQUENCY_DICT[mbti]))])
    return clean_data
def write_to_csv(data, csv_path):
    with open(csv_path, "w") as f:
        writer = csv.writer(f)
        writer.writerow(["type", "posts"])
        for row in data:
            writer.writerow([row["type"], row["posts"]])
def main():
    df = read_raw_data(MBTI_RAW_CSV_PATH)
    counts = count_mbti_occurrences(df)
    min_size = min(counts[mbti] / MBTI_TO_FREQUENCY_DICT[mbti] for mbti in counts)
    limiting_type = min(counts, key=lambda mbti: counts[mbti] / MBTI_TO_FREQUENCY_DICT[mbti])
    mbti_groups = group_data_by_mbti(df)
    unclean_data = prepare_unclean_data(mbti_groups, min_size)
    write_to_csv(unclean_data, MBTI_UNCLEAN_CSV_PATH)
    clean_data = prepare_clean_data(mbti_groups, min_size)
    write_to_csv(clean_data, MBTI_CLEAN_CSV_PATH)
if __name__ == "__main__":
    main()