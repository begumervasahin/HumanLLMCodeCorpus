import os
import pandas as pd
import csv
import re
DATA_DIR = "data"
MBTI_CLEAN_CSV_PATH = os.path.join(DATA_DIR, "mbti_clean.csv")
DIMENSIONS = ("IE", "NS", "TF", "PJ")
def is_valid_post(post):
    return not ("http" in post or post == "" or post is None or not re.search("[a-zA-Z]", post))
def save_posts_to_csv(posts, letter):
    csv_path = os.path.join(DATA_DIR, f"filtered_posts_{letter}.csv")
    with open(csv_path, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows([[post] for post in posts])
def process_posts_by_letter(df, letter):
    selected_posts = []
    for _, row in df.iterrows():
        if letter in row["type"]:
            individual_posts = row["posts"].split("|||")
            valid_posts = [post for post in individual_posts if is_valid_post(post)]
            selected_posts.extend(valid_posts)
    save_posts_to_csv(selected_posts, letter)
def process_dimension(df, dimension):
    letter_1, letter_2 = dimension
    for letter in [letter_1, letter_2]:
        process_posts_by_letter(df, letter)
if __name__ == "__main__":
    df = pd.read_csv(MBTI_CLEAN_CSV_PATH)
    for dimension in DIMENSIONS:
        process_dimension(df, dimension)