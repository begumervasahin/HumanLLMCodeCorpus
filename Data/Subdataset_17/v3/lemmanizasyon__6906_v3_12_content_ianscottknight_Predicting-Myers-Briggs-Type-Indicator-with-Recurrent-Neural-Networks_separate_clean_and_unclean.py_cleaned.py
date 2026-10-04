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
def read_raw_data(file_path):
    return pd.read_csv(file_path)
def count_mbti_types(dataframe):
    counts = collections.defaultdict(int)
    for mbti in dataframe["type"]:
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
def group_data_by_type(dataframe):
    type_to_rows = collections.defaultdict(list)
    for _, row in dataframe.iterrows():
        type_to_rows[row["type"]].append(row)
    return type_to_rows
def separate_data(type_to_rows, frequency_dict, min_size):
    clean_data = []
    unclean_data = []
    for mbti, rows in type_to_rows.items():
        clean_count = int(round(min_size * frequency_dict[mbti]))
        clean_data.extend(rows[:clean_count])
        unclean_data.extend(rows[clean_count:])
    return clean_data, unclean_data
def write_to_csv(file_path, data, headers):
    with open(file_path, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for row in data:
            writer.writerow([row["type"], row["posts"]])
def main():
    df = read_raw_data(MBTI_RAW_CSV_PATH)
    counts = count_mbti_types(df)
    limiting_type, min_size = find_limiting_type(counts, MBTI_TO_FREQUENCY_DICT)
    type_to_rows = group_data_by_type(df)
    clean_data, unclean_data = separate_data(type_to_rows, MBTI_TO_FREQUENCY_DICT, min_size)
    write_to_csv(MBTI_CLEAN_CSV_PATH, clean_data, ["type", "posts"])
    write_to_csv(MBTI_UNCLEAN_CSV_PATH, unclean_data, ["type", "posts"])
    print("Clean and unclean data have been written to their respective CSV files.")
if __name__ == "__main__":
    main()