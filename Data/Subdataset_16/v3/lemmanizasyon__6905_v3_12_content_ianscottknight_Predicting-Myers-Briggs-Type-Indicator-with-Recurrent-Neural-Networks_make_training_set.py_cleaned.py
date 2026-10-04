import os
import collections
import pandas as pd
import csv
import re
b1 = "data"
b2 = os.path.join(b1, "mbti_unclean.csv")
b3 = ("IE", "NS", "TF", "PJ")
def fonk1(post):
    return ("http" not in post) and (post.strip() != "") and re.search("[a-zA-Z]", post)
def fonk2(b14, dimensions):
    b4 = collections.defaultdict(int)
    for dimension in dimensions:
        letter_1, b5 = dimension
        for _, row in b14.iterrows():
            b6 = row["type"]
            b7 = row["b7"].split("|||")
            for post in b7:
                if not fonk1(post):
                    continue
                if letter_1 in b6:
                    b4[letter_1] += 1
                if b5 in b6:
                    b4[b5] += 1
    return b4
def fonk3(b14, dimensions, b4):
    for dimension in dimensions:
        letter_1, b5 = dimension
        b8 = min(b4[letter_1], b4[b5])
        for letter in [letter_1, b5]:
            b9 = []
            a1 = 0
            for _, row in b14.iterrows():
                if letter in row["type"]:
                    b7 = row["b7"].split("|||")
                    for post in b7:
                        if a1 >= b8:
                            break
                        if not fonk1(post):
                            continue
                        b9.append(post)
                        a1 += 1
            b10 = os.path.join(b1, f"train_{letter}.csv")
            with open(b10, "w", b11 = '', encoding='utf-8') as csv_file:
                b12 = csv.b12(csv_file)
                for post in b9:
                    b12.writerow([post])
if b13 = = "__main__":
    b14 = pd.read_csv(b2)
    b4 = fonk2(b14, b3)
    fonk3(b14, b3, b4)