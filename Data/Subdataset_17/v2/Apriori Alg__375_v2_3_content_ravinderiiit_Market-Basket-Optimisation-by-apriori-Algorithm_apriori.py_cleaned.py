
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header=None)
transactions = []
for i in range(0, dataset.shape[0]):
    transactions.append([str(dataset.values[i, j]) for j in range(0, dataset.shape[1]) if pd.notna(dataset.values[i, j])])
min_support = 0.003
min_confidence = 0.2
min_lift = 3
min_length = 2
rules = apriori(transactions, min_support=min_support, min_confidence=min_confidence, min_lift=min_lift, min_length=min_length)
results = list(rules)
def inspect(results):
    lhs = [tuple(result.items_base) for result in results]
    rhs = [tuple(result.items_add) for result in results]
    supports = [result.support for result in results]
    confidences = [result.ordered_statistics[0].confidence for result in results]
    lifts = [result.ordered_statistics[0].lift for result in results]
    return list(zip(lhs, rhs, supports, confidences, lifts))
results_df = pd.DataFrame(inspect(results), columns=['Left Hand Side', 'Right Hand Side', 'Support', 'Confidence', 'Lift'])
print(results_df)