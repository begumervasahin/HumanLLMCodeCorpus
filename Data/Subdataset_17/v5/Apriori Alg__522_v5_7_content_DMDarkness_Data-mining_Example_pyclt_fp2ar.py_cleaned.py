
import pyclt
import fp2ar
import re
def read_dataset(file_name):
    transactions = []
    with open(file_name, 'r') as file:
        content = file.readlines()
        for line in content:
            items = re.split(r' |\n', line)
            transaction = [int(item) for item in items if item.isdigit()]
            if transaction:
                transactions.append(transaction)
    return transactions
def main():
    dataset = read_dataset("kosarak.dat")
    min_support = 0.03
    support_deviation_range = 0.005
    sample_probability = 0.01
    frequent_patterns, sample_size = pyclt.getFP(dataset, min_support, support_deviation_range, sample_probability)
    min_confidence = 0.75
    min_lift = 1
    association_rules = fp2ar.getAR(frequent_patterns, sample_size, min_confidence, min_lift)
    print("Frequent Patterns:")
    for pattern in frequent_patterns:
        print(pattern)
    print("\nAssociation Rules:")
    for rule in association_rules:
        print(rule)
if __name__ == "__main__":
    main()