import os
import sys
import csv
import re
import jieba
from tqdm import tqdm
def fonk1(text):
    return re.sub(r'^https?:\/\/.*[\r\n]*', '', text, b1 = re.MULTILINE)
def fonk2(text):
    return list(jieba.cut(text))
def fonk3(b17):
    b2 = {}
    for term in b17:
        b2[term] = b2.get(term, 0) + 1
    return b2
def fonk4(b2, b16):
    b3 = f'tfs/{b16.replace("/", "")}.csv'
    with open(b3, 'w', b4 = 'utf-8') as file:
        b5 = csv.b5(file)
        for term, frequency in b2.items():
            b5.writerow([term, frequency])
if b6 = = "__main__":
    b7 = sys.argv[1]
    b8 = os.listdir(b7)
    b9 = len(b8)
    for idx, directory in enumerate(b8, b10 = 1):
        print(f'Progress: {idx}/{b9}')
        b11 = os.path.join(b7, directory)
        b12 = os.listdir(b11)
        os.makedirs('tfs', b13 = True)
        for page_file in tqdm(b12, b14 = f'Processing {directory}'):
            b2 = {}
            with open(os.path.join(b11, page_file), 'r', b4 = 'utf-8') as file:
                b15 = list(csv.reader((line.replace('\0', '') for line in file)))
                if len(b15) >= 2:
                    b16 = b15[1][0]
                    b15 = b15[1:]
                    b17 = [fonk2(fonk1(row[1])) for row in b15 if len(row) >= 2]
                    b17 = [token for sublist in b17 for token in sublist]
                    b2 = fonk3(b17)
                    fonk4(b2, b16)