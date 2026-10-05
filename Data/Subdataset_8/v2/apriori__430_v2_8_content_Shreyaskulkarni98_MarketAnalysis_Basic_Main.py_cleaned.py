import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
file_path = 'D:\Shreyas Kulkarni\Documents\PycharmProjects\MarketAnalysis_Apriori_Basic\store_data.csv'
store_data = pd.read_csv(file_path, header=None)
print("First few rows of the dataset:")
print(store_data.head())
records = []
for i in range(len(store_data)):
    transaction = [str(store_data.values[i, j]) for j in range(len(store_data.columns))]
    records.append(transaction)
min_support = 0.0045
min_confidence = 0.2
min_lift = 3
min_length = 2
association_rules = apriori(records, min_support=min_support, min_confidence=min_confidence,
                            min_lift=min_lift, min_length=min_length)
association_results = list(association_rules)
print("\nNumber of association rules:", len(association_results))
if len(association_results) > 0:
    print("\nDetails of the first association rule:")
    print("Rule:", association_results[0][0])
    print("Support:", association_results[0][1])
    print("Confidence:", association_results[0][2][0][2])
    print("Lift:", association_results[0][2][0][3])
print("\nAll association rules:")
for item in association_results:
    pair = item[0]
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])
    print("Support: " + str(item[1]))
    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")