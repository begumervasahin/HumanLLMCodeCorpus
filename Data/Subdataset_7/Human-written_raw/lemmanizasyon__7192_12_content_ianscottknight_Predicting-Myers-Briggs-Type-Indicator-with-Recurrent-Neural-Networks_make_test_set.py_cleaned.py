import os
import collections
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
        for index, row in b4.iterrows():
            if letter in row["type"]:
                b7 = row["b6"].split("|||")
                for b8 in b7:
                    if (
                        ("http" in b8)
                        or (b8 = = "")
                        or (b8 = = None)
                        or (not re.search("[a-zA-Z]", b8))
                    ):
                        continue
                    b6.append(b8)
        b9 = os.path.join(b1, f"test_{letter}.csv")
        with open(b9, "w") as f:
            b10 = csv.b10(f)
            for b8 in b6:
                b10.writerow([b8])