import os
import collections
import pandas as pd
import csv
import re
DATA_DIR = "data"
MBTI_UNCLEAN_CSV_PATH = os.path.join(DATA_DIR, "mbti_unclean.csv")
DIMENSIONS = ("IE", "NS", "TF", "PJ")
def is_valid_post(post):
    return ("http" not in post) and (post.strip() != "") and re.search("[a-zA-Z]", post)
def count_letter_occurrences(df, dimensions):
    counts = collections.defaultdict(int)
    for dimension in dimensions:
        letter_1, letter_2 = dimension
        for _, row in df.iterrows():
            mbti_type = row["type"]
            posts = row["posts"].split("|||")
            for post in posts:
                if not is_valid_post(post):
                    continue
                if letter_1 in mbti_type:
                    counts[letter_1] += 1
                if letter_2 in mbti_type:
                    counts[letter_2] += 1
    return counts
def collect_balanced_posts(df, dimensions, counts):
    for dimension in dimensions:
        letter_1, letter_2 = dimension
        limit = min(counts[letter_1], counts[letter_2])
        for letter in [letter_1, letter_2]:
            collected_posts = []
            post_count = 0
            for _, row in df.iterrows():
                if letter in row["type"]:
                    posts = row["posts"].split("|||")
                    for post in posts:
                        if post_count >= limit:
                            break
                        if not is_valid_post(post):
                            continue
                        collected_posts.append(post)
                        post_count += 1
            train_csv_path = os.path.join(DATA_DIR, f"train_{letter}.csv")
            with open(train_csv_path, "w", newline='', encoding='utf-8') as csv_file:
                writer = csv.writer(csv_file)
                for post in collected_posts:
                    writer.writerow([post])
if __name__ == "__main__":
    df = pd.read_csv(MBTI_UNCLEAN_CSV_PATH)
    counts = count_letter_occurrences(df, DIMENSIONS)
    collect_balanced_posts(df, DIMENSIONS, counts)