
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
def preprocess_dataset(file_path):
    dataset = pd.read_csv(file_path, header=None)
    transactions = []
    for i in range(len(dataset)):
        transaction_items = [str(dataset.values[i, j]) for j in range(len(dataset.columns))]
        transactions.append(transaction_items)
    return transactions
def find_association_rules(transactions, min_support=0.003, min_confidence=0.2, min_lift=3, min_length=2):
    rules = apriori(transactions, min_support=min_support, min_confidence=min_confidence,
                    min_lift=min_lift, min_length=min_length)
    return list(rules)
def print_association_rules(rules):
    for rule in rules:
        print(rule)
def main():
    file_path = 'Market_Basket_Optimisation.csv'
    transactions = preprocess_dataset(file_path)
    rules = find_association_rules(transactions)
    print_association_rules(rules)
if __name__ == "__main__":
    main()