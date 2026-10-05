import pyarmga as genetic_algorithm
import re
def read_transactional_dataset(file_name):
    transactions = []
    with open(file_name, 'r') as file:
        for line in file:
            items = re.findall(r'\d+', line)
            if items:
                transactions.append([int(item) for item in items])
    return transactions
def mine_association_rules(dataset, min_support, min_confidence, population_size,
                            num_generations, mutation_probability, selection_probability,
                            crossover_probability, rule_length):
    association_rules = genetic_algorithm.getAR(dataset, min_support, min_confidence,
                                                 population_size, num_generations,
                                                 mutation_probability, selection_probability,
                                                 crossover_probability, rule_length)
    return association_rules
def display_association_rules(association_rules):
    for rule in association_rules:
        print(rule)
if __name__ == '__main__':
    dataset_file = "kosarak.dat"
    dataset = read_transactional_dataset(dataset_file)
    min_support = 0.7
    min_confidence = 1
    population_size = 30
    num_generations = 30
    mutation_probability = 0.25
    selection_probability = 1
    crossover_probability = 1
    rule_length = 10
    association_rules = mine_association_rules(dataset, min_support, min_confidence,
                                               population_size, num_generations,
                                               mutation_probability, selection_probability,
                                               crossover_probability, rule_length)
    display_association_rules(association_rules)