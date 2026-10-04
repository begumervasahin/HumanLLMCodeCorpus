
import numpy as np
import pandas as pd
from apyori import apriori
def load_dataset(file_path):
    return pd.read_csv(file_path, header=None)
def preprocess_data(dataset):
    transactions = []
    for i in range(len(dataset)):
        transaction = [str(dataset.values[i, j]) for j in range(dataset.shape[1])]
        transactions.append(transaction)
    return transactions
def train_apriori(transactions, min_support, min_confidence, min_lift, min_length):
    rules = apriori(transactions, min_support=min_support, min_confidence=min_confidence, min_lift=min_lift, min_length=min_length)
    return list(rules)
def visualize_results(rules):
    for rule in rules:
        items = [x for x in rule.items]
        print(f"Rule: {items[0]} -> {items[1]}")
        print(f"Support: {rule.support}")
        print(f"Confidence: {rule.ordered_statistics[0].confidence}")
        print(f"Lift: {rule.ordered_statistics[0].lift}")
        print("=====================================")
def main():
    file_path = 'Market_Basket_Optimisation.csv'
    dataset = load_dataset(file_path)
    transactions = preprocess_data(dataset)
    min_support = 0.003
    min_confidence = 0.2
    min_lift = 3
    min_length = 2
    rules = train_apriori(transactions, min_support, min_confidence, min_lift, min_length)
    visualize_results(rules)
if __name__ == "__main__":
    main()