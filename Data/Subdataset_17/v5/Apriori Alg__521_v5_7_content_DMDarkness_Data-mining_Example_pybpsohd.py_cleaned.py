
import pybpsohd as pybp
import re
def read_dataset(file_name):
    transactions = []
    with open(file_name, 'r') as file:
        content = file.readlines()
        for line in content:
            items = re.split(r' |\n', line)
            transaction = [int(item) for item in items if item.isdigit()]
            if transaction:
                transactions.append(transaction)
    return transactions
def main():
    dataset = read_dataset("kosarak.dat")
    min_support = 0.00001
    population_size = 30
    num_generations = 30
    inertia_weight = 0.5
    accel_coeff1 = 1
    accel_coeff2 = 1
    min_pattern_length = 10
    frequent_itemsets = pybp.getFP(
        dataset, min_support, population_size, num_generations,
        inertia_weight, accel_coeff1, accel_coeff2, min_pattern_length
    )
    print("Frequent itemsets:")
    for itemset in frequent_itemsets:
        print(itemset)
if __name__ == "__main__":
    main()
