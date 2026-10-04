import os
import collections
import pandas as pd
import csv
import re
b1 = "data"
b2 = os.path.join(b1, "mbti_unclean.csv")
b3 = ("IE", "NS", "TF", "PJ")
b4 = pd.read_csv(b2)
b5 = collections.defaultdict(int)
def fonk1(b6):
    return not any([
        "http" in b6,
        b6 = = "",
        b6 is None,
        not re.search("[a-zA-Z]", b6)
    ])
for dimension in b3:
    letter_1, b7 = dimension
    for _, row in b4.iterrows():
        b8 = row["type"]
        for b6 in row["b10"].split("|||"):
            if fonk1(b6):
                b5[letter_1] += int(letter_1 in b8)
                b5[b7] += int(b7 in b8)
for dimension in b3:
    letter_1, b7 = dimension
    b9 = min(b5[letter_1], b5[b7])
    b10 = []
    a1 = 0
    for _, row in b4.iterrows():
        if any([letter_1 in row["type"], b7 in row["type"]]):
            for b6 in row["b10"].split("|||"):
                if fonk1(b6):
                    b10.append(b6)
                    a1 += 1
                    if a1 = = b9:
                        break
        if a1 = = b9:
            break
    b11 = os.path.join(b1, f"train_{letter_1}.csv")
    with open(b11, "w", b12 = '') as f:
        b13 = csv.b13(f)
        b13.writerows([[b6] for b6 in b10])