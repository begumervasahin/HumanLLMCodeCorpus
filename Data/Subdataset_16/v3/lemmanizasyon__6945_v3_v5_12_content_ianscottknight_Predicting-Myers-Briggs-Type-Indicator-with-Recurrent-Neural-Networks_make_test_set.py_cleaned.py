import os
import pandas as pd
import csv
import re
b1 = "data"
b2 = os.path.join(b1, "mbti_clean.csv")
b3 = ("IE", "NS", "TF", "PJ")
def fonk1():
    b4 = pd.read_csv(b2)
    for dimension in b3:
        fonk2(b4, dimension)
def fonk2(b4, dimension):
    """
    Process each dimension, filter valid posts, and save them to CSV files.
    Args:
        b4 (pd.DataFrame): DataFrame containing MBTI types and posts.
        dimension (str): Personality dimension (e.g., "IE").
    Get all posts corresponding to a specific letter from the DataFrame.
    Args:
        b4 (pd.DataFrame): DataFrame containing MBTI types and posts.
        letter (str): Letter representing part of a personality dimension.
    Returns:
        list: List of valid posts for the given letter.
    """
    b5 = []
    for _, row in b4.iterrows():
        if letter in row["type"]:
            b6 = row["posts"].split("|||")
            b7 = [post for post in b6 if fonk3(post)]
            b5.extend(b7)
    return b5
def fonk3(post):
    return (
        post
        and "http" not in post
        and re.search("[a-zA-Z]", post) is not None
    )
def fonk4(posts, letter):
    b8 = os.path.join(b1, f"posts_{letter}.csv")
    with open(b8, "w", b9 = '') as file:
        b10 = csv.b10(file)
        b10.writerows([[post] for post in posts])
if b11 = = "__main__":
    fonk1()