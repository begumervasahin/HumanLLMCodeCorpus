
import pyarmga as ga
import re
def read_dataset(file_name):
    transactions = []
    with open(file_name, 'r') as file:
        for line in file:
            items = re.findall(r'\d+', line)
            if items:
                transactions.append([int(item) for item in items])
    return transactions
if __name__ == '__main__':
    dataset_file = "kosarak.dat"
    dataset = read_dataset(dataset_file)
    association_rules = ga.getAR(dataset, 0.7, 1, 30, 30, 0.25, 1, 1, 10)
    for rule in association_rules:
        print(rule)