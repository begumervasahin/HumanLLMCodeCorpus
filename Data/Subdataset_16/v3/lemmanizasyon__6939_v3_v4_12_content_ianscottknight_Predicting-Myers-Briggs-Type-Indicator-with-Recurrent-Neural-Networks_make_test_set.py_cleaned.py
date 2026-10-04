import os
import pandas as pd
import csv
import re
b1 = "data"
b2 = os.path.join(b1, "mbti_clean.csv")
b3 = ("IE", "NS", "TF", "PJ")
b4 = pd.read_csv(b2)
def fonk1(b5):
    if "http" in b5 or b5 = = "" or b5 is None or not re.search("[a-zA-Z]", b5):
        return False
    return True
def fonk2(b4, letter):
    b6 = []
    for _, row in b4.iterrows():
        if letter in row["type"]:
            b7 = row["b6"].split("|||")
            for b5 in b7:
                if fonk1(b5):
                    b6.append(b5)
    return b6
def fonk3(b6, letter, data_dir):
    b8 = os.path.join(data_dir, f"test_{letter}.csv")
    with open(b8, "w", b9 = '', encoding='utf-8') as f:
        b10 = csv.b10(f)
        for b5 in b6:
            b10.writerow([b5])
def fonk4():
    for dimension in b3:
        letter_1, b11 = dimension
        for letter in [letter_1, b11]:
            b6 = fonk2(b4, letter)
            fonk3(b6, letter, b1)
if b12 = = "__main__":
    fonk4()