import os
import collections
import pandas as pd
import csv
import re
b1 = "data"
b2 = os.path.join(b1, "mbti_unclean.csv")
b3 = ("IE", "NS", "TF", "PJ")
def fonk1(b4):
    return not any([
        "http" in b4,
        b4 = = "",
        b4 is None,
        not re.search("[a-zA-Z]", b4)
    ])
def fonk2(b13, dimensions):
    b5 = collections.defaultdict(int)
    for dimension in dimensions:
        letter_1, b6 = dimension
        for _, row in b13.iterrows():
            b7 = row["type"]
            for b4 in row["b9"].split("|||"):
                if fonk1(b4):
                    b5[letter_1] += int(letter_1 in b7)
                    b5[b6] += int(b6 in b7)
    return b5
def fonk3(b13, dimensions, b5, data_dir):
    for dimension in dimensions:
        letter_1, b6 = dimension
        b8 = min(b5[letter_1], b5[b6])
        b9 = []
        a1 = 0
        for _, row in b13.iterrows():
            if any([letter_1 in row["type"], b6 in row["type"]]):
                for b4 in row["b9"].split("|||"):
                    if fonk1(b4):
                        b9.append(b4)
                        a1 += 1
                        if a1 = = b8:
                            break
            if a1 = = b8:
                break
        b10 = os.path.join(data_dir, f"train_{letter_1}.csv")
        with open(b10, "w", b11 = '') as f:
            b12 = csv.b12(f)
            b12.writerows([[b4] for b4 in b9])
def fonk4():
    b13 = pd.read_csv(b2)
    b5 = fonk2(b13, b3)
    fonk3(b13, b3, b5, b1)
if b14 = = "__main__":
    fonk4()