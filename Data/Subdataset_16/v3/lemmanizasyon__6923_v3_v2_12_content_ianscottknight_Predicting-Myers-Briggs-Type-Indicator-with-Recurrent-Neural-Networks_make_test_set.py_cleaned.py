import os
import pandas as pd
import csv
import re
b1 = "data"
b2 = os.path.join(b1, "mbti_clean.csv")
b3 = ("IE", "NS", "TF", "PJ")
def fonk1(b11, dimension):
    """
    Filters b7 based on the specified MBTI dimension and saves them to a CSV file.
    Args:
        b11 (pd.DataFrame): DataFrame containing MBTI types and b7.
        dimension (str): MBTI dimension to filter b7 by (e.g., "IE", "NS").
    """
    letter_1, b4 = dimension
    b5 = []
    for index, row in b11.iterrows():
        b6 = row["type"]
        if letter_1 in b6 or b4 in b6:
            b7 = row["b7"].split("|||")
            b5.extend(
                post for post in b7
                if "http" not in post and re.search("[a-zA-Z]", post)
            )
    b8 = os.path.join(b1, f"filtered_posts_{dimension}.csv")
    fonk2(b5, b8)
def fonk2(b7, output_path):
    with open(output_path, "w", b9 = "", encoding="utf-8") as file:
        b10 = csv.b10(file)
        b10.writerows([[post] for post in b7])
def fonk3():
    b11 = pd.read_csv(b2)
    for dimension in b3:
        fonk1(b11, dimension)
if b12 = = "__main__":
    fonk3()