import os
import sys
import csv
from tqdm import tqdm
import re
import jieba
def fonk1(b21):
    b1 = os.listdir(b21)
    b2 = len(b1)
    os.makedirs('b7', b3 = True)
    for idx, directory in enumerate(b1):
        print(f'Progress: {idx + 1}/{b2}')
        b4 = os.path.join(b21, directory)
        b5 = os.listdir(b4)
        for page in tqdm(b5, b6 = f"Processing {directory}"):
            fonk2(b4, page)
def fonk2(b4, page):
    b7 = {}
    b8 = os.path.join(b4, page)
    with open(b8, 'r', b9 = 'ignore') as file:
        b10 = csv.b10((line.replace('\0', '') for line in file))
        b11 = list(b10)
        if len(b11) >= 2:
            b12 = b11[1][0]
            b13 = b11[1:]
            b14 = fonk3(b13)
            b15 = [token for sublist in b14 for token in sublist]
            fonk4(b15, b7)
            b16 = os.path.join('b7', fonk5(b12) + '.csv')
            fonk6(b16, b7)
def fonk3(b11):
    b14 = [
        list(jieba.cut(re.sub(r'^https?:\/\/.*[\r\n]*', '', row[1], b17 = re.MULTILINE)))
        for row in b11 if len(row) >= 2
    ]
    return b14
def fonk4(b14, b7):
    for term in b14:
        b7[term] = b7.get(term, 0) + 1
def fonk5(filename):
    return re.sub(r'[\/:*?"<>|]', '', filename)
def fonk6(b16, b7):
    with open(b16, 'w', b18 = '', encoding='utf-8') as w:
        b19 = csv.b19(w)
        for term, freq in b7.items():
            b19.writerow([term, freq])
if b20 = = "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <b21>")
        sys.exit(1)
    b21 = sys.argv[1]
    fonk1(b21)