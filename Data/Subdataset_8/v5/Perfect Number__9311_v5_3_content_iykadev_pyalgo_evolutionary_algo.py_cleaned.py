from string import ascii_letters
from random import choice, random
TARGET = list("METHINKS IT IS LIKE A WEASEL")
CHARSET = ascii_letters + ' '
MIN_MUTATE_RATE = 0.09
POPULATION_SIZE = range(100)
PERFECT_FITNESS = float(len(TARGET))
def calculate_fitness(trial):
    'Calculate fitness by sum of matching characters by position'
    return sum(trial_char == target_char for trial_char, target_char in zip(trial, TARGET))
def calculate_mutate_rate(parent_fitness):
    'Calculate mutation rate based on parent fitness'
    return 1 - ((PERFECT_FITNESS - parent_fitness) / PERFECT_FITNESS * (1 - MIN_MUTATE_RATE))
def mutate(parent, rate):
    'Mutate the parent string based on the mutation rate'
    return [(ch if random() <= rate else choice(CHARSET)) for ch in parent]
def display_progress(iterations, parent_fitness, parent):
    'Print current progress'
    print("(iterations: {}, fitness: {:.2f}%, parent: '{}')".format(iterations, parent_fitness * 100. / PERFECT_FITNESS, ''.join(parent)))
def mate_parents(parent1, parent2):
    'Mate two parents to produce offspring'
    if choice(range(10)) < 7:
        crossover_point = choice(range(len(TARGET)))
    else:
        return parent1, parent2
    offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
    offspring2 = parent2[:crossover_point] + parent1[crossover_point:]
    return parent1, parent2, offspring1, offspring2
iterations = 0
population_center = len(POPULATION_SIZE)
current_parent = [choice(CHARSET) for _ in range(len(TARGET))]
while current_parent != TARGET:
    mutation_rate = calculate_mutate_rate(calculate_fitness(current_parent))
    iterations += 1
    if iterations % 100 == 0:
        display_progress(iterations, calculate_fitness(current_parent), current_parent)
    population = [mutate(current_parent, mutation_rate) for _ in POPULATION_SIZE] + [current_parent]
    parent1 = max(population[:population_center], key=calculate_fitness)
    parent2 = max(population[population_center:], key=calculate_fitness)
    current_parent = max(mate_parents(parent1, parent2), key=calculate_fitness)
display_progress(iterations, calculate_fitness(current_parent), current_parent)