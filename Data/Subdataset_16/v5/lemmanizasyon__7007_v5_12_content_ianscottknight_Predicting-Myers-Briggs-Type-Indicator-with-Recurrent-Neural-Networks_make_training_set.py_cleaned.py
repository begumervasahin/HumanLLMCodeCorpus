import os
import collections
import pandas as pd
import csv
import re
b1 = "data"
b2 = os.path.join(b1, "mbti_unclean.csv")
b3 = ("IE", "NS", "TF", "PJ")
b4 = pd.read_csv(b2)
def fonk1(b4, dimensions):
    b5 = collections.defaultdict(int)
    for dimension in dimensions:
        letter_1, b6 = dimension
        for _, row in b4.iterrows():
            b7 = row["type"]
            b8 = row["b9"].split("|||")
            for post in b8:
                if "http" in post or not post or not re.search("[a-zA-Z]", post):
                    continue
                if letter_1 in b7:
                    b5[letter_1] += 1
                if b6 in b7:
                    b5[b6] += 1
    return b5
def fonk2(b4, letter, b12):
    b9 = []
    a1 = 0
    for _, row in b4.iterrows():
        if letter in row["type"]:
            b8 = row["b9"].split("|||")
            for post in b8:
                if a1 >= b12:
                    break
                if "http" in post or not post or not re.search("[a-zA-Z]", post):
                    continue
                b9.append(post)
                a1 += 1
    return b9
def fonk3(b9, file_path):
    with open(file_path, "w", b10 = '') as f:
        b11 = csv.b11(f)
        for post in b9:
            b11.writerow([post])
b5 = fonk1(b4, b3)
for dimension in b3:
    letter_1, b6 = dimension
    b12 = min(b5[letter_1], b5[b6])
    for letter in [letter_1, b6]:
        b9 = fonk2(b4, letter, b12)
        b13 = os.path.join(b1, f"train_{letter}.csv")
        fonk3(b9, b13)