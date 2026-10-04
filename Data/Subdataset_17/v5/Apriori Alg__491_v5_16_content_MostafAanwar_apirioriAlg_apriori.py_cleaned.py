import itertools
import pandas as pd
from collections import defaultdict
from itertools import chain, permutations
def read_dataset(file_path, percentage):
    total_lines = sum(1 for _ in open(file_path))
    records_to_read = int((percentage / 100) * total_lines)
    return pd.read_csv(file_path, sep=' ', header=None, nrows=records_to_read).values
def generate_combinations(data_set):
    combination_counts = defaultdict(int)
    for transaction in data_set:
        for i in range(1, len(transaction) + 1):
            for combination in itertools.combinations(transaction, i):
                combination_counts[combination] += 1
    return combination_counts
def filter_by_support(combination_counts, min_support):
    return {item: count for item, count in combination_counts.items() if count >= min_support}
def calculate_confidence(combination_counts, min_confidence):
    max_size = max(len(item) for item in combination_counts)
    large_itemsets = [item for item in combination_counts if len(item) == max_size]
    confidence_values = [combination_counts[item] for item in large_itemsets]
    confidence_subset = set(chain.from_iterable(large_itemsets))
    combinations = [subset for itemset in large_itemsets
                    for i in range(1, len(itemset))
                    for subset in itertools.combinations(itemset, i)]
    permutations_list = list(permutations(confidence_subset, max_size))
    return confidence_values, combinations, permutations_list
def main():
    percentage = int(input("Enter the percentage of records to read: "))
    min_support = int(input("Enter the minimum support: "))
    min_confidence = int(input("Enter the minimum confidence percentage: "))
    file_path = "CarSales.txt"
    data_set = read_dataset(file_path, percentage)
    combination_counts = generate_combinations(data_set)
    filtered_combinations = filter_by_support(combination_counts, min_support)
    print("Filtered Itemsets:", filtered_combinations)
    confidence_values, combinations, permutations_list = calculate_confidence(filtered_combinations, min_confidence)
    print("Confidence Values:", confidence_values)
    print("Combinations:", combinations)
    print("Permutations:", permutations_list)
if __name__ == "__main__":
    main()