import os
import pandas as pd
import csv
import re
DATA_DIR = "data"
MBTI_CLEAN_CSV_PATH = os.path.join(DATA_DIR, "mbti_clean.csv")
DIMENSIONS = ("IE", "NS", "TF", "PJ")
def main():
    df = pd.read_csv(MBTI_CLEAN_CSV_PATH)
    for dimension in DIMENSIONS:
        process_dimension(df, dimension)
def process_dimension(df, dimension):
    """
    Process each dimension, filter valid posts, and save them to CSV files.
    Args:
        df (pd.DataFrame): DataFrame containing MBTI types and posts.
        dimension (str): Personality dimension (e.g., "IE").
    Get all posts corresponding to a specific letter from the DataFrame.
    Args:
        df (pd.DataFrame): DataFrame containing MBTI types and posts.
        letter (str): Letter representing part of a personality dimension.
    Returns:
        list: List of valid posts for the given letter.
    """
    selected_posts = []
    for _, row in df.iterrows():
        if letter in row["type"]:
            individual_posts = row["posts"].split("|||")
            valid_posts = [post for post in individual_posts if is_valid_post(post)]
            selected_posts.extend(valid_posts)
    return selected_posts
def is_valid_post(post):
    return (
        post
        and "http" not in post
        and re.search("[a-zA-Z]", post) is not None
    )
def save_posts_to_csv(posts, letter):
    csv_path = os.path.join(DATA_DIR, f"posts_{letter}.csv")
    with open(csv_path, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows([[post] for post in posts])
if __name__ == "__main__":
    main()