import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
def load_dataset(file_path):
    return pd.read_csv(file_path, header=None)
def preprocess_data(data):
    records = []
    for i in range(len(data)):
        records.append([str(data.values[i, j]) for j in range(data.shape[1])])
    return records
def apply_apriori(transactions, min_support, min_confidence, min_lift, min_length):
    return list(apriori(transactions, min_support=min_support,
                        min_confidence=min_confidence, min_lift=min_lift,
                        min_length=min_length))
def print_association_rules(rules):
    print(f"Number of association rules: {len(rules)}")
    if rules:
        print(f"First association rule: {rules[0]}")
    for item in rules:
        pair = item[0]
        items = [x for x in pair]
        print(f"Rule: {items[0]} -> {items[1]}")
        print(f"Support: {item[1]}")
        print(f"Confidence: {item[2][0][2]}")
        print(f"Lift: {item[2][0][3]}")
        print("=====================================")
def main():
    file_path = 'D:/Shreyas Kulkarni/Documents/PycharmProjects/MarketAnalysis_Apriori_Basic/store_data.csv'
    store_data = load_dataset(file_path)
    print(store_data.head())
    records = preprocess_data(store_data)
    association_rules = apply_apriori(records, min_support=0.0045, min_confidence=0.2, min_lift=3, min_length=2)
    print_association_rules(association_rules)
if __name__ == "__main__":
    main()