import os
import pandas as pd
import csv
import re
b1 = "data"
b2 = os.path.join(b1, "mbti_clean.csv")
b3 = ("IE", "NS", "TF", "PJ")
def fonk1(b10, dimension):
    letter_1, b4 = dimension
    b5 = []
    for _, row in b10.iterrows():
        if letter_1 in row["type"] or b4 in row["type"]:
            b6 = row["b6"].split("|||")
            for post in b6:
                if "http" in post or not re.search("[a-zA-Z]", post):
                    continue
                b5.append(post)
    fonk2(b5, dimension)
def fonk2(b6, dimension):
    b7 = os.path.join(b1, f"test_{dimension}.csv")
    with open(b7, "w", b8 = "", encoding="utf-8") as f:
        b9 = csv.b9(f)
        b9.writerows([[post] for post in b6])
def fonk3():
    b10 = pd.read_csv(b2)
    for dimension in b3:
        fonk1(b10, dimension)
if b11 = = "__main__":
    fonk3()