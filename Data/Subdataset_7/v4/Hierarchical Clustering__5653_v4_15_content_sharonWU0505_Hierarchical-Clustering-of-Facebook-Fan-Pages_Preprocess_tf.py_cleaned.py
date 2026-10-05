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
    print(f'Progress: {idx + 1}/{b3}')
    b4 = os.path.join(b1, d)
    b5 = os.listdir(b4)
    if not os.path.isdir('b6'):
        os.makedirs('b6')
    for i in tqdm(b5):
        b6 = dict()
        with open(os.path.join(b4, i), 'r') as file:
            b7 = list(csv.reader((line.replace('\0', '') for line in file)))
            if len(b7) >= 2:
                b8 = b7[1][0]
                b7 = b7[1:]
                b9 = [list(jieba.cut(re.sub(r'^https?:\/\/.*[\r\n]*', '', i[1], flags=re.MULTILINE)))
                          for i in b7 if len(i) >= 2]
                b9 = [token for sublist in b9 for token in sublist]
                for term in b9:
                    b6[term] = b6.get(term, 0) + 1
                with open(f'b6/{b8.replace("/", "")}.csv', 'w') as w:
                    b10 = csv.b10(w)
                    for term, frequency in b6.items():
                        b10.writerow([term, frequency])