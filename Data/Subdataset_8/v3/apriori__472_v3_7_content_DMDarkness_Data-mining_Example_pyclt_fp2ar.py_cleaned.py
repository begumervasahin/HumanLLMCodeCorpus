
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
    min_support = 0.03
    deviation = 0.005
    probability = 0.01
    frequent_patterns, sample_size = pyclt.getFP(dataset, min_support, deviation, probability)
    min_confidence = 0.75
    min_lift = 1
    association_rules = fp2ar.getAR(frequent_patterns, sample_size, min_confidence, min_lift)