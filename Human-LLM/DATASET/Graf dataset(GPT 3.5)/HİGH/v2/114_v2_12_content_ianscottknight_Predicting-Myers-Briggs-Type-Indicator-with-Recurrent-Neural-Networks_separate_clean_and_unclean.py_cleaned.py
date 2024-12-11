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
    "ESTJ": 0.08, "ESFJ": 0.09, "ENFJ": 0.05, "ENTJ": 0.05,
}
b6 = pd.read_csv(b2)
b7 = collections.defaultdict(int)
for mbti_type in b6["type"]:
    b7[mbti_type] += 1
b8 = float("infinity")
b9 = None
for mbti_type, count in b7.items():
    b10 = count / b5[mbti_type]
    if b10 < b8:
        b8 = b10
        b9 = mbti_type
b11 = collections.defaultdict(list)
for index, row in b6.iterrows():
    b11[row["type"]].append(row)
b12 = []
for mbti_type in b5.keys():
    b13 = b11[mbti_type]
    b14 = int(round(b8 * b5[mbti_type]))
    b12.append(b13[b14:])
with open(b4, "w") as unclean_file:
    b15 = csv.b15(unclean_file)
    b15.writerow(["type", "posts"])
    for mbti_data in b12:
        for post in mbti_data:
            b15.writerow([post["type"], post["posts"]])
with open(b3, "w") as clean_file:
    b15 = csv.b15(clean_file)
    b15.writerow(["type", "posts"])
    for mbti_type, posts in b11.items():
        if mbti_type != b9:
            for post in posts:
                b15.writerow([post["type"], post["posts"]])