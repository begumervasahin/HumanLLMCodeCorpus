import os
import pandas as pd
import csv
import re
b1 = "data"
b2 = os.path.join(b1, "mbti_clean.csv")
b3 = ("IE", "NS", "TF", "PJ")
b4 = pd.read_csv(b2)
def fonk1(b9, letter):
    b5 = os.path.join(b1, f"test_{letter}.csv")
    with open(b5, "w", b6 = "", encoding="utf-8") as f:
        b7 = csv.b7(f)
        for b11 in b9:
            b7.writerow([b11])
for dimension in b3:
    letter_1, b8 = dimension
    for letter in [letter_1, b8]:
        b9 = []
        for index, row in b4.iterrows():
            if letter in row["type"]:
                b10 = row["b9"].split("|||")
                for b11 in b10:
                    if (
                        ("http" in b11)
                        or (b11 = = "")
                        or (b11 = = None)
                        or (not re.search("[a-zA-Z]", b11))
                    ):
                        continue
                    b9.append(b11)
        fonk1(b9, letter)
print("CSV files generated successfully.")