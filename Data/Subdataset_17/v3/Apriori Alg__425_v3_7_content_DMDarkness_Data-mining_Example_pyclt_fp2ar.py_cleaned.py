
import pyclt
import fp2ar
import re
def read_dataset(file_path):
    transactions = []
    with open(file_path, 'r') as file:
        content = file.readlines()
        for line in content:
            items = re.split(r' |\n', line)
            transaction = [int(item) for item in items if item.isdigit()]
            if transaction:
                transactions.append(transaction)
    return transactions
if __name__ == "__main__":
    dataset_path = "kosarak.dat"
    dataset = read_dataset(dataset_path)
    frequent_patterns, sample_size = pyclt.getFP(dataset, 0.03, 0.005, 0.01)
    association_rules = fp2ar.getAR(frequent_patterns, sample_size, 0.75, 1)
    for rule in association_rules:
        print(rule)