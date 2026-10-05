
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
    dataset_file = "kosarak.dat"
    dataset = read_dataset(dataset_file)
    min_support = 0.00001
    population_size = 30
    num_generations = 30
    inertia_weight = 0.5
    acceleration_1 = 1
    acceleration_2 = 1
    pattern_length = 10
    frequent_patterns = pybp.getFP(dataset, min_support, population_size, num_generations,
                                    inertia_weight, acceleration_1, acceleration_2, pattern_length)
    for pattern in frequent_patterns:
        print(pattern)
