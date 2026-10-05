import os
import pandas as pd
import csv
import re
DATA_DIR = "data"
MBTI_CLEAN_CSV_PATH = os.path.join(DATA_DIR, "mbti_clean.csv")
DIMENSIONS = ("IE", "NS", "TF", "PJ")
df = pd.read_csv(MBTI_CLEAN_CSV_PATH)
def write_posts_to_csv(posts, letter):
    csv_path = os.path.join(DATA_DIR, f"test_{letter}.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        for post in posts:
            writer.writerow([post])
for dimension in DIMENSIONS:
    letter_1, letter_2 = dimension
    for letter in [letter_1, letter_2]:
        posts = []
        for _, row in df.iterrows():
            if letter in row["type"]:
                individual_posts = row["posts"].split("|||")
                for post in individual_posts:
                    if ("http" not in post) and post and re.search("[a-zA-Z]", post):
                        posts.append(post)
        write_posts_to_csv(posts, letter)
print("CSV files generated successfully.")