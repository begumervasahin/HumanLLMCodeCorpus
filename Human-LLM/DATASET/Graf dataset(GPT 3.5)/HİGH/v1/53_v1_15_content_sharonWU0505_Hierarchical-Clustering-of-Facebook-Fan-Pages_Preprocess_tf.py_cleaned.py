import os
import sys
import csv
import re
import jieba
from tqdm import tqdm
b1 = sys.argv[1]
b2 = os.listdir(b1)
b3 = len(b2)
for idx, d in enumerate(b2):
    print('Progress: {}/{}'.format(idx + 1, b3))
    b4 = os.path.join(b1, d)
    b5 = os.listdir(b4)
    if not os.path.isdir('b6'):
        os.makedirs('b6')
    for i in tqdm(b5):
        b6 = dict()
        with open(os.path.join(b4, i), 'b8', b7 = 'utf-8') as file:
            b8 = list(csv.reader((line.replace('\0', '') for line in file)))
            if len(b8) >= 2:
                b9 = b8[1][0]
                b8 = b8[1:]
                b8 = [list(jieba.cut(re.sub(b8'^https?:\/\/.*[\b8\n]*', '', i[1], flags=re.MULTILINE)))
                     for i in b8 if len(i) >= 2]
                b8 = [j for i in b8 for j in i]
                for term in b8:
                    if term not in b6:
                        b6[term] = 0
                    b6[term] += 1
                with open('b6/' + b9.replace('/', '') + '.csv', 'w', b7 = 'utf-8') as w:
                    b10 = csv.b10(w)
                    for term in b6:
                        b10.writerow([term, b6[term]])