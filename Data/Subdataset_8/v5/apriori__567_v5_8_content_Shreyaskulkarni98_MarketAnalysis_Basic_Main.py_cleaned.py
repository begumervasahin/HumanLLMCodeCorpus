import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
def load_dataset(file_path):
    return pd.read_csv(file_path, header=None)
def display_dataset_head(dataset, num_rows=5):
    print(f"First {num_rows} rows of the dataset:")
    print(dataset.head(num_rows))
def convert_to_list_of_lists(dataset, num_rows=7501):
    records = [[str(dataset.values[i, j]) for j in range(dataset.shape[1])] for i in range(num_rows)]
    return records
def apply_apriori_algorithm(records, min_support, min_confidence, min_lift, min_length):
    return list(apriori(records, min_support=min_support, min_confidence=min_confidence,
                         min_lift=min_lift, min_length=min_length))
def display_association_rules(association_results):
    print("\nNumber of association rules:", len(association_results))
    if association_results:
        print("\nDetails of the first association rule:")
        print(association_results[0])
    print("\nAll association rules:")
    for item in association_results:
        pair = item[0]
        items = [str(x) for x in pair]
        print(f"Rule: {items[0]} -> {items[1]}")
        print(f"Support: {item[1]}")
        print(f"Confidence: {item[2][0][2]}")
        print(f"Lift: {item[2][0][3]}")
        print("=====================================")
def main():
    file_path = 'D:\Shreyas Kulkarni\Documents\PycharmProjects\MarketAnalysis_Apriori_Basic\store_data.csv'
    store_data = load_dataset(file_path)
    display_dataset_head(store_data)
    records = convert_to_list_of_lists(store_data)
    min_support = 0.0045
    min_confidence = 0.2
    min_lift = 3
    min_length = 2
    association_rules = apply_apriori_algorithm(records, min_support, min_confidence, min_lift, min_length)
    display_association_rules(association_rules)
if __name__ == "__main__":
    main()