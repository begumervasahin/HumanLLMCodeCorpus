
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
def load_transactions(file_path):
    dataset = pd.read_csv(file_path, header=None)
    transactions = []
    for i in range(dataset.shape[0]):
        transaction = [str(dataset.values[i, j]) for j in range(dataset.shape[1]) if str(dataset.values[i, j]) != 'nan']
        transactions.append(transaction)
    return transactions
def train_apriori(transactions, min_support, min_confidence, min_lift, min_length):
    rules = apriori(transactions, min_support=min_support, min_confidence=min_confidence, min_lift=min_lift, min_length=min_length)
    return list(rules)
def display_rules(rules):
    for rule in rules:
        items = [x for x in rule.items]
        print(f"Rule: {items}")
        print(f"Support: {rule.support}")
        for ordered_stat in rule.ordered_statistics:
            print(f"Confidence: {ordered_stat.confidence}")
            print(f"Lift: {ordered_stat.lift}")
        print("=====================================")
def main():
    file_path = 'Market_Basket_Optimisation.csv'
    transactions = load_transactions(file_path)
    min_support = 0.003
    min_confidence = 0.2
    min_lift = 3
    min_length = 2
    rules = train_apriori(transactions, min_support, min_confidence, min_lift, min_length)
    display_rules(rules)
if __name__ == "__main__":
    main()