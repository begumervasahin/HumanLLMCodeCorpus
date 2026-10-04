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
b9 = float("inf")
for mbti, count in b7.items():
    b10 = count / b5[mbti]
    if b10 < b9:
        b9 = b10
        b8 = mbti
b11 = collections.defaultdict(list)
for _, row in b6.iterrows():
    b11[row["type"]].append(row)
b12 = []
b13 = []
for mbti, rows in b11.items():
    b14 = int(round(b9 * b5[mbti]))
    b12.extend(rows[:b14])
    b13.extend(rows[b14:])
with open(b3, "w", b15 = '') as clean_file:
    b16 = csv.b16(clean_file)
    b16.writerow(["type", "posts"])
    for row in b12:
        b16.writerow([row["type"], row["posts"]])
with open(b4, "w", b15 = '') as unclean_file:
    b16 = csv.b16(unclean_file)
    b16.writerow(["type", "posts"])
    for row in b13:
        b16.writerow([row["type"], row["posts"]])
print("Clean and unclean data have been written to their respective CSV files.")