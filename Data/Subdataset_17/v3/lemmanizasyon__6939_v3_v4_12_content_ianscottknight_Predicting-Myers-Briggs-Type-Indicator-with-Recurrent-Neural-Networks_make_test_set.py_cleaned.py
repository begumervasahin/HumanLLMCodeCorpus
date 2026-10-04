import os
import pandas as pd
import csv
import re
DATA_DIR = "data"
MBTI_CLEAN_CSV_PATH = os.path.join(DATA_DIR, "mbti_clean.csv")
DIMENSIONS = ("IE", "NS", "TF", "PJ")
df = pd.read_csv(MBTI_CLEAN_CSV_PATH)
def is_valid_post(post):
    if "http" in post or post == "" or post is None or not re.search("[a-zA-Z]", post):
        return False
    return True
def process_posts_for_letter(df, letter):
    posts = []
    for _, row in df.iterrows():
        if letter in row["type"]:
            individual_posts = row["posts"].split("|||")
            for post in individual_posts:
                if is_valid_post(post):
                    posts.append(post)
    return posts
def save_posts_to_csv(posts, letter, data_dir):
    output_csv_path = os.path.join(data_dir, f"test_{letter}.csv")
    with open(output_csv_path, "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for post in posts:
            writer.writerow([post])
def main():
    for dimension in DIMENSIONS:
        letter_1, letter_2 = dimension
        for letter in [letter_1, letter_2]:
            posts = process_posts_for_letter(df, letter)
            save_posts_to_csv(posts, letter, DATA_DIR)
if __name__ == "__main__":
    main()