import os
import pandas as pd
import csv
import re
DATA_DIR = "data"
MBTI_CLEAN_CSV_PATH = os.path.join(DATA_DIR, "mbti_clean.csv")
DIMENSIONS = ("IE", "NS", "TF", "PJ")
def filter_and_save_posts(df, dimension):
    letter_1, letter_2 = dimension
    filtered_posts = []
    for _, row in df.iterrows():
        mbti_type = row["type"]
        if letter_1 in mbti_type or letter_2 in mbti_type:
            posts = row["posts"].split("|||")
            for post in posts:
                if "http" not in post and re.search("[a-zA-Z]", post):
                    filtered_posts.append(post)
    output_csv_path = os.path.join(DATA_DIR, f"filtered_posts_{dimension}.csv")
    with open(output_csv_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows([[post] for post in filtered_posts])
def main():
    df = pd.read_csv(MBTI_CLEAN_CSV_PATH)
    for dimension in DIMENSIONS:
        filter_and_save_posts(df, dimension)
if __name__ == "__main__":
    main()