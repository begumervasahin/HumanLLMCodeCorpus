
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header=None)
transactions = []
for i in range(len(dataset)):
    transactions.append([str(dataset.values[i, j]) for j in range(len(dataset.columns))])
min_support = 0.003
min_confidence = 0.2
min_lift = 3
min_length = 2
rules = apriori(transactions, min_support=min_support, min_confidence=min_confidence, min_lift=min_lift, min_length=min_length)
results = list(rules)
for result in results:
    print("Association Rule:", result.items)
    print("Support:", result.support)
    print("Confidence:", result.ordered_statistics[0].confidence)
    print("Lift:", result.ordered_statistics[0].lift)
    print("===================================")
