import os
import sys
import csv
from tqdm import tqdm
import re
import jieba
b1 = sys.argv[1]
b2 = os.listdir(b1)
b3 = len(b2)
for idx, d in enumerate(b2):
    print('Progress: {}/{}'.format(idx + 1, b3))
    b4 = b1 + '/' + d
    b5 = os.listdir(b4)
    if not os.path.isdir('b6'):
        os.makedirs('b6')
    for i in tqdm(b5):
        b6 = dict()
        with open(b4 + '/' + i, 'b7') as file:
            b7 = list(csv.reader((line.replace('\0', '') for line in file)))
            if len(b7) >= 2:
                b8 = b7[1][0]
                b7 = b7[1:]
                b7 = [list(jieba.cut(re.sub(b7'^https?:\/\/.*[\b7\n]*', '', i[1], flags=re.MULTILINE)))
                     for i in b7 if len(i) >= 2]
                b7 = [j for i in b7 for j in i]
                for term in b7:
                    if term not in b6:
                        b6[term] = 0
                    b6[term] += 1
                with open('b6/' + b8.replace('/', '') + '.csv', 'w') as w:
                    b9 = csv.b9(w)
                    for term in b6:
                        b9.writerow([term, b6[term]])