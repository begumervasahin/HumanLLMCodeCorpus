import os
import pandas as pd
import csv
import re
DATA_DIR = "data"
MBTI_CLEAN_CSV_PATH = os.path.join(DATA_DIR, "mbti_clean.csv")
DIMENSIONS = ("IE", "NS", "TF", "PJ")
df = pd.read_csv(MBTI_CLEAN_CSV_PATH)
def filter_posts(posts):
    return [post for post in posts if ("http" not in post) and post and re.search("[a-zA-Z]", post)]
def process_posts_for_letter(df, letter):
    posts = []
    for _, row in df.iterrows():
        if letter in row["type"]:
            hundred_posts = row["posts"].split("|||")
            posts.extend(filter_posts(hundred_posts))
    return posts
def write_posts_to_csv(posts, letter):
    csv_path = os.path.join(DATA_DIR, f"test_{letter}.csv")
    with open(csv_path, "w", newline='') as f:
        writer = csv.writer(f)
        for post in posts:
            writer.writerow([post])
for dimension in DIMENSIONS:
    for letter in dimension:
        posts = process_posts_for_letter(df, letter)
        write_posts_to_csv(posts, letter)