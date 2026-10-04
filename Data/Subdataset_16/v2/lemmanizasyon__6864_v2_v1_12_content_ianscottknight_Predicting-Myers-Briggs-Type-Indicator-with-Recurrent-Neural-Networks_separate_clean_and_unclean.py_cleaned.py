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
for mbti_type in b6["type"]:
    b7[mbti_type] += 1
b8 = None
b9 = float("infinity")
for mbti_type, count in b7.items():
    b10 = count / b5[mbti_type]
    if b10 < b9:
        b9 = b10
        b8 = mbti_type
b11 = collections.defaultdict(list)
for _, row in b6.iterrows():
    b11[row["type"]].append(row)
b12 = []
for mbti_type, freq in b5.items():
    b13 = b11[mbti_type]
    b14 = int(round(b9 * freq))
    b12.extend(b13[b14:])
with open(b4, "w", b15 = '') as f:
    b16 = csv.b16(f)
    b16.writerow(["type", "posts"])
    for entry in b12:
        b16.writerow([entry["type"], entry["posts"]])
b17 = []
for mbti_type, b13 in b11.items():
    if mbti_type != b8:
        b17.extend(b13)
with open(b3, "w", b15 = '') as f:
    b16 = csv.b16(f)
    b16.writerow(["type", "posts"])
    for entry in b17:
        b16.writerow([entry["type"], entry["posts"]])