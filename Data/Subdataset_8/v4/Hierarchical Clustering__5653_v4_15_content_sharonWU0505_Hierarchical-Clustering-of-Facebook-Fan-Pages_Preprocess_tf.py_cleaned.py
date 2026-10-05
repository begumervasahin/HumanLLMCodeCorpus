import os
import sys
import csv
import re
import jieba
from tqdm import tqdm
posts_path = sys.argv[1]
dirs = os.listdir(posts_path)
dir_count = len(dirs)
for idx, d in enumerate(dirs):
    print(f'Progress: {idx + 1}/{dir_count}')
    pages_path = os.path.join(posts_path, d)
    pages = os.listdir(pages_path)
    if not os.path.isdir('tfs'):
        os.makedirs('tfs')
    for i in tqdm(pages):
        tfs = dict()
        with open(os.path.join(pages_path, i), 'r') as file:
            csv_content = list(csv.reader((line.replace('\0', '') for line in file)))
            if len(csv_content) >= 2:
                page_name = csv_content[1][0]
                csv_content = csv_content[1:]
                tokens = [list(jieba.cut(re.sub(r'^https?:\/\/.*[\r\n]*', '', i[1], flags=re.MULTILINE)))
                          for i in csv_content if len(i) >= 2]
                tokens = [token for sublist in tokens for token in sublist]
                for term in tokens:
                    tfs[term] = tfs.get(term, 0) + 1
                with open(f'tfs/{page_name.replace("/", "")}.csv', 'w') as w:
                    writer = csv.writer(w)
                    for term, frequency in tfs.items():
                        writer.writerow([term, frequency])