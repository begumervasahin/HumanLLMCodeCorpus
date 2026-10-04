import os
import collections
import pandas as pd
import csv
b1 = "data"
b2 = os.path.join(b1, "mbti_1.csv")
b3 = os.path.join(b1, "mbti_clean.csv")
b4 = os.path.join(b1, "mbti_unclean.csv")
b5 = {
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
def fonk1(file_path):
    return pd.read_csv(file_path)
def fonk2(dataframe):
    b6 = collections.defaultdict(int)
    for mbti_type in dataframe["type"]:
        b6[mbti_type] += 1
    return b6
def fonk3(b6, frequency_dict):
    b7 = None
    b8 = float("infinity")
    for mbti_type, count in b6.items():
        b9 = count / frequency_dict[mbti_type]
        if b9 < b8:
            b8 = b9
            b7 = mbti_type
    return b7, b8
def fonk4(dataframe):
    b10 = collections.defaultdict(list)
    for _, row in dataframe.iterrows():
        b10[row["type"]].append(row)
    return b10
def fonk5(b10, b8, frequency_dict):
    b11 = []
    for mbti_type, freq in frequency_dict.items():
        b12 = b10[mbti_type]
        b13 = int(round(b8 * freq))
        b11.extend(b12[b13:])
    return b11
def fonk6(file_path, data, header):
    with open(file_path, "w", b14 = '') as f:
        b15 = csv.b15(f)
        b15.writerow(header)
        for entry in data:
            b15.writerow([entry["type"], entry["posts"]])
def fonk7():
    b16 = fonk1(b2)
    b6 = fonk2(b16)
    b7, b8 = fonk3(b6, b5)
    b10 = fonk4(b16)
    b11 = fonk5(b10, b8, b5)
    fonk6(b4, b11, ["type", "posts"])
    b17 = []
    for mbti_type, b12 in b10.items():
        if mbti_type != b7:
            b17.extend(b12)
    fonk6(b3, b17, ["type", "posts"])
if b18 = = "__main__":
    fonk7()