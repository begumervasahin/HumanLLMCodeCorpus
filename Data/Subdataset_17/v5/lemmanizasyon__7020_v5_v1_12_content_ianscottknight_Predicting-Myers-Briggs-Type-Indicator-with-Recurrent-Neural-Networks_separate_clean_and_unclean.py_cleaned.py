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
def read_data(file_path):
    return pd.read_csv(file_path)
def count_mbti_types(df):
    counts = collections.defaultdict(int)
    for mbti in df["type"]:
        counts[mbti] += 1
    return counts
def find_limiting_type(counts, frequency_dict):
    min_size = float("inf")
    limiting_type = None
    for mbti, count in counts.items():
        size = count / frequency_dict[mbti]
        if size < min_size:
            min_size = size
            limiting_type = mbti
    return limiting_type, min_size
def group_data_by_mbti(df):
    grouped_data = collections.defaultdict(list)
    for _, row in df.iterrows():
        grouped_data[row["type"]].append(row)
    return grouped_data
def prepare_unclean_data(grouped_data, min_size, frequency_dict):
    unclean_list = []
    for mbti, data_list in grouped_data.items():
        start_index = int(round(min_size * frequency_dict[mbti]))
        unclean_list.append(data_list[start_index:])
    return unclean_list
def write_csv(file_path, header, data):
    with open(file_path, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for row in data:
            writer.writerow(row)
def main():
    df = read_data(MBTI_RAW_CSV_PATH)
    counts = count_mbti_types(df)
    limiting_type, min_size = find_limiting_type(counts, MBTI_TO_FREQUENCY_DICT)
    grouped_data = group_data_by_mbti(df)
    unclean_list = prepare_unclean_data(grouped_data, min_size, MBTI_TO_FREQUENCY_DICT)
    unclean_data = [(row["type"], row["posts"]) for mbti_list in unclean_list for row in mbti_list]
    write_csv(MBTI_UNCLEAN_CSV_PATH, ["type", "posts"], unclean_data)
    clean_data = [(post["type"], post["posts"]) for mbti, posts in grouped_data.items() if mbti != limiting_type for post in posts]
    write_csv(MBTI_CLEAN_CSV_PATH, ["type", "posts"], clean_data)
if __name__ == "__main__":
    main()