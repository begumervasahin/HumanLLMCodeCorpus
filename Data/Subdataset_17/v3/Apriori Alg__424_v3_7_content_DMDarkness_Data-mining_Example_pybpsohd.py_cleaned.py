
import pybpsohd as pybp
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
    frequent_itemsets = pybp.getFP(dataset, 0.00001, 30, 30, 0.5, 1, 1, 10)
    for itemset in frequent_itemsets:
        print(itemset)