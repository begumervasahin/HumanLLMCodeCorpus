import os
import pandas as pd
import csv
import re
b1 = "data"
b2 = os.path.join(b1, "mbti_clean.csv")
b3 = ["IE", "NS", "TF", "PJ"]
def fonk1(post):
    """
    Checks if a post is valid (i.e., does not contain "http" and contains letters).
    Parameters:
    - post (str): The post text to validate.
    Returns:
    - bool: True if the post is valid, False otherwise.
    """
    return "http" not in post and re.search("[a-zA-Z]", post) is not None
def fonk2(row, dimension):
    letter_1, b4 = dimension
    if letter_1 in row["type"] or b4 in row["type"]:
        b5 = row["b5"].split("|||")
        return [post for post in b5 if fonk1(post)]
    return []
def fonk3(b10, dimension):
    """
    Filters b5 based on the given MBTI dimension and saves them to a CSV file.
    Parameters:
    - b10 (DataFrame): The DataFrame containing MBTI types and b5.
    - dimension (str): The MBTI dimension to filter b5 by (e.g., "IE", "NS").
    """
    b6 = []
    for _, row in b10.iterrows():
        b6.extend(fonk2(row, dimension))
    b7 = os.path.join(b1, f"filtered_posts_{dimension}.csv")
    with open(b7, "w", b8 = "", encoding="utf-8") as file:
        b9 = csv.b9(file)
        b9.writerows([[post] for post in b6])
def fonk4():
    b10 = pd.read_csv(b2)
    for dimension in b3:
        fonk3(b10, dimension)
if b11 = = "__main__":
    fonk4()