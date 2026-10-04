import os
import pandas as pd
import csv
import re
DATA_DIR = "data"
MBTI_CLEAN_CSV_PATH = os.path.join(DATA_DIR, "mbti_clean.csv")
DIMENSIONS = ("IE", "NS", "TF", "PJ")
df = pd.read_csv(MBTI_CLEAN_CSV_PATH)
def filter_posts(posts):
    filtered_posts = []
    for post in posts:
        if ("http" in post) or (post == "") or (post is None) or (not re.search("[a-zA-Z]", post)):
            continue
        filtered_posts.append(post)
    return filtered_posts
def process_posts_for_letter(df, letter):
    posts = []
    for _, row in df.iterrows():
        if letter in row["type"]:
            hundred_posts = row["posts"].split("|||")
            filtered_posts = filter_posts(hundred_posts)
            posts.extend(filtered_posts)
    return posts
def write_posts_to_csv(posts, letter):
    test_csv_path = os.path.join(DATA_DIR, f"test_{letter}.csv")
    with open(test_csv_path, "w") as f:
        writer = csv.writer(f)
        for post in posts:
            writer.writerow([post])
for dimension in DIMENSIONS:
    letter_1, letter_2 = dimension
    for letter in [letter_1, letter_2]:
        posts = process_posts_for_letter(df, letter)
        write_posts_to_csv(posts, letter)