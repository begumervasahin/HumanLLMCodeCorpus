
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
            support_value = patsup / collen
            aux = list(cols)
            del aux[-1]
            confidence_value = 0
            if ts[aux].all(axis=1).sum() != 0:
                confidence_value = patsup / ts[aux].all(axis=1).sum()
            pattern.append([",".join(cols), support_value * 100, confidence_value * 100])
            iterations += 1
    results_df = pd.DataFrame(pattern, columns=["Pattern", "Support", "Confidence"])
    results_df = results_df[results_df.Support >= support]
    results_df = results_df[results_df.Confidence >= confidence]
    print(results_df)
    print(f'Iterations: {iterations}')
def legs_function(legs, n, label):
    return label if legs == n else np.nan
def preprocess_zoo_data(file_path):
    zoo = pd.read_csv(file_path, sep=',', header=None)
    zoo.columns = [
        'name', 'hair', 'feathers', 'eggs', 'milk', 'airborne', 'aquatic',
        'predator', 'toothed', 'backbone', 'breathes', 'venomous', 'fins',
        'legs', 'tail', 'domestic', 'catsize', 'type'
    ]
    zoo = zoo.drop(['name', 'type'], axis=1)
    legs = zoo['legs']
    zoo = zoo.drop(['legs'], axis=1)
    for column in zoo.columns:
        zoo[column] = zoo[column].replace(1, column)
        zoo[column] = zoo[column].replace(0, np.nan)
    leg_labels = {
        'No Legs': 0, '2 Legs': 2, '4 Legs': 4, '5 Legs': 5, '6 Legs': 6, '8 Legs': 8
    }
    for label, n in leg_labels.items():
        zoo[label] = legs.apply(lambda x: legs_function(x, n, label))
    return zoo
if __name__ == '__main__':
    zoo_data_file = 'zooOriginal.csv'
    zoo_data = preprocess_zoo_data(zoo_data_file)
    apriori(zoo_data, support=30, minlen=4, confidence=97)
