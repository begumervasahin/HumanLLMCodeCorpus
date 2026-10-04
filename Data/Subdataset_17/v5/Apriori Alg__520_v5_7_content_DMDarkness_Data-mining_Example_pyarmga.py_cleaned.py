
import pyarmga as ga
import re
def read_transaction_file(filename):
    transactions = []
    with open(filename) as file:
        content = file.readlines()
        for line in content:
            items = re.split(r'\s+', line.strip())
            transaction = [int(item) for item in items if item.isdigit()]
            if transaction:
                transactions.append(transaction)
    return transactions
dataset = read_transaction_file("kosarak.dat")
min_confidence = 0.75
min_lift = 1
population_size = 30
num_generations = 30
mutation_prob = 0.25
selection_prob = 1
crossover_prob = 1
rule_length = 10
association_rules = ga.getAR(
    dataset,
    min_confidence,
    min_lift,
    population_size,
    num_generations,
    mutation_prob,
    selection_prob,
    crossover_prob,
    rule_length
)
