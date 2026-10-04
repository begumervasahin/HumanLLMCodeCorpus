import numpy as np
import ascent as asc
from math import ceil
from random import random as rd, randint as ri
asc.train_file = 'DB24-glass/TRAIN.TXT'
asc.test_file = 'DB24-glass/TEST.TXT'
asc.plot = False
asc.stabilzation_factor = 1e-6
pc = 1.0
pm = 0.05
generations = 100
N = 100
n_terms = 5
n_vars = 9
max_deg = 3
L = n_terms * n_vars * ceil(np.log2(max_deg))
b2m = round(L * N * pm)
def set_parameters():
    global L, b2m
    L = n_terms * n_vars * ceil(np.log2(max_deg))
    b2m = round(L * N * pm)
def generate_population():
    return np.random.choice([0, 1], size=(N, L), p=[0.5, 0.5])
def decode_individual(individual):
    var_exp = []
    bits_exp = ceil(np.log2(max_deg))
    term_len = n_vars * bits_exp
    for t in range(n_terms):
        term = []
        start = t * term_len
        term_str = individual[start:start + term_len]
        for v in range(n_vars):
            init = v * bits_exp
            dec_exp = int("".join(map(str, term_str[init:init + bits_exp])), 2)
            term.append(dec_exp)
        var_exp.append(term)
    return np.array(var_exp)
def evaluate_population(population):
    fitness = []
    for ind in population:
        terms = decode_individual(ind)
        asc.variables = terms
        asc.set()
        _, _, tst_rms = asc.run()
        fitness.append(tst_rms)
    return np.array(fitness)
def annular_crossover(population):
    for i in range(N
        if rd() <= pc:
            p = ri(1, L
            population[i, p:], population[N - i - 1, p:] = (
                population[N - i - 1, p:].copy(),
                population[i, p:].copy(),
            )
    return population
def mutate_population(population):
    for _ in range(b2m):
        p1 = ri(0, L - 1)
        p2 = ri(0, N - 1)
        population[p2, p1] ^= 1
    return population
def run_evolution():
    asc.set()
    population = generate_population()
    fitness = evaluate_population(population)
    for g in range(generations):
        population = np.tile(population[:N], (2, 1))
        fitness = np.tile(fitness[:N], 2)
        population = annular_crossover(population)
        population = mutate_population(population)
        fitness[:N] = evaluate_population(population[:N])
        sorted_indices = np.argsort(fitness)
        fitness = fitness[sorted_indices]
        population = population[sorted_indices]
        print(f"Generation {g+1}: Best fitness = {fitness[0]:.6f}, Worst fitness = {fitness[N]:.6f}")
    return decode_individual(population[0]), fitness[0]
if __name__ == "__main__":
    terms, best_fitness = run_evolution()
    asc.variables = terms
    asc.set()
    C, trn_rms, tst_rms = asc.run()
    print("Terms:")
    print(terms)
    print("Coefficients:")
    print(C)
    print("Training RMS:")
    print(trn_rms)
    print("Test RMS:")
    print(tst_rms)