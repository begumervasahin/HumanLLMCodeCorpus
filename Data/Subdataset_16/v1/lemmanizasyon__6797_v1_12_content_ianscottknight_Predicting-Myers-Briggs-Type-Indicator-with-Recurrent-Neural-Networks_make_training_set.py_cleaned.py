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
for dimension in b3:
    letter_1, b6 = dimension
    for index, row in b4.iterrows():
        b7 = row["type"]
        b8 = row["b11"].split("|||")
        for b9 in b8:
            if (
                ("http" in b9)
                or (b9 = = "")
                or (b9 is None)
                or (not re.search("[a-zA-Z]", b9))
            ):
                continue
            if letter_1 in b7:
                b5[letter_1] += 1
            if b6 in b7:
                b5[b6] += 1
for dimension in b3:
    letter_1, b6 = dimension
    b10 = min(b5[letter_1], b5[b6])
    for letter in [letter_1, b6]:
        b11 = []
        a1 = 0
        for index, row in b4.iterrows():
            if letter in row["type"]:
                b8 = row["b11"].split("|||")
                for b9 in b8:
                    if a1 = = b10:
                        break
                    if (
                        ("http" in b9)
                        or (b9 = = "")
                        or (b9 is None)
                        or (not re.search("[a-zA-Z]", b9))
                    ):
                        continue
                    b11.append(b9)
                    a1 += 1
        b12 = os.path.join(b1, f"train_{letter}.csv")
        with open(b12, "w", b13 = '', encoding='utf-8') as f:
            b14 = csv.b14(f)
            for b9 in b11:
                b14.writerow([b9])