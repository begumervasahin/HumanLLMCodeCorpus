
import pyarmga as ga
import re
def read_transactional_dataset(file_name):
    with open(file_name, 'r') as file:
        content = file.readlines()
    transactions = []
    for line in content:
        items = re.split(r' |\n', line)
        transaction = [int(item) for item in items if item.isdigit()]
        if transaction:
            transactions.append(transaction)
    return transactions
def mine_association_rules(dataset, min_confidence, min_lift, population_size, generations, mutation_prob, selection_prob, crossover_prob, rule_length):
    return ga.getAR(dataset, min_confidence, min_lift, population_size, generations, mutation_prob, selection_prob, crossover_prob, rule_length)
def print_association_rules(association_rules):
    for rule in association_rules:
        print(rule)
def main():
    dataset_path = "kosarak.dat"
    dataset = read_transactional_dataset(dataset_path)
    min_confidence = 0.7
    min_lift = 1
    population_size = 30
    generations = 30
    mutation_prob = 0.25
    selection_prob = 1
    crossover_prob = 1
    rule_length = 10
    association_rules = mine_association_rules(
        dataset,
        min_confidence,
        min_lift,
        population_size,
        generations,
        mutation_prob,
        selection_prob,
        crossover_prob,
        rule_length
    )
    print_association_rules(association_rules)
if __name__ == "__main__":
    main()