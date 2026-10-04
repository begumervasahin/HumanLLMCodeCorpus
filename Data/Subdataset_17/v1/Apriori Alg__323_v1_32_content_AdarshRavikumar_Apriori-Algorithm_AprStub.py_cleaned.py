
from Apriori import Apriori
import re
def get_user_inputs():
    min_support = int(input("Minimum support\n"))
    min_confidence = float(input("Minimum Confidence\n"))
    min_length = int(input("Minimum Length of rules \n"))
    return min_support, min_confidence, min_length
def load_dataset(file_path):
    alpha = [chr(i) for i in range(ord('a'), ord('z')+1)]
    transactions = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            line = re.sub(r"[?\s]", 'a', line)
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