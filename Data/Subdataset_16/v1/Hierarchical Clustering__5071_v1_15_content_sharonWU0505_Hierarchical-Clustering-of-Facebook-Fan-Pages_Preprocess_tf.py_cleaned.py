import os
import sys
import csv
from tqdm import tqdm
import re
import jieba
def fonk1(b18):
    b1 = os.listdir(b18)
    b2 = len(b1)
    for idx, d in enumerate(b1):
        print('Progress: {}/{}'.format(idx + 1, b2))
        b3 = os.path.join(b18, d)
        b4 = os.listdir(b3)
        if not os.path.isdir('b5'):
            os.makedirs('b5')
        for page in tqdm(b4):
            b5 = dict()
            b6 = os.path.join(b3, page)
            with open(b6, 'r', b7 = 'ignore') as file:
                b8 = csv.b8((line.replace('\0', '') for line in file))
                b9 = list(b8)
                if len(b9) >= 2:
                    b10 = b9[1][0]
                    b11 = b9[1:]
                    b12 = [list(jieba.cut(re.sub(r'^https?:\/\/.*[\r\n]*', '', row[1], flags=re.MULTILINE)))
                              for row in b11 if len(row) >= 2]
                    b13 = [token for sublist in b12 for token in sublist]
                    for term in b13:
                        if term not in b5:
                            b5[term] = 0
                        b5[term] += 1
                    b14 = os.path.join('b5', b10.replace('/', '') + '.csv')
                    with open(b14, 'w', b15 = '', encoding='utf-8') as w:
                        b16 = csv.b16(w)
                        for term, freq in b5.items():
                            b16.writerow([term, freq])
if b17 = = "__main__":
    b18 = sys.argv[1]
    fonk1(b18)