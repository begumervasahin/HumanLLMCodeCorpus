import os
import sys
import csv
from tqdm import tqdm
import re
import jieba
def process_files(posts_path):
    dirs = os.listdir(posts_path)
    dir_count = len(dirs)
    os.makedirs('tfs', exist_ok=True)
    for idx, directory in enumerate(dirs):
        print(f'Progress: {idx + 1}/{dir_count}')
        pages_path = os.path.join(posts_path, directory)
        pages = os.listdir(pages_path)
        for page in tqdm(pages, desc=f"Processing {directory}"):
            process_page(pages_path, page)
def process_page(pages_path, page):
    tfs = {}
    page_path = os.path.join(pages_path, page)
    with open(page_path, 'r', errors='ignore') as file:
        reader = csv.reader((line.replace('\0', '') for line in file))
        rows = list(reader)
        if len(rows) >= 2:
            page_name = rows[1][0]
            content_rows = rows[1:]
            tokens = tokenize_text(content_rows)
            flat_tokens = [token for sublist in tokens for token in sublist]
            count_term_frequencies(flat_tokens, tfs)
            output_file = os.path.join('tfs', sanitize_filename(page_name) + '.csv')
            write_term_frequencies(output_file, tfs)
def tokenize_text(rows):
    tokens = [
        list(jieba.cut(re.sub(r'^https?:\/\/.*[\r\n]*', '', row[1], flags=re.MULTILINE)))
        for row in rows if len(row) >= 2
    ]
    return tokens
def count_term_frequencies(tokens, tfs):
    for term in tokens:
        tfs[term] = tfs.get(term, 0) + 1
def sanitize_filename(filename):
    return re.sub(r'[\/:*?"<>|]', '', filename)
def write_term_frequencies(output_file, tfs):
    with open(output_file, 'w', newline='', encoding='utf-8') as w:
        writer = csv.writer(w)
        for term, freq in tfs.items():
            writer.writerow([term, freq])
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <posts_path>")
        sys.exit(1)
    posts_path = sys.argv[1]
    process_files(posts_path)