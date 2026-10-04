import os
import pandas as pd
import csv
import re
b1 = "data"
b2 = os.path.join(b1, "mbti_clean.csv")
b3 = ("IE", "NS", "TF", "PJ")
b4 = pd.read_csv(b2)
def fonk1(b5):
    return [post for post in b5 if ("http" not in post) and post and re.search("[a-zA-Z]", post)]
def fonk2(b4, letter):
    b5 = []
    for _, row in b4.iterrows():
        if letter in row["type"]:
            b6 = row["b5"].split("|||")
            b5.extend(fonk1(b6))
    return b5
def fonk3(b5, letter):
    b7 = os.path.join(b1, f"test_{letter}.csv")
    with open(b7, "w", b8 = '') as f:
        b9 = csv.b9(f)
        for post in b5:
            b9.writerow([post])
for dimension in b3:
    for letter in dimension:
        b5 = fonk2(b4, letter)
        fonk3(b5, letter)