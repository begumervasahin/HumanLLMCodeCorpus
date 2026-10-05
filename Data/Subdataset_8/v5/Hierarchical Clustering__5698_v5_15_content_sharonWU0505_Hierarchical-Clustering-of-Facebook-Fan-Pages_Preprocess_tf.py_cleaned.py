import os
import sys
import csv
import re
import jieba
from tqdm import tqdm
def preprocess_text(text):
    return re.sub(r'^https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)
def tokenize_text(text):
    return list(jieba.cut(text))
def calculate_term_frequencies(tokens):
    tfs = {}
    for term in tokens:
        tfs[term] = tfs.get(term, 0) + 1
    return tfs
def write_term_frequencies(tfs, page_name):
    with open(f'tfs/{page_name.replace("/", "")}.csv', 'w') as file:
        writer = csv.writer(file)
        for term, frequency in tfs.items():
            writer.writerow([term, frequency])
if __name__ == "__main__":
    posts_path = sys.argv[1]
    dirs = os.listdir(posts_path)
    dir_count = len(dirs)
    for idx, directory in enumerate(dirs):
        print(f'Progress: {idx + 1}/{dir_count}')
        pages_path = os.path.join(posts_path, directory)
        if not os.path.isdir('tfs'):
            os.makedirs('tfs')
        pages = os.listdir(pages_path)
        for page_file in tqdm(pages):
            tfs = {}
            with open(os.path.join(pages_path, page_file), 'r') as file:
                csv_content = list(csv.reader((line.replace('\0', '') for line in file)))
                if len(csv_content) >= 2:
                    page_name = csv_content[1][0]
                    csv_content = csv_content[1:]
                    tokens = [tokenize_text(preprocess_text(row[1])) for row in csv_content if len(row) >= 2]
                    tokens = [token for sublist in tokens for token in sublist]
                    tfs = calculate_term_frequencies(tokens)
                    write_term_frequencies(tfs, page_name)