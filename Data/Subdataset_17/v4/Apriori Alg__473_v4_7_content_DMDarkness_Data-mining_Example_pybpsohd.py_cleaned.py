
import pybpsohd as pybp
import re
def read_dataset(file_name):
    with open(file_name, 'r') as file:
        transactions = []
        content = file.readlines()
        for line in content:
            items = re.split(r' |\n', line)
            transaction = [int(item) for item in items if item.isdigit()]
            if transaction:
                transactions.append(transaction)
    return transactions
def main():
    dataset = read_dataset("kosarak.dat")
    frequent_itemsets = pybp.getFP(dataset, 0.00001, 30, 30, 0.5, 1, 1, 10)
    print("Frequent itemsets:")
    for itemset in frequent_itemsets:
        print(itemset)
if __name__ == "__main__":
    main()
