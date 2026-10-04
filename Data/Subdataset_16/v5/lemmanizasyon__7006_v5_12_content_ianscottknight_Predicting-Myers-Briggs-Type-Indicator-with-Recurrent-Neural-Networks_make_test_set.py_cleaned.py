import os
import pandas as pd
import csv
import re
b1 = "data"
b2 = os.path.join(b1, "mbti_clean.csv")
b3 = ("IE", "NS", "TF", "PJ")
b4 = pd.read_csv(b2)
for dimension in b3:
    letter_1, b5 = dimension
    for letter in [letter_1, b5]:
        b6 = []
        for _, row in b4.iterrows():
            if letter in row["type"]:
                b7 = row["posts"].split("|||")
                b8 = [b9 for b9 in b7 if fonk1(b9)]
                b6.extend(b8)
        fonk2(b6, letter)
def fonk1(b9):
    return not ("http" in b9 or b9 = = "" or b9 is None or not re.search("[a-zA-Z]", b9))
def fonk2(posts, letter):
    b10 = os.path.join(b1, f"test_{letter}.csv")
    with open(b10, "w") as file:
        b11 = csv.b11(file)
        b11.writerows([[b9] for b9 in posts])