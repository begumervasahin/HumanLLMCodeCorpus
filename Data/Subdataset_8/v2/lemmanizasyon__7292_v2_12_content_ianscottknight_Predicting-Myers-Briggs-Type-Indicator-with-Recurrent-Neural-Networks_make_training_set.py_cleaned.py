import os
import collections
import pandas as pd
import csv
import re
DATA_DIR = "data"
MBTI_UNCLEAN_CSV_PATH = os.path.join(DATA_DIR, "mbti_unclean.csv")
DIMENSIONS = ("IE", "NS", "TF", "PJ")
df = pd.read_csv(MBTI_UNCLEAN_CSV_PATH)
counts = collections.defaultdict(int)
for dimension in DIMENSIONS:
    letter_1, letter_2 = dimension
    for index, row in df.iterrows():
        mbti = row["type"]
        hundred_posts = row["posts"].split("|||")
        for post in hundred_posts:
            if any([
                "http" in post,
                post == "",
                post is None,
                not re.search("[a-zA-Z]", post)
            ]):
                continue
            counts[letter_1] += int(letter_1 in mbti)
            counts[letter_2] += int(letter_2 in mbti)
for dimension in DIMENSIONS:
    letter_1, letter_2 = dimension
    limit = min(counts[letter_1], counts[letter_2])
    posts = []
    i = 0
    for index, row in df.iterrows():
        if any([letter_1 in row["type"], letter_2 in row["type"]]):
            hundred_posts = row["posts"].split("|||")
            for post in hundred_posts:
                if any([
                    "http" in post,
                    post == "",
                    post is None,
                    not re.search("[a-zA-Z]", post)
                ]):
                    continue
                posts.append(post)
                i += 1
                if i == limit:
                    break
    train_csv_path = os.path.join(DATA_DIR, f"train_{letter_1}.csv")
    with open(train_csv_path, "w") as f:
        writer = csv.writer(f)
        for post in posts:
            writer.writerow([post])