import itertools
import pandas as pd
def read_data(file_path, percentage):
    num_lines = sum(1 for _ in open(file_path))
    records_to_read = int((percentage / 100) * num_lines)
    data = pd.read_csv(file_path, sep=' ', header=None, nrows=records_to_read).values
    return data
def generate_combinations(data_set):
    combination_counts = {}
    for record in data_set:
        for i in range(1, len(record) + 1):
            for combo in itertools.combinations(record, i):
                combination_counts[combo] = combination_counts.get(combo, 0) + 1
    return combination_counts
def filter_combinations(combination_counts, min_support):
    return {combo: count for combo, count in combination_counts.items() if count >= min_support}
def calculate_confidence(combination_counts, min_confidence, max_size):
    for size in range(2, max_size + 1):
        for combo in (k for k in combination_counts if len(k) == size):
            for subset in itertools.combinations(combo, size - 1):
                confidence = combination_counts[combo] / combination_counts[subset]
                if confidence >= min_confidence:
                    print(f"Rule: {subset} -> {set(combo) - set(subset)}, Confidence: {confidence:.2f}")
def main():
    file_path = "CarSales.txt"
    percentage = int(input("How many % of records do you want to read? "))
    min_support = int(input("What is the minimum support? "))
    min_confidence = float(input("What is the % of the minimum confidence? ")) / 100
    data_set = read_data(file_path, percentage)
    combination_counts = generate_combinations(data_set)
    filtered_combinations = filter_combinations(combination_counts, min_support)
    print("Frequent itemsets:", filtered_combinations)
    max_size = max(len(combo) for combo in filtered_combinations)
    calculate_confidence(filtered_combinations, min_confidence, max_size)
if __name__ == "__main__":
    main()