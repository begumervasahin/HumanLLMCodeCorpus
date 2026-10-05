import pyarmga as ga
import re
def read_transactions(file_name):
    transactions = []
    with open(file_name, 'r') as file:
        for line in file:
            items = re.findall(r'\d+', line)
            if items:
                transactions.append([int(item) for item in items])
    return transactions
if __name__ == '__main__':
    dataset_file = "kosarak.dat"
    min_support = 0.7
    min_confidence = 1
    population_size = 30
    num_generations = 30
    mutation_probability = 0.25
    selection_probability = 1
    crossover_probability = 1
    rule_length = 10
    dataset = read_transactions(dataset_file)
    association_rules = ga.getAR(dataset, min_support, min_confidence, population_size,
                                  num_generations, mutation_probability, selection_probability,
                                  crossover_probability, rule_length)
    for rule in association_rules:
        print(rule)