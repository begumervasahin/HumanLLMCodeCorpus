15. Repository: DiptaGomes/Apriori-Association-Rule-Mining-
   File: implementation.py
   URL: https:
   Code Content:
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_csv('Nursery.csv', header = 1)
transactions = []
for i in range(1, 9409):
    transactions.append([str(dataset.values[i,j]) for j in range(0, 9)])
from apyori import apriori
rules = apriori(transactions, min_support = 0.04, min_confidence = .90, min_lift = 3, min_length = 2)
results = list(rules)
print(results)
for item in results:
    pair = item[0]
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])
    print("Support: " + str(item[1]))
    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")
   README Content:
