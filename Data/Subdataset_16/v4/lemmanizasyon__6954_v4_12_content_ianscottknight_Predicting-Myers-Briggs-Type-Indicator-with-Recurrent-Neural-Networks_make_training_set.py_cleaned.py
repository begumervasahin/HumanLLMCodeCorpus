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
        b8 = row["b10"].split("|||")
        for post in b8:
            if (
                "http" in post or
                not post or
                not re.search("[a-zA-Z]", post)
            ):
                continue
            if letter_1 in b7:
                b5[letter_1] += 1
            if b6 in b7:
                b5[b6] += 1
for dimension in b3:
    letter_1, b6 = dimension
    b9 = min(b5[letter_1], b5[b6])
    for letter in [letter_1, b6]:
        b10 = []
        a1 = 0
        for index, row in b4.iterrows():
            if letter in row["type"]:
                b8 = row["b10"].split("|||")
                for post in b8:
                    if a1 = = b9:
                        break
                    if (
                        "http" in post or
                        not post or
                        not re.search("[a-zA-Z]", post)
                    ):
                        continue
                    b10.append(post)
                    a1 += 1
        b11 = os.path.join(b1, f"train_{letter}.csv")
        with open(b11, "w", b12 = '') as f:
            b13 = csv.b13(f)
            for post in b10:
                b13.writerow([post])