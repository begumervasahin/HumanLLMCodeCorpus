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
def fonk1(b8, letter_1, b7, b6):
    if "http" in b6 or b6 = = "" or b6 is None or not re.search("[a-zA-Z]", b6):
        return
    if letter_1 in b8:
        b5[letter_1] += 1
    if b7 in b8:
        b5[b7] += 1
for dimension in b3:
    letter_1, b7 = dimension
    for _, row in b4.iterrows():
        b8 = row["type"]
        b9 = row["b11"].split("|||")
        for b6 in b9:
            fonk1(b8, letter_1, b7, b6)
for dimension in b3:
    letter_1, b7 = dimension
    b10 = min(b5[letter_1], b5[b7])
    b11 = []
    for _, row in b4.iterrows():
        if letter_1 in row["type"] or b7 in row["type"]:
            b9 = row["b11"].split("|||")
            for b6 in b9:
                if len(b11) == b10:
                    break
                fonk1(row["type"], letter_1, b7, b6)
                b11.append(b6)
    b12 = os.path.join(b1, f"train_{letter_1}.csv")
    with open(b12, "w") as f:
        b13 = csv.b13(f)
        for b6 in b11:
            b13.writerow([b6])