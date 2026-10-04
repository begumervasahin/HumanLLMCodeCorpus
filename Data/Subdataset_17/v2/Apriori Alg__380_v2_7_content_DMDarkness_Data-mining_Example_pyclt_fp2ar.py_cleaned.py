
import pyclt
import fp2ar
import re
def read_dataset(file_path):
    transactions = []
    with open(file_path, 'r') as file:
        content = file.readlines()
        for line in content:
            sline = re.split(r' |\n', line)
            trans = [int(item) for item in sline if item.isdigit()]
            if trans:
                transactions.append(trans)
    return transactions
if __name__ == "__main__":
    dataset_path = "kosarak.dat"
    dataset = read_dataset(dataset_path)
    frequent_patterns, sample_size = pyclt.getFP(dataset, 0.03, 0.005, 0.01)
    association_rules = fp2ar.getAR(frequent_patterns, sample_size, 0.75, 1)
    for rule in association_rules:
        print(rule)