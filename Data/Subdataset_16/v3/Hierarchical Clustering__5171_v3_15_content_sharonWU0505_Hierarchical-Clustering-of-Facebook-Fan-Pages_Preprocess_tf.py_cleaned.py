import os
import sys
import csv
from tqdm import tqdm
import re
import jieba
def fonk1(b20):
    b1 = os.listdir(b20)
    b2 = len(b1)
    os.makedirs('b7', b3 = True)
    for idx, directory in enumerate(b1):
        print(f'Progress: {idx + 1}/{b2}')
        b4 = os.path.join(b20, directory)
        b5 = os.listdir(b4)
        for page in tqdm(b5, b6 = f"Processing {directory}"):
            fonk2(os.path.join(b4, page))
def fonk2(page_path):
    b7 = {}
    with open(page_path, 'r', b8 = 'ignore') as file:
        b9 = csv.b9((line.replace('\0', '') for line in file))
        b10 = list(b9)
        if len(b10) >= 2:
            b11 = b10[1][0]
            b12 = b10[1:]
            b13 = [
                list(jieba.cut(re.sub(r'^https?:\/\/.*[\r\n]*', '', row[1], b14 = re.MULTILINE)))
                for row in b12 if len(row) >= 2
            ]
            b15 = [token for sublist in b13 for token in sublist]
            for term in b15:
                b7[term] = b7.get(term, 0) + 1
            b16 = os.path.join('b7', fonk3(b11) + '.csv')
            fonk4(b16, b7)
def fonk3(filename):
    return re.sub(r'[\/:*?"<>|]', '', filename)
def fonk4(b16, b7):
    with open(b16, 'w', b17 = '', encoding='utf-8') as w:
        b18 = csv.b18(w)
        for term, freq in b7.items():
            b18.writerow([term, freq])
if b19 = = "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <b20>")
        sys.exit(1)
    b20 = sys.argv[1]
    fonk1(b20)