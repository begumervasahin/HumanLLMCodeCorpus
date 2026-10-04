
from itertools import combinations
import numpy as np
import pandas as pd
def apriori(data, support, minlen, confidence):
    binary_matrix = pd.get_dummies(data.unstack().dropna()).groupby(level=1).sum()
    num_transactions, num_items = binary_matrix.shape
    patterns = []
    iterations = 0
    for cnum in range(minlen, num_items + 1):
        for itemset in combinations(binary_matrix, cnum):
            support_count = binary_matrix[list(itemset)].all(axis=1).sum()
            support_value = float(support_count) / num_transactions
            antecedent = list(itemset[:-1])
            antecedent_support_count = binary_matrix[antecedent].all(axis=1).sum()
            confidence_value = 0
            if antecedent_support_count != 0:
                confidence_value = float(support_count) / antecedent_support_count
            patterns.append([",".join(itemset), support_value * 100, confidence_value * 100])
            iterations += 1
    results_df = pd.DataFrame(patterns, columns=["Pattern", "Support", "Confidence"])
    results = results_df[(results_df.Support >= support) & (results_df.Confidence >= confidence)]
    print(results)
    print('Iterations:', iterations)
def convert_legs_to_label(legs, num_legs, label):
    return label if legs == num_legs else np.nan
zoo = pd.read_csv('zooOriginal.csv', sep=',', header=None)
zoo.columns = ['name', 'hair', 'feathers', 'eggs', 'milk', 'airborne', 'aquatic', 'predator', 'toothed', 'backbone', 'breathes', 'venomous', 'fins', 'legs', 'tail', 'domestic', 'catsize', 'type']
zoo = zoo.drop(['name', 'type'], axis=1)
legs = zoo['legs']
zoo = zoo.drop(['legs'], axis=1)
for column in zoo.columns:
    zoo[column] = zoo[column].replace(1, column).replace(0, np.nan)
zoo['No Legs'] = legs.apply(lambda x: convert_legs_to_label(x, 0, 'No Legs'))
zoo['2 Legs'] = legs.apply(lambda x: convert_legs_to_label(x, 2, '2 Legs'))
zoo['4 Legs'] = legs.apply(lambda x: convert_legs_to_label(x, 4, '4 Legs'))
zoo['5 Legs'] = legs.apply(lambda x: convert_legs_to_label(x, 5, '5 Legs'))
zoo['6 Legs'] = legs.apply(lambda x: convert_legs_to_label(x, 6, '6 Legs'))
zoo['8 Legs'] = legs.apply(lambda x: convert_legs_to_label(x, 8, '8 Legs'))
apriori(zoo, support=30, minlen=4, confidence=97)