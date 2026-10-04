import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
store_data = pd.read_csv('D:\\Shreyas Kulkarni\\Documents\\PycharmProjects\\MarketAnalysis_Apriori_Basic\\store_data.csv', header=None)
transactions = []
for i in range(0, len(store_data)):
    transactions.append([str(store_data.values[i, j]) for j in range(0, store_data.shape[1])])
association_rules = apriori(transactions, min_support=0.0045, min_confidence=0.2, min_lift=3, min_length=2)
association_results = list(association_rules)
print(f"Number of association rules: {len(association_results)}")
if association_results:
    print("First association rule:")
    first_rule = association_results[0]
    print(f"Items: {list(first_rule.items)}")
    print(f"Support: {first_rule.support}")
    for ordered_stat in first_rule.ordered_statistics:
        print(f"Confidence: {ordered_stat.confidence}")
        print(f"Lift: {ordered_stat.lift}")
    print("=====================================")
for item in association_results:
    pair = item.items
    items = [x for x in pair]
    print(f"Rule: {items[0]} -> {items[1] if len(items) > 1 else ''}")
    print(f"Support: {item.support}")
    for ordered_stat in item.ordered_statistics:
        print(f"Confidence: {ordered_stat.confidence}")
        print(f"Lift: {ordered_stat.lift}")
    print("=====================================")