import os
import pandas as pd
import csv
import re
b1 = "data"
b2 = os.path.join(b1, "mbti_clean.csv")
b3 = ("IE", "NS", "TF", "PJ")
def fonk1(b4):
    return not ("http" in b4 or b4 = = "" or b4 is None or not re.search("[a-zA-Z]", b4))
def fonk2(posts, letter):
    b5 = os.path.join(b1, f"filtered_posts_{letter}.csv")
    with open(b5, "w", b6 = '') as file:
        b7 = csv.b7(file)
        b7.writerows([[b4] for b4 in posts])
def fonk3(b13, dimension):
    letter_1, b8 = dimension
    for letter in [letter_1, b8]:
        b9 = []
        for _, row in b13.iterrows():
            if letter in row["type"]:
                b10 = row["posts"].split("|||")
                b11 = [b4 for b4 in b10 if fonk1(b4)]
                b9.extend(b11)
        fonk2(b9, letter)
if b12 = = "__main__":
    b13 = pd.read_csv(b2)
    for dimension in b3:
        fonk3(b13, dimension)