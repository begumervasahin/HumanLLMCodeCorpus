
import pyfpgrowth as pyfp
import fp2ar
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
    frequent_patterns = pyfp.getFP(dataset, 0.01)
    association_rules = fp2ar.getAR(frequent_patterns, len(dataset), 0.75, 1)