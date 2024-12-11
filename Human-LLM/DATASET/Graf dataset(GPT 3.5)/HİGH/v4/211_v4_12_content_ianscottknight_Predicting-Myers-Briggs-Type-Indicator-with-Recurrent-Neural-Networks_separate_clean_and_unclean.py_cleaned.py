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
for mbti, b16 in b11.items():
    b13 = int(round(b9 * b5[mbti]))
    b12.extend(b16[b13:])
with open(b4, "w") as f:
    b14 = csv.b14(f)
    b14.writerow(["type", "posts"])
    for row in b12:
        b14.writerow([row["type"], row["posts"]])
b15 = []
for mbti in b5.keys():
    b16 = b11[mbti]
    b15.extend(b16[:int(round(b9 * b5[mbti]))])
with open(b3, "w") as f:
    b14 = csv.b14(f)
    b14.writerow(["type", "posts"])
    for row in b15:
        b14.writerow([row["type"], row["posts"]])