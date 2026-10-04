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
def fonk2(b15):
    b6 = collections.defaultdict(int)
    for mbti in b15["type"]:
        b6[mbti] += 1
    return b6
def fonk3(b6, frequency_dict):
    b7 = float("inf")
    b8 = None
    for mbti, count in b6.items():
        b9 = count / frequency_dict[mbti]
        if b9 < b7:
            b7 = b9
            b8 = mbti
    return b8, b7
def fonk4(b15):
    b10 = collections.defaultdict(list)
    for _, row in b15.iterrows():
        b10[row["type"]].append(row)
    return b10
def fonk5(b10, b7, frequency_dict):
    b11 = []
    for mbti, data_list in b10.items():
        b12 = int(round(b7 * frequency_dict[mbti]))
        b11.append(data_list[b12:])
    return b11
def fonk6(file_path, header, data):
    with open(file_path, "w", b13 = '') as f:
        b14 = csv.b14(f)
        b14.writerow(header)
        for row in data:
            b14.writerow(row)
def fonk7():
    b15 = fonk1(b2)
    b6 = fonk2(b15)
    b8, b7 = fonk3(b6, b5)
    b10 = fonk4(b15)
    b11 = fonk5(b10, b7, b5)
    b16 = [(row["type"], row["posts"]) for mbti_list in b11 for row in mbti_list]
    fonk6(b4, ["type", "posts"], b16)
    b17 = [(post["type"], post["posts"]) for mbti, posts in b10.items() if mbti != b8 for post in posts]
    fonk6(b3, ["type", "posts"], b17)
if b18 = = "__main__":
    fonk7()