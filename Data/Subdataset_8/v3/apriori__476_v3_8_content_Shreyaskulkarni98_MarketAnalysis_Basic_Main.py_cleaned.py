import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
def load_dataset(file_path):
    return pd.read_csv(file_path, header=None)
def convert_to_list_of_lists(dataframe):
    records = []
    for i in range(len(dataframe)):
        transaction = [str(dataframe.values[i, j]) for j in range(len(dataframe.columns))]
        records.append(transaction)
    return records
def apply_apriori(records, min_support=0.0045, min_confidence=0.2, min_lift=3, min_length=2):
    association_rules = apriori(records, min_support=min_support, min_confidence=min_confidence,
                                min_lift=min_lift, min_length=min_length)
    return list(association_rules)
def display_results(association_results):
    print("\nNumber of association rules:", len(association_results))
    if len(association_results) > 0:
        print("\nDetails of the first association rule:")
        first_rule = association_results[0]
        print("Rule:", first_rule[0])
        print("Support:", first_rule[1])
        print("Confidence:", first_rule[2][0][2])
        print("Lift:", first_rule[2][0][3])
    print("\nAll association rules:")
    for item in association_results:
        pair = item[0]
        items = [x for x in pair]
        print("Rule: " + items[0] + " -> " + items[1])
        print("Support: " + str(item[1]))
        print("Confidence: " + str(item[2][0][2]))
        print("Lift: " + str(item[2][0][3]))
        print("=====================================")
def main():
    file_path = 'D:\Shreyas Kulkarni\Documents\PycharmProjects\MarketAnalysis_Apriori_Basic\store_data.csv'
    store_data = load_dataset(file_path)
    print("First few rows of the dataset:")
    print(store_data.head())
    records = convert_to_list_of_lists(store_data)
    association_results = apply_apriori(records)
    display_results(association_results)
if __name__ == "__main__":
    main()