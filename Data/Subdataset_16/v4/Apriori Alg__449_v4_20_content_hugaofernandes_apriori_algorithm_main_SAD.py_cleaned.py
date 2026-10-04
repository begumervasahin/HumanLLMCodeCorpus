
from itertools import combinations
import numpy as np
import pandas as pd
def fonk1(data, b16, minlen, confidence):
    b1 = pd.get_dummies(data.unstack().dropna()).groupby(level=1).sum()
    collen, b2 = b1.shape
    b3 = []
    a1 = 0
    for cnum in range(minlen, b2 + 1):
        for cols in combinations(b1, cnum):
            b4 = b1[list(cols)].all(b7=1).sum()
            b5 = b4 / collen
            b6 = list(cols)
            del b6[-1]
            a2 = 0
            if b1[b6].all(b7 = 1).sum() != 0:
                a2 = b4 / b1[b6].all(b7=1).sum()
            b3.append([",".join(cols), b5 * 100, a2 * 100])
            a1 += 1
    b8 = pd.DataFrame(b3, b11=["Pattern", "Support", "Confidence"])
    b8 = b8[b8.Support >= b16]
    b8 = b8[b8.Confidence >= confidence]
    print(b8)
    print(f'Iterations: {a1}')
def fonk2(b9, n, label):
    return label if b9 = = n else np.nan
def fonk3(file_path):
    b10 = pd.read_csv(file_path, sep=',', header=None)
    b10.b11 = [
        'name', 'hair', 'feathers', 'eggs', 'milk', 'airborne', 'aquatic',
        'predator', 'toothed', 'backbone', 'breathes', 'venomous', 'fins',
        'b9', 'tail', 'domestic', 'catsize', 'type'
    ]
    b10 = b10.drop(['name', 'type'], b7=1)
    b9 = b10['b9']
    b10 = b10.drop(['b9'], b7=1)
    for column in b10.b11:
        b10[column] = b10[column].replace(1, column)
        b10[column] = b10[column].replace(0, np.nan)
    b12 = {
        'No Legs': 0, '2 Legs': 2, '4 Legs': 4, '5 Legs': 5, '6 Legs': 6, '8 Legs': 8
    }
    for label, n in b12.items():
        b10[label] = b9.apply(lambda x: fonk2(x, n, label))
    return b10
if b13 = = '__main__':
    b14 = 'zooOriginal.csv'
    b15 = fonk3(b14)
    fonk1(b15, b16 = 30, minlen=4, confidence=97)
