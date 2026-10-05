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
def fonk3(b12):
    b2 = {}
    for term in b12:
        b2[term] = b2.get(term, 0) + 1
    return b2
def fonk4(b2, b11):
    with open(f'b2/{b11.replace("/", "")}.csv', 'w') as file:
        b3 = csv.b3(file)
        for term, frequency in b2.items():
            b3.writerow([term, frequency])
if b4 = = "__main__":
    b5 = sys.argv[1]
    b6 = os.listdir(b5)
    b7 = len(b6)
    for idx, directory in enumerate(b6):
        print(f'Progress: {idx + 1}/{b7}')
        b8 = os.path.join(b5, directory)
        if not os.path.isdir('b2'):
            os.makedirs('b2')
        b9 = os.listdir(b8)
        for page_file in tqdm(b9):
            b2 = {}
            with open(os.path.join(b8, page_file), 'r') as file:
                b10 = list(csv.reader((line.replace('\0', '') for line in file)))
                if len(b10) >= 2:
                    b11 = b10[1][0]
                    b10 = b10[1:]
                    b12 = [fonk2(fonk1(row[1])) for row in b10 if len(row) >= 2]
                    b12 = [token for sublist in b12 for token in sublist]
                    b2 = fonk3(b12)
                    fonk4(b2, b11)