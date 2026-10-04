import os
import pandas as pd
import csv
import re
DATA_DIR = "data"
MBTI_CLEAN_CSV_PATH = os.path.join(DATA_DIR, "mbti_clean.csv")
DIMENSIONS = ("IE", "NS", "TF", "PJ")
df = pd.read_csv(MBTI_CLEAN_CSV_PATH)
for dimension in DIMENSIONS:
    letter_1, letter_2 = dimension
    for letter in [letter_1, letter_2]:
        selected_posts = []
        for _, row in df.iterrows():
            if letter in row["type"]:
                individual_posts = row["posts"].split("|||")
                valid_posts = [post for post in individual_posts if is_valid_post(post)]
                selected_posts.extend(valid_posts)
        save_posts_to_csv(selected_posts, letter)
def is_valid_post(post):
    return not ("http" in post or post == "" or post is None or not re.search("[a-zA-Z]", post))
def save_posts_to_csv(posts, letter):
    test_csv_path = os.path.join(DATA_DIR, f"test_{letter}.csv")
    with open(test_csv_path, "w") as file:
        writer = csv.writer(file)
        writer.writerows([[post] for post in posts])