
import pyclt
import fp2ar
import re
def read_transactional_dataset(file_name):
    transactions = []
    with open(file_name, 'r') as file:
        for line in file:
            items = re.findall(r'\d+', line)
            if items:
                transactions.append([int(item) for item in items])
    return transactions
if __name__ == '__main__':
    dataset_file = "kosarak.dat"
    dataset = read_transactional_dataset(dataset_file)
    fi, sN = pyclt.getFP(dataset, 0.03, 0.005, 0.01)
    association_rules = fp2ar.getAR(fi, sN, 0.75, 1)