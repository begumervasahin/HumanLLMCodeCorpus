
import pyclt
import fp2ar
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
    fi, sN = pyclt.getFP(dataset, 0.03, 0.005, 0.01)
    association_rules = fp2ar.getAR(fi, sN, 0.75, 1)
    print("Frequent Patterns:")
    for pattern in fi:
        print(pattern)
    print("\nAssociation Rules:")
    for rule in association_rules:
        print(rule)
if __name__ == "__main__":
    main()