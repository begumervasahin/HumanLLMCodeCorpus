import os
import sys
import csv
from tqdm import tqdm
import re
import jieba
def fonk1(b21):
    b1 = os.listdir(b21)
    b2 = len(b1)
    for idx, directory in enumerate(b1):
        print(f'Progress: {idx + 1}/{b2}')
        b3 = os.path.join(b21, directory)
        b4 = os.listdir(b3)
        os.makedirs('b7', b5 = True)
        for page in tqdm(b4, b6 = f"Processing {directory}"):
            b7 = {}
            b8 = os.path.join(b3, page)
            with open(b8, 'r', b9 = 'ignore') as file:
                b10 = csv.b10((line.replace('\0', '') for line in file))
                b11 = list(b10)
                if len(b11) >= 2:
                    b12 = b11[1][0]
                    b13 = b11[1:]
                    b14 = [
                        list(jieba.cut(re.sub(r'^https?:\/\/.*[\r\n]*', '', row[1], b15 = re.MULTILINE)))
                        for row in b13 if len(row) >= 2
                    ]
                    b16 = [token for sublist in b14 for token in sublist]
                    for term in b16:
                        b7[term] = b7.get(term, 0) + 1
                    b17 = os.path.join('b7', b12.replace('/', '') + '.csv')
                    with open(b17, 'w', b18 = '', encoding='utf-8') as w:
                        b19 = csv.b19(w)
                        for term, freq in b7.items():
                            b19.writerow([term, freq])
if b20 = = "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <b21>")
        sys.exit(1)
    b21 = sys.argv[1]
    fonk1(b21)