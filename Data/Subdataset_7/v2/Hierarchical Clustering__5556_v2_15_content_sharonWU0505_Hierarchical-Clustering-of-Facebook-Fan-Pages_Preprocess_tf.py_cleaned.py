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
def fonk3(b15):
    b2 = {}
    for term in b15:
        if term not in b2:
            b2[term] = 0
        b2[term] += 1
    return b2
def fonk4(b2, b14):
    b3 = 'b2/' + b14.replace('/', '') + '.csv'
    with open(b3, 'w', b4 = 'utf-8') as file:
        b5 = csv.b5(file)
        for term, frequency in b2.items():
            b5.writerow([term, frequency])
if b6 = = "__main__":
    b7 = sys.argv[1]
    b8 = os.listdir(b7)
    b9 = len(b8)
    for idx, directory in enumerate(b8):
        print('Progress: {}/{}'.format(idx + 1, b9))
        b10 = os.path.join(b7, directory)
        b11 = os.listdir(b10)
        if not os.path.isdir('b2'):
            os.makedirs('b2')
        for page_file in tqdm(b11):
            b12 = {}
            with open(os.path.join(b10, page_file), 'r', b4 = 'utf-8') as file:
                b13 = list(csv.reader((line.replace('\0', '') for line in file)))
                if len(b13) >= 2:
                    b14 = b13[1][0]
                    b13 = b13[1:]
                    b15 = [fonk2(fonk1(row[1])) for row in b13 if len(row) >= 2]
                    b15 = [token for sublist in b15 for token in sublist]
                    b12 = fonk3(b15)
                    fonk4(b12, b14)