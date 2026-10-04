import os
import pandas as pd
import csv
import re
DATA_DIR = "data"
MBTI_CLEAN_CSV_PATH = os.path.join(DATA_DIR, "mbti_clean.csv")
DIMENSIONS = ["IE", "NS", "TF", "PJ"]
def is_valid_post(post):
    """
    Checks if a post is valid (i.e., does not contain "http" and contains letters).
    Parameters:
    - post (str): The post text to validate.
    Returns:
    - bool: True if the post is valid, False otherwise.
    """
    return "http" not in post and re.search("[a-zA-Z]", post) is not None
def extract_and_filter_posts(row, dimension):
    letter_1, letter_2 = dimension
    if letter_1 in row["type"] or letter_2 in row["type"]:
        posts = row["posts"].split("|||")
        return [post for post in posts if is_valid_post(post)]
    return []
def filter_and_save_posts(df, dimension):
    """
    Filters posts based on the given MBTI dimension and saves them to a CSV file.
    Parameters:
    - df (DataFrame): The DataFrame containing MBTI types and posts.
    - dimension (str): The MBTI dimension to filter posts by (e.g., "IE", "NS").
    """
    filtered_posts = []
    for _, row in df.iterrows():
        filtered_posts.extend(extract_and_filter_posts(row, dimension))
    output_csv_path = os.path.join(DATA_DIR, f"filtered_posts_{dimension}.csv")
    with open(output_csv_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows([[post] for post in filtered_posts])
def main():
    df = pd.read_csv(MBTI_CLEAN_CSV_PATH)
    for dimension in DIMENSIONS:
        filter_and_save_posts(df, dimension)
if __name__ == "__main__":
    main()