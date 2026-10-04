import os
import pandas as pd
import csv
import re
b1 = "data"
b2 = os.path.join(b1, "mbti_clean.csv")
b3 = ("IE", "NS", "TF", "PJ")
b4 = pd.read_csv(b2)
def fonk1(b7):
    b5 = []
    for b6 in b7:
        if ("http" in b6) or (b6 = = "") or (b6 is None) or (not re.search("[a-zA-Z]", b6)):
            continue
        b5.append(b6)
    return b5
def fonk2(b4, letter):
    b7 = []
    for _, row in b4.iterrows():
        if letter in row["type"]:
            b8 = row["b7"].split("|||")
            b5 = fonk1(b8)
            b7.extend(b5)
    return b7
def fonk3(b7, letter):
    b9 = os.path.join(b1, f"test_{letter}.csv")
    with open(b9, "w") as f:
        b10 = csv.b10(f)
        for b6 in b7:
            b10.writerow([b6])
for dimension in b3:
    letter_1, b11 = dimension
    for letter in [letter_1, b11]:
        b7 = fonk2(b4, letter)
        fonk3(b7, letter)