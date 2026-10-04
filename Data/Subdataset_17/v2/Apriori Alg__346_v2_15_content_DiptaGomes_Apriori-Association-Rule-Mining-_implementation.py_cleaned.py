
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
def load_data(file_path):
    dataset = pd.read_csv(file_path, header=0)
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
def visualize_rules(rules):
    for rule in rules:
        items = [item for item in rule.items]
        support = rule.support
        confidence = rule.ordered_statistics[0].confidence
        lift = rule.ordered_statistics[0].lift
        print(f"Rule: {items[0]} -> {items[1]}")
        print(f"Support: {support:.4f}")
        print(f"Confidence: {confidence:.4f}")
        print(f"Lift: {lift:.4f}")
        print("=====================================")
if __name__ == "__main__":
    file_path = 'Nursery.csv'
    transactions = load_data(file_path)
    min_support = 0.04
    min_confidence = 0.9
    min_lift = 3
    min_length = 2
    rules = train_apriori(transactions, min_support, min_confidence, min_lift, min_length)
    visualize_rules(rules)