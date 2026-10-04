import itertools
import pandas as pd
def read_data(file_path, percentage):
    num_lines = sum(1 for line in open(file_path))
    records = int((percentage / 100) * num_lines)
    dataSet = pd.read_csv(file_path, sep=' ', header=None, nrows=records).values
    return dataSet
def generate_combinations(dataSet):
    D = {}
    for record in dataSet:
        for i in range(1, len(record) + 1):
            for combo in itertools.combinations(record, i):
                if combo in D:
                    D[combo] += 1
                else:
                    D[combo] = 1
    return D
def filter_combinations(D, minSupport):
    return {k: v for k, v in D.items() if v >= minSupport}
def calculate_confidence(D, minConfidence, maxSize):
    for k in range(2, maxSize + 1):
        for combo in [k for k in D if len(k) == k]:
            for subset in itertools.combinations(combo, k - 1):
                confidence = D[combo] / D[subset]
                if confidence >= minConfidence:
                    print(f"Rule: {subset} -> {set(combo) - set(subset)}, Confidence: {confidence:.2f}")
def main():
    file_path = "CarSales.txt"
    percentage = int(input("How many % of records you want to read? "))
    minSupport = int(input("What is the minimum support? "))
    minConfidence = float(input("What is the % of the minimum confidence? ")) / 100
    dataSet = read_data(file_path, percentage)
    D = generate_combinations(dataSet)
    D = filter_combinations(D, minSupport)
    print("Frequent itemsets:", D)
    maxSize = max(len(k) for k in D)
    calculate_confidence(D, minConfidence, maxSize)
if __name__ == "__main__":
    main()