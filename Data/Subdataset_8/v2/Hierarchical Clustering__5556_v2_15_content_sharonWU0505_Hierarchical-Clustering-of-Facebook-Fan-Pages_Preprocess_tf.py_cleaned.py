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
        if term not in tfs:
            tfs[term] = 0
        tfs[term] += 1
    return tfs
def write_term_frequencies(tfs, page_name):
    filename = 'tfs/' + page_name.replace('/', '') + '.csv'
    with open(filename, 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        for term, frequency in tfs.items():
            writer.writerow([term, frequency])
if __name__ == "__main__":
    posts_path = sys.argv[1]
    dirs = os.listdir(posts_path)
    dir_count = len(dirs)
    for idx, directory in enumerate(dirs):
        print('Progress: {}/{}'.format(idx + 1, dir_count))
        pages_path = os.path.join(posts_path, directory)
        pages = os.listdir(pages_path)
        if not os.path.isdir('tfs'):
            os.makedirs('tfs')
        for page_file in tqdm(pages):
            term_frequencies = {}
            with open(os.path.join(pages_path, page_file), 'r', encoding='utf-8') as file:
                csv_content = list(csv.reader((line.replace('\0', '') for line in file)))
                if len(csv_content) >= 2:
                    page_name = csv_content[1][0]
                    csv_content = csv_content[1:]
                    tokens = [tokenize_text(preprocess_text(row[1])) for row in csv_content if len(row) >= 2]
                    tokens = [token for sublist in tokens for token in sublist]
                    term_frequencies = calculate_term_frequencies(tokens)
                    write_term_frequencies(term_frequencies, page_name)