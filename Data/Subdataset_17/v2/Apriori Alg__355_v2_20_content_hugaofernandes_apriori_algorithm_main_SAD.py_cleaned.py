
from itertools import combinations
import numpy as np
import pandas as pd
def apriori(data, support, minlen, confidence):
    ts = pd.get_dummies(data.unstack().dropna()).groupby(level=1).sum()
    collen, rowlen = ts.shape
    pattern = []
    iterations = 0
    for cnum in range(minlen, rowlen + 1):
        for cols in combinations(ts, cnum):
            patsup = ts[list(cols)].all(axis=1).sum()
            a = patsup
            patsup = float(patsup) / collen
            aux = list(cols)
            del aux[-1]
            confiance = 0
            b = ts[aux].all(axis=1).sum()
            if b != 0:
                confiance = float(a) / b
            pattern.append([",".join(cols), patsup * 100, confiance * 100])
            iterations += 1
    sdf = pd.DataFrame(pattern, columns=["Pattern", "Support", "Confidence"])
    results = sdf[sdf.Support >= support]
    results = results[results.Confidence >= confidence]
    print(results)
    print('Iterations:', iterations)
def legs_function(legs, n, s):
    return s if legs == n else np.nan
zoo = pd.read_csv('zooOriginal.csv', sep=',', header=None)
zoo.columns = ['name', 'hair', 'feathers', 'eggs', 'milk', 'airborne', 'aquatic', 'predator', 'toothed', 'backbone', 'breathes', 'venomous', 'fins', 'legs', 'tail', 'domestic', 'catsize', 'type']
zoo = zoo.drop(['name', 'type'], axis=1)
legs = zoo['legs']
zoo = zoo.drop(['legs'], axis=1)
for column in zoo.columns:
    zoo[column] = zoo[column].replace(1, column).replace(0, np.nan)
zoo['No Legs'] = legs.apply(lambda x: legs_function(x, 0, 'No Legs'))
zoo['2 Legs'] = legs.apply(lambda x: legs_function(x, 2, '2 Legs'))
zoo['4 Legs'] = legs.apply(lambda x: legs_function(x, 4, '4 Legs'))
zoo['5 Legs'] = legs.apply(lambda x: legs_function(x, 5, '5 Legs'))
zoo['6 Legs'] = legs.apply(lambda x: legs_function(x, 6, '6 Legs'))
zoo['8 Legs'] = legs.apply(lambda x: legs_function(x, 8, '8 Legs'))
apriori(zoo, support=30, minlen=4, confidence=97)