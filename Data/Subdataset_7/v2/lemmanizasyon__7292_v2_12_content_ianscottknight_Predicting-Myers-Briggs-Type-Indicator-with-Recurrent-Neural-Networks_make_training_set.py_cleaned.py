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
            if any([
                "http" in b9,
                b9 = = "",
                b9 is None,
                not re.search("[a-zA-Z]", b9)
            ]):
                continue
            b5[letter_1] += int(letter_1 in b7)
            b5[b6] += int(b6 in b7)
for dimension in b3:
    letter_1, b6 = dimension
    b10 = min(b5[letter_1], b5[b6])
    b11 = []
    a1 = 0
    for index, row in b4.iterrows():
        if any([letter_1 in row["type"], b6 in row["type"]]):
            b8 = row["b11"].split("|||")
            for b9 in b8:
                if any([
                    "http" in b9,
                    b9 = = "",
                    b9 is None,
                    not re.search("[a-zA-Z]", b9)
                ]):
                    continue
                b11.append(b9)
                a1 += 1
                if a1 = = b10:
                    break
    b12 = os.path.join(b1, f"train_{letter_1}.csv")
    with open(b12, "w") as f:
        b13 = csv.b13(f)
        for b9 in b11:
            b13.writerow([b9])