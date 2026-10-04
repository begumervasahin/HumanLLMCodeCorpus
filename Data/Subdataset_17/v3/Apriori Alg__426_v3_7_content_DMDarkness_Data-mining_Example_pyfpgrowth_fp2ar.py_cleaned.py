
import pyfpgrowth as pyfp
import fp2ar
import re
def read_transactional_dataset(file_name):
    with open(file_name, 'r') as file:
        content = file.readlines()
    transactions = []
    for line in content:
        items = re.split(r' |\n', line)
        transaction = [int(item) for item in items if item.isdigit()]
        if transaction:
            transactions.append(transaction)
    return transactions
def mine_frequent_patterns(dataset, min_support):
    return pyfp.getFP(dataset, min_support)
def generate_association_rules(frequent_patterns, dataset_size, min_confidence, min_lift):
    return fp2ar.getAR(frequent_patterns, dataset_size, min_confidence, min_lift)
def print_frequent_patterns(frequent_patterns):
    print("Frequent Patterns:")
    for pattern, support in frequent_patterns.items():
        print(f"Pattern: {pattern}, Support: {support}")
def print_association_rules(association_rules):
    print("\nAssociation Rules:")
    for rule, metrics in association_rules.items():
        print(f"Rule: {rule}, Confidence: {metrics['confidence']}, Lift: {metrics['lift']}")
def main():
    dataset_path = "kosarak.dat"
    dataset = read_transactional_dataset(dataset_path)
    min_support = 0.01
    min_confidence = 0.75
    min_lift = 1
    frequent_patterns = mine_frequent_patterns(dataset, min_support)
    association_rules = generate_association_rules(frequent_patterns, len(dataset), min_confidence, min_lift)
    print_frequent_patterns(frequent_patterns)
    print_association_rules(association_rules)
if __name__ == "__main__":
    main()