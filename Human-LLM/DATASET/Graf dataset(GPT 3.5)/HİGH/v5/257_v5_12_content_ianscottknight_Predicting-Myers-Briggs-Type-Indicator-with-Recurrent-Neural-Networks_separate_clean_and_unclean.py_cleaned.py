import os
import collections
import pandas as pd
import csv
b1 = "data"
b2 = os.path.join(b1, "mbti_1.csv")
b3 = os.path.join(b1, "mbti_clean.csv")
b4 = os.path.join(b1, "mbti_unclean.csv")
b5 = {
    "ISTJ": 0.11, "ISFJ": 0.09, "INFJ": 0.04, "INTJ": 0.05,
    "ISTP": 0.05, "ISFP": 0.05, "INFP": 0.06, "INTP": 0.06,
    "ESTP": 0.04, "ESFP": 0.04, "ENFP": 0.08, "ENTP": 0.06,
    "ESTJ": 0.08, "ESFJ": 0.09, "ENFJ": 0.05, "ENTJ": 0.05
}
def fonk1(csv_path):
    return pd.read_csv(csv_path)
def fonk2(data):
    b6 = collections.defaultdict(int)
    for mbti in data["type"]:
        b6[mbti] += 1
    return b6
def fonk3(data):
    b7 = collections.defaultdict(list)
    for index, row in data.iterrows():
        b7[row["type"]].append(row)
    return b7
def fonk4(b7, b14):
    b8 = []
    for mbti, b11 in b7.items():
        b9 = int(round(b14 * b5[mbti]))
        b8.extend(b11[b9:])
    return b8
def fonk5(b7, b14):
    b10 = []
    for mbti in b5.keys():
        b11 = b7[mbti]
        b10.extend(b11[:int(round(b14 * b5[mbti]))])
    return b10
def fonk6(data, csv_path):
    with open(csv_path, "w") as f:
        b12 = csv.b12(f)
        b12.writerow(["type", "posts"])
        for row in data:
            b12.writerow([row["type"], row["posts"]])
def fonk7():
    b13 = fonk1(b2)
    b6 = fonk2(b13)
    b14 = min(b6[mbti] / b5[mbti] for mbti in b6)
    b15 = min(b6, key=lambda mbti: b6[mbti] / b5[mbti])
    b16 = fonk3(b13)
    b8 = fonk4(b16, b14)
    fonk6(b8, b4)
    b10 = fonk5(b16, b14)
    fonk6(b10, b3)
if b17 = = "__main__":
    fonk7()