
from itertools import combinations
import numpy as np
import pandas as pd
def fonk1(data, b13, minlen, confidence):
    b1 = pd.get_dummies(data.unstack().dropna()).groupby(level=1).sum()
    collen, b2 = b1.shape
    b3 = []
    a1 = 0
    for cnum in range(minlen, b2 + 1):
        for cols in combinations(b1, cnum):
            b4 = b1[list(cols)].all(axis=1).sum()
            b5 = b4
            b4 = float(b4) / collen
            b6 = list(cols)
            del b6[-1]
            a2 = 0
            b7 = b1[b6].all(axis=1).sum()
            if b7 != 0:
                a2 = float(b5) / b7
            b3.append([",".join(cols), b4 * 100, a2 * 100])
            a1 += 1
    b8 = pd.DataFrame(b3, b12=["Pattern", "Support", "Confidence"])
    b9 = b8[b8.Support >= b13]
    b9 = b9[b9.Confidence >= confidence]
    print(b9)
    print('Iterations:', a1)
def fonk2(b10, n, s):
    return s if b10 = = n else np.nan
b11 = pd.read_csv('zooOriginal.csv', sep=',', header=None)
b11.b12 = ['name', 'hair', 'feathers', 'eggs', 'milk', 'airborne', 'aquatic', 'predator', 'toothed', 'backbone', 'breathes', 'venomous', 'fins', 'b10', 'tail', 'domestic', 'catsize', 'type']
b11 = b11.drop(['name', 'type'], axis=1)
b10 = b11['b10']
b11 = b11.drop(['b10'], axis=1)
for column in b11.b12:
    b11[column] = b11[column].replace(1, column).replace(0, np.nan)
b11['No Legs'] = b10.apply(lambda x: fonk2(x, 0, 'No Legs'))
b11['2 Legs'] = b10.apply(lambda x: fonk2(x, 2, '2 Legs'))
b11['4 Legs'] = b10.apply(lambda x: fonk2(x, 4, '4 Legs'))
b11['5 Legs'] = b10.apply(lambda x: fonk2(x, 5, '5 Legs'))
b11['6 Legs'] = b10.apply(lambda x: fonk2(x, 6, '6 Legs'))
b11['8 Legs'] = b10.apply(lambda x: fonk2(x, 8, '8 Legs'))
fonk1(b11, b13 = 30, minlen=4, confidence=97)