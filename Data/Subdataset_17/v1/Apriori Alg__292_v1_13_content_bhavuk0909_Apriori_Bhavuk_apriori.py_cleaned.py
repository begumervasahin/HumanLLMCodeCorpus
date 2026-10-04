
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
def load_data(file_path):
    dataset = pd.read_csv(file_path, header=None)
    transactions = []
    for i in range(0, dataset.shape[0]):
        transactions.append([str(dataset.values[i, j]) for j in range(0, dataset.shape[1])])
    return transactions
def train_apriori(transactions, min_support, min_confidence, min_lift, min_length):
    rules = apriori(transactions, min_support=min_support, min_confidence=min_confidence, min_lift=min_lift, min_length=min_length)
    return list(rules)
def visualize_rules(rules):
    for rule in rules:
        items = [x for x in rule.items]
        print(f"Rule: {items}")
        print(f"Support: {rule.support}")
        print(f"Confidence: {rule.ordered_statistics[0].confidence}")
        print(f"Lift: {rule.ordered_statistics[0].lift}")
        print("-" * 20)
if __name__ == "__main__":
    file_path = 'Market_Basket_Optimisation.csv'
    transactions = load_data(file_path)
    min_support = 0.003
    min_confidence = 0.2
    min_lift = 3
    min_length = 2
    rules = train_apriori(transactions, min_support, min_confidence, min_lift, min_length)
    visualize_rules(rules)