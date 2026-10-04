
import re
from Apriori import Apriori
def get_user_inputs():
    min_support = int(input("Minimum support: "))
    min_confidence = float(input("Minimum confidence: "))
    min_length = int(input("Minimum length of rules: "))
    return min_support, min_confidence, min_length
def load_dataset(file_path):
    alpha = set(chr(i) for i in range(ord('a'), ord('z') + 1))
    transactions = []
    with open(file_path, 'r') as file:
        for line in file:
            line = re.sub(r"[?\s]", 'a', line.strip())
            items = line.split(',')
            transaction = [item for item in items if item in alpha]
            transactions.append(transaction)
    return transactions
def main():
    min_support, min_confidence, min_length = get_user_inputs()
    file_path = 'datasetUCI.txt'
    transactions = load_dataset(file_path)
    rules = Apriori(transactions, min_support, min_confidence, min_length)
    for rule in rules:
        print(rule)
if __name__ == "__main__":
    main()