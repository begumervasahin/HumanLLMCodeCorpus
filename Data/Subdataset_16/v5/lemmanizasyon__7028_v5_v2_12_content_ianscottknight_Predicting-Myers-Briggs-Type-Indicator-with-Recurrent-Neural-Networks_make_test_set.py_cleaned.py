import os
import pandas as pd
import csv
import re
b1 = "data"
b2 = os.path.join(b1, "mbti_clean.csv")
b3 = ("IE", "NS", "TF", "PJ")
def fonk1(b11, dimension):
    letter_1, b4 = dimension
    b5 = []
    for _, row in b11.iterrows():
        b6 = row["type"]
        if letter_1 in b6 or b4 in b6:
            b7 = row["b7"].split("|||")
            for post in b7:
                if "http" not in post and re.search("[a-zA-Z]", post):
                    b5.append(post)
    b8 = os.path.join(b1, f"filtered_posts_{dimension}.csv")
    with open(b8, "w", b9 = "", encoding="utf-8") as csvfile:
        b10 = csv.b10(csvfile)
        b10.writerows([[post] for post in b5])
def fonk2():
    b11 = pd.read_csv(b2)
    for dimension in b3:
        fonk1(b11, dimension)
if b12 = = "__main__":
    fonk2()