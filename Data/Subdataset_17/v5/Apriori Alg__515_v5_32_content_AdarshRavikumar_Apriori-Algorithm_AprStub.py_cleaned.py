
import re
from Apriori import Apriori
def load_dataset(file_path):
    alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    transactions = []
    with open(file_path, 'r') as file:
        for line in file:
            cleaned_line = re.sub(r"[?\s]", 'a', line.strip())
            items = [item for item in cleaned_line.split(',') if item in alphabet]
            transactions.append(items)
    return transactions
def main():
    min_support = int(input("Minimum support: "))
    min_confidence = float(input("Minimum confidence: "))
    min_length = int(input("Minimum length of rules: "))
    dataset_file_path = 'datasetUCI.txt'
    transactions = load_dataset(dataset_file_path)
    apriori = Apriori(transactions, min_support, min_confidence, min_length)
if __name__ == "__main__":
    main()