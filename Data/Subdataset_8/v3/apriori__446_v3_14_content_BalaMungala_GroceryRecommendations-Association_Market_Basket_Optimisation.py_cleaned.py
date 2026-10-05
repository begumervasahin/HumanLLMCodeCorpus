
import pandas as pd
from apyori import apriori
dataset_path = "F:
dataset = pd.read_csv(dataset_path, header=None)
transactions = []
for i in range(len(dataset)):
    transactions.append([str(dataset.values[i, j]) for j in range(len(dataset.columns))])
rules = apriori(transactions,
                min_support=0.003,
                min_confidence=0.2,
                min_lift=3,
                min_length=2)
print("Association Rules:")
for rule in rules:
    print(rule)