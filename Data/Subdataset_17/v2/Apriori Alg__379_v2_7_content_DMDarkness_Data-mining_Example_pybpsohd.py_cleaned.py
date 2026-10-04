
import pybpsohd as pybp
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
    frequent_itemsets = pybp.getFP(dataset, 0.00001, 30, 30, 0.5, 1, 1, 10)
    for itemset in frequent_itemsets:
        print(itemset)