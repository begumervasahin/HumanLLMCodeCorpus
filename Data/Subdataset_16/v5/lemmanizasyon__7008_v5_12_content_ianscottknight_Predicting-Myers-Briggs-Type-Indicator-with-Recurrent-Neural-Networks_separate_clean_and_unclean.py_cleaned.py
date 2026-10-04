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
b7 = b6["type"].value_counts().to_dict()
b8 = float("infinity")
b9 = None
for mbti, count in b7.items():
    b10 = count / b5[mbti]
    if b10 < b8:
        b8 = b10
        b9 = mbti
b11 = b6.groupby("type").apply(lambda x: x.to_dict(orient="records")).to_dict()
b12 = []
b13 = []
for mbti, rows in b11.items():
    b14 = int(round(b8 * b5[mbti]))
    b12.extend(rows[:b14])
    b13.extend(rows[b14:])
with open(b3, "w", b15 = '') as clean_file:
    b16 = csv.DictWriter(clean_file, fieldnames=["type", "posts"])
    b16.writeheader()
    b16.writerows(b12)
with open(b4, "w", b15 = '') as unclean_file:
    b16 = csv.DictWriter(unclean_file, fieldnames=["type", "posts"])
    b16.writeheader()
    b16.writerows(b13)