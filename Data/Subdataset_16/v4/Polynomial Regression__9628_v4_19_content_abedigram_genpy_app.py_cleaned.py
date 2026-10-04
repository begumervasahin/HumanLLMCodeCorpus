import Ind
import random
import copy
import numpy as np
import matplotlib.pyplot as plt
def fonk1(parents):
    b1 = Ind.Ind()
    b2 = random.sample(range(4), 2)
    for i in b2:
        b1.cof[i] = parents[0].cof[i]
    b3 = [i for i in range(4) if i not in b2]
    for i in b3:
        b1.cof[i] = parents[1].cof[i]
    return b1
def fonk2(individual, mutation_rate, sigma):
    if random.random() <= mutation_rate:
        b4 = np.random.normal(0, sigma, 4)
        individual.cof += b4
    return individual
def fonk3(b11, mutation_rate, sigma, b9, b10):
    b5 = [[copy.deepcopy(b11[random.randrange(len(b11))]),
              copy.deepcopy(b11[random.randrange(len(b11))])]
             for _ in range(len(b11))]
    b6 = [fonk1(pair) for pair in b5]
    b6 = [fonk2(b1, mutation_rate, sigma) for b1 in b6]
    for individual in b6:
        individual.fit_ness(b9, b10)
    b7 = b11 + b6
    b7.sort(b8 = lambda x: x.fitness, reverse=True)
    return b7[:len(b11)]
def fonk4(b21, pop_size, mut_rate, sigma):
    with open('input.csv', 'r') as f:
        b9 = [float(line.strip()) for line in f.readlines()]
    b10 = [round(x * 0.1, 1) for x in range(100)]
    b11 = [Ind.Ind() for _ in range(pop_size)]
    for individual in b11:
        individual.fit_ness(b9, b10)
    b12 = []
    b13 = []
    b14 = []
    b15 = []
    for generation in range(b21):
        b11 = fonk3(b11, mut_rate, sigma, b9, b10)
        b15.append(generation)
        b12.append(b11[0].fitness)
        b13.append(np.mean([individual.fitness for individual in b11]))
        b14.append(b11[-1].fitness)
        print(f'{generation + 1} - {b11[0].fitness}')
    b16 = b11[0]
    b17 = np.linspace(0, 10, 100)
    b18 = sum(cof * (b17 ** idx) for idx, cof in enumerate(b16.cof[::-1]))
    plt.plot(b10, b9, 'co', b19 = 'Data')
    plt.plot(b17, b18, '-g', b19 = 'Best Fit')
    plt.legend()
    plt.show()
    plt.plot(b15, b12, 'g^', b19 = 'Best')
    plt.plot(b15, b13, 'co', b19 = 'Mean')
    plt.plot(b15, b14, 'rs', b19 = 'Worst')
    plt.legend()
    plt.show()
if b20 = = "__main__":
    fonk4(b21 = 5000, pop_size=50, mut_rate=0.1, sigma=0.1)