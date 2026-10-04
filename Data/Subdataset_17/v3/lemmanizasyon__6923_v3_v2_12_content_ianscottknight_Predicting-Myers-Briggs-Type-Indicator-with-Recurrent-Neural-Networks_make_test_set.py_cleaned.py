import os
import pandas as pd
import csv
import re
DATA_DIR = "data"
MBTI_CLEAN_CSV_PATH = os.path.join(DATA_DIR, "mbti_clean.csv")
DIMENSIONS = ("IE", "NS", "TF", "PJ")
def filter_and_save_posts(df, dimension):
    """
    Filters posts based on the specified MBTI dimension and saves them to a CSV file.
    Args:
        df (pd.DataFrame): DataFrame containing MBTI types and posts.
        dimension (str): MBTI dimension to filter posts by (e.g., "IE", "NS").
    """
    letter_1, letter_2 = dimension
    filtered_posts = []
    for index, row in df.iterrows():
        mbti_type = row["type"]
        if letter_1 in mbti_type or letter_2 in mbti_type:
            posts = row["posts"].split("|||")
            filtered_posts.extend(
                post for post in posts
                if "http" not in post and re.search("[a-zA-Z]", post)
            )
    output_csv_path = os.path.join(DATA_DIR, f"filtered_posts_{dimension}.csv")
    save_posts_to_csv(filtered_posts, output_csv_path)
def save_posts_to_csv(posts, output_path):
    with open(output_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows([[post] for post in posts])
def main():
    df = pd.read_csv(MBTI_CLEAN_CSV_PATH)
    for dimension in DIMENSIONS:
        filter_and_save_posts(df, dimension)
if __name__ == "__main__":
    main()