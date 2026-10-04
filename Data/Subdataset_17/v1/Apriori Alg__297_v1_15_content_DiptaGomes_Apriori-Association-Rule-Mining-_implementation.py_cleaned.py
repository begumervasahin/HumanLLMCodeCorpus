
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
def load_data(file_path):
    dataset = pd.read_csv(file_path, header=1)
    transactions = []
    for i in range(1, len(dataset)):
        transactions.append([str(dataset.values[i, j]) for j in range(0, dataset.shape[1])])
    return transactions
def train_apriori(transactions, min_support, min_confidence, min_lift, min_length):
    rules = apriori(transactions, min_support=min_support, min_confidence=min_confidence, min_lift=min_lift, min_length=min_length)
    return list(rules)
def visualize_rules(rules):
    for item in rules:
        pair = item[0]
        items = [x for x in pair]
        print("Rule: " + items[0] + " -> " + items[1])
        print("Support: " + str(item[1]))
        print("Confidence: " + str(item[2][0][2]))
        print("Lift: " + str(item[2][0][3]))
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