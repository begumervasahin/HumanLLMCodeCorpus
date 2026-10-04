
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
def load_data(file_path):
    dataset = pd.read_csv(file_path, header=None)
    transactions = []
    for i in range(len(dataset)):
        transactions.append([str(dataset.values[i, j]) for j in range(dataset.shape[1])])
    return transactions
def train_apriori(transactions, min_support, min_confidence, min_lift, min_length):
    rules = apriori(
        transactions,
        min_support=min_support,
        min_confidence=min_confidence,
        min_lift=min_lift,
        min_length=min_length
    )
    return list(rules)
def visualize_results(rules):
    for item in rules:
        pair = item[0]
        items = [x for x in pair]
        print(f"Rule: {items[0]} -> {items[1]}")
        print(f"Support: {item[1]:.4f}")
        print(f"Confidence: {item[2][0][2]:.4f}")
        print(f"Lift: {item[2][0][3]:.4f}")
        print("=====================================")
if __name__ == "__main__":
    file_path = 'Market_Basket_Optimisation.csv'
    transactions = load_data(file_path)
    min_support = 0.003
    min_confidence = 0.2
    min_lift = 3
    min_length = 2
    rules = train_apriori(transactions, min_support, min_confidence, min_lift, min_length)
    visualize_results(rules)