import Ind
import random
import copy
import numpy as np
import matplotlib.pyplot as plt
def fonk1(b6):
    b1 = Ind.Ind()
    b2 = random.sample(range(4), 2)
    for i in b2:
        b1.cof[i] = b6[0].cof[i]
    b3 = [i for i in range(4) if i not in b2]
    for i in b3:
        b1.cof[i] = b6[1].cof[i]
    return b1
def fonk2(individual, mutation_rate, sigma):
    if random.random() <= mutation_rate:
        b4 = np.random.normal(0, sigma, 4)
        individual.cof += b4
    return individual
def fonk3(b12, mutation_rate, sigma, b10, b11):
    b5 = []
    for _ in range(len(b12)):
        b6 = [copy.deepcopy(b12[random.randrange(len(b12))]),
                   copy.deepcopy(b12[random.randrange(len(b12))])]
        b1 = fonk1(b6)
        b7 = fonk2(b1, mutation_rate, sigma)
        b7.fit_ness(b10, b11)
        b5.append(b7)
    b8 = b12 + b5
    b8.sort(b9 = lambda x: x.fitness, reverse=True)
    return b8[:len(b12)]
def fonk4(filename):
    with open(filename, 'r') as f:
        b10 = [float(line.strip()) for line in f]
    b11 = [round(x * 0.1, 1) for x in range(100)]
    return b10, b11
def fonk5(b18, pop_size, mut_rate, sigma):
    b10, b11 = fonk4('input.csv')
    b12 = [Ind.Ind() for _ in range(pop_size)]
    for individual in b12:
        individual.fit_ness(b10, b11)
    best_fitness, mean_fitness, worst_fitness, b13 = [], [], [], []
    for generation in range(b18):
        b12 = fonk3(b12, mut_rate, sigma, b10, b11)
        b13.append(generation)
        best_fitness.append(b12[0].fitness)
        mean_fitness.append(np.mean([ind.fitness for ind in b12]))
        worst_fitness.append(b12[-1].fitness)
        print(f'Generation {generation + 1} - Best Fitness: {b12[0].fitness}')
    fonk6(b11, b10, b12[0], b13, best_fitness, mean_fitness, worst_fitness)
def fonk6(b11, b10, best_individual, b13, best_fitness, mean_fitness, worst_fitness):
    b14 = np.linspace(0, 10, 100)
    b15 = sum(cof * (b14 ** idx) for idx, cof in enumerate(best_individual.cof[::-1]))
    plt.plot(b11, b10, 'co', b16 = 'Data')
    plt.plot(b14, b15, '-g', b16 = 'Best Fit')
    plt.legend()
    plt.show()
    plt.plot(b13, best_fitness, 'g^', b16 = 'Best')
    plt.plot(b13, mean_fitness, 'co', b16 = 'Mean')
    plt.plot(b13, worst_fitness, 'rs', b16 = 'Worst')
    plt.legend()
    plt.show()
if b17 = = "__main__":
    fonk5(b18 = 5000, pop_size=50, mut_rate=0.1, sigma=0.1)