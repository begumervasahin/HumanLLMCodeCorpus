import os
import pandas as pd
import csv
import re
DATA_DIR = "data"
MBTI_CLEAN_CSV_PATH = os.path.join(DATA_DIR, "mbti_clean.csv")
DIMENSIONS = ("IE", "NS", "TF", "PJ")
def filter_and_save_posts(df, dimension):
    letter_1, letter_2 = dimension
    posts = []
    for index, row in df.iterrows():
        if any(letter in row["type"] for letter in [letter_1, letter_2]):
            hundred_posts = row["posts"].split("|||")
            for post in hundred_posts:
                if "http" in post or not re.search("[a-zA-Z]", post):
                    continue
                posts.append(post)
    test_csv_path = os.path.join(DATA_DIR, f"test_{dimension}.csv")
    with open(test_csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([[post] for post in posts])
def main():
    df = pd.read_csv(MBTI_CLEAN_CSV_PATH)
    for dimension in DIMENSIONS:
        filter_and_save_posts(df, dimension)
if __name__ == "__main__":
    main()