import random
import copy
import numpy as np
import matplotlib.pyplot as plt
import Ind
def fonk1(parents):
    b1 = Ind.Ind()
    r1, b2 = random.sample(range(4), 2)
    b1.cof[r1] = parents[0].cof[r1]
    b1.cof[b2] = parents[0].cof[b2]
    b3 = [i for i in range(4) if i not in (r1, b2)]
    b1.cof[b3[0]] = parents[1].cof[b3[0]]
    b1.cof[b3[1]] = parents[1].cof[b3[1]]
    return b1
def fonk2(individual, mutation_rate, sigma):
    if random.random() <= mutation_rate:
        b4 = np.random.normal(0, sigma, 4)
        individual.cof += b4
    return individual
def fonk3(b12, mutation_rate, sigma, b9, b11):
    b5 = [
        (copy.deepcopy(random.choice(b12)), copy.deepcopy(random.choice(b12)))
        for _ in range(len(b12))
    ]
    b6 = [fonk1(pair) for pair in b5]
    b6 = [fonk2(ind, mutation_rate, sigma) for ind in b6]
    for ind in b6:
        ind.fit_ness(b9, b11)
    b7 = b12 + b6
    b7.sort(b8 = lambda ind: ind.fitness, reverse=True)
    return b7[:50]
def fonk4(file_path):
    with open(file_path, 'r') as f:
        b9 = [float(f.readline().strip()) for _ in range(100)]
    return b9
def fonk5(population_size):
    return [Ind.Ind() for _ in range(population_size)]
def fonk6(b12, b9, b11):
    for ind in b12:
        ind.fit_ness(b9, b11)
def fonk7(b11, b9, b16, b13, best_fitness, mean_fitness, worst_fitness):
    plt.plot(b11, b9, 'co', b10 = 'Data')
    plt.plot(b11, b16, '-g', b10 = 'Best Fit')
    plt.legend()
    plt.show()
    plt.plot(b13, best_fitness, 'g^', b10 = 'Best')
    plt.plot(b13, mean_fitness, 'co', b10 = 'Mean')
    plt.plot(b13, worst_fitness, 'rs', b10 = 'Worst')
    plt.legend()
    plt.show()
def fonk8(b18, population_size, tournament_size, mutation_rate, sigma):
    b9 = fonk4('input.csv')
    b11 = [round(b14 * 0.1, 1) for b14 in range(100)]
    b12 = fonk5(population_size)
    fonk6(b12, b9, b11)
    best_fitness, mean_fitness, worst_fitness, b13 = [], [], [], []
    for gen_num in range(b18):
        b12 = fonk3(b12, mutation_rate, sigma, b9, b11)
        b13.append(gen_num)
        best_fitness.append(b12[0].fitness)
        mean_fitness.append((b12[0].fitness + b12[-1].fitness) / 2)
        worst_fitness.append(b12[-1].fitness)
        print(f'Generation {gen_num + 1} - Best Fitness: {b12[0].fitness}')
    b14 = np.linspace(0, 10, 100)
    b15 = b12[0].cof
    b16 = b15[3] * b14**3 + b15[2] * b14**2 + b15[1] * b14 + b15[0]
    fonk7(b11, b9, b16, b13, best_fitness, mean_fitness, worst_fitness)
if b17 = = "__main__":
    fonk8(b18 = 5000, population_size=50, tournament_size=2, mutation_rate=0.1, sigma=0.1)