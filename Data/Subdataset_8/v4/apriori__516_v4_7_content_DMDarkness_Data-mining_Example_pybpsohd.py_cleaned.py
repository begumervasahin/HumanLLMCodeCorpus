
import pybpsohd as pybp
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
    dataset = read_dataset("kosarak.dat")
    frequent_patterns = pybp.getFP(dataset, 0.00001, 30, 30, 0.5, 1, 1, 10)
    for pattern in frequent_patterns:
        print(pattern)
