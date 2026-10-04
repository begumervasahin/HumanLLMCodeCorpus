import itertools
import pandas as pd
from collections import Counter, defaultdict
from itertools import chain, permutations
def read_dataset(file_path, percentage):
    num_lines = sum(1 for _ in open(file_path))
    records_to_read = int((percentage / 100) * num_lines)
    return pd.read_csv(file_path, sep=' ', header=None, nrows=records_to_read).values
def generate_combinations(data_set):
    D = defaultdict(int)
    for transaction in data_set:
        for i in range(1, len(transaction) + 1):
            for combination in itertools.combinations(transaction, i):
                D[combination] += 1
    return D
def filter_by_support(D, min_support):
    return {k: v for k, v in D.items() if v >= min_support}
def calculate_confidence(D, min_confidence):
    max_size = max(len(item) for item in D)
    large_itemsets = [item for item in D if len(item) == max_size]
    confidence_values = [D[item] for item in large_itemsets]
    confidence_subset = set(chain.from_iterable(large_itemsets))
    combinations = []
    for itemset in large_itemsets:
        for i in range(1, len(itemset)):
            for subset in itertools.combinations(itemset, i):
                combinations.append(subset)
    confidence_permutations = list(permutations(confidence_subset, max_size))
    return confidence_values, combinations, confidence_permutations
def main():
    percentage = int(input("How many % of records you want to read? "))
    min_support = int(input("What is the minimum support? "))
    min_confidence = int(input("What is the % of the minimum confidence? "))
    file_path = "CarSales.txt"
    data_set = read_dataset(file_path, percentage)
    D = generate_combinations(data_set)
    filtered_D = filter_by_support(D, min_support)
    print("Filtered Itemsets:", filtered_D)
    confidence_values, combinations, confidence_permutations = calculate_confidence(filtered_D, min_confidence)
    print("Confidence Values:", confidence_values)
    print("Combinations:", combinations)
    print("Permutations:", confidence_permutations)
if __name__ == "__main__":
    main()