import os
import collections
import pandas as pd
import csv
import re
DATA_DIR = "data"
MBTI_UNCLEAN_CSV_PATH = os.path.join(DATA_DIR, "mbti_unclean.csv")
DIMENSIONS = ("IE", "NS", "TF", "PJ")
df = pd.read_csv(MBTI_UNCLEAN_CSV_PATH)
def count_mbti_letters(df, dimensions):
    counts = collections.defaultdict(int)
    for dimension in dimensions:
        letter_1, letter_2 = dimension
        for _, row in df.iterrows():
            mbti = row["type"]
            hundred_posts = row["posts"].split("|||")
            for post in hundred_posts:
                if "http" in post or not post or not re.search("[a-zA-Z]", post):
                    continue
                if letter_1 in mbti:
                    counts[letter_1] += 1
                if letter_2 in mbti:
                    counts[letter_2] += 1
    return counts
def collect_posts(df, letter, limit):
    posts = []
    count = 0
    for _, row in df.iterrows():
        if letter in row["type"]:
            hundred_posts = row["posts"].split("|||")
            for post in hundred_posts:
                if count >= limit:
                    break
                if "http" in post or not post or not re.search("[a-zA-Z]", post):
                    continue
                posts.append(post)
                count += 1
    return posts
def save_posts_to_csv(posts, file_path):
    with open(file_path, "w", newline='') as f:
        writer = csv.writer(f)
        for post in posts:
            writer.writerow([post])
counts = count_mbti_letters(df, DIMENSIONS)
for dimension in DIMENSIONS:
    letter_1, letter_2 = dimension
    limit = min(counts[letter_1], counts[letter_2])
    for letter in [letter_1, letter_2]:
        posts = collect_posts(df, letter, limit)
        train_csv_path = os.path.join(DATA_DIR, f"train_{letter}.csv")
        save_posts_to_csv(posts, train_csv_path)