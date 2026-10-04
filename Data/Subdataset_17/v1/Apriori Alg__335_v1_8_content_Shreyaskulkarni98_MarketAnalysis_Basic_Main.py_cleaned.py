import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
store_data = pd.read_csv('D:/Shreyas Kulkarni/Documents/PycharmProjects/MarketAnalysis_Apriori_Basic/store_data.csv', header=None)
print(store_data.head())
records = []
for i in range(0, 7501):
    records.append([str(store_data.values[i, j]) for j in range(0, 20)])
association_rules = apriori(records, min_support=0.0045, min_confidence=0.2, min_lift=3, min_length=2)
association_results = list(association_rules)
print(f"Number of association rules: {len(association_results)}")
if association_results:
    print(f"First association rule: {association_results[0]}")
for item in association_results:
    pair = item[0]
    items = [x for x in pair]
    print(f"Rule: {items[0]} -> {items[1]}")
    print(f"Support: {item[1]}")
    print(f"Confidence: {item[2][0][2]}")
    print(f"Lift: {item[2][0][3]}")
    print("=====================================")