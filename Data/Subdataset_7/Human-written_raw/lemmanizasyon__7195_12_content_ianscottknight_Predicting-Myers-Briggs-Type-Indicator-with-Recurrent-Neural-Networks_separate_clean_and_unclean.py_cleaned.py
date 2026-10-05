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
b6 = pd.read_csv(b2)
b7 = collections.defaultdict(int)
for mbti in b6["type"]:
    b7[mbti] += 1
b8 = None
b9 = float("infinity")
for mbti in b7.keys():
    b10 = b7[mbti] / b5[mbti]
    if b10 < b9:
        b9 = b10
        b8 = mbti
b11 = collections.defaultdict(list)
for index, row in b6.iterrows():
    b11[row["type"]].append(row)
b12 = []
with open(b3, "w") as f:
    b13 = csv.b13(f)
    b13.writerow(["type", "posts"])
    for mbti in b5.keys():
        b14 = b11[mbti]
        for x in range(0, int(round(b9 * b5[mbti]))):
            b13.writerow(b14[x])
        b12.append(
            b14[int(round(b9 * b5[mbti])) : len(b14)]
        )
with open(b4, "w") as f:
    b13 = csv.b13(f)
    b13.writerow(["type", "posts"])
    for mbti in b12:
        for x in mbti:
            b13.writerow(x)