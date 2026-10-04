import random
import copy
import numpy as np
import matplotlib.pyplot as plt
import Ind
def fonk1(ps):
    b1 = Ind.Ind()
    r1, b2 = random.sample(range(4), 2)
    b1.b14[r1] = ps[0].b14[r1]
    b1.b14[b2] = ps[0].b14[b2]
    b3 = [i for i in range(4) if i not in (r1, b2)]
    b1.b14[b3[0]] = ps[1].b14[b3[0]]
    b1.b14[b3[1]] = ps[1].b14[b3[1]]
    return b1
def fonk2(guy, mut_rate, sigma):
    if random.random() <= mut_rate:
        b4 = np.random.normal(0, sigma, 4)
        guy.b14 += b4
    return guy
def fonk3(b11, mut_rate, sigma, b9, b10):
    b5 = [(copy.deepcopy(random.choice(b11)), copy.deepcopy(random.choice(b11))) for _ in range(len(b11))]
    b6 = [fonk1(pair) for pair in b5]
    b6 = [fonk2(ind, mut_rate, sigma) for ind in b6]
    for ind in b6:
        ind.fit_ness(b9, b10)
    b7 = b11 + b6
    b7.sort(b8 = lambda ind: ind.fitness, reverse=True)
    return b7[:50]
def fonk4(b18, pop_size, tor_size, mut_rate, sigma):
    with open('input.csv', 'r') as f:
        b9 = [float(f.readline().strip()) for _ in range(100)]
    b10 = [round(b13 * 0.1, 1) for b13 in range(100)]
    b11 = [Ind.Ind() for _ in range(pop_size)]
    for ind in b11:
        ind.fit_ness(b9, b10)
    b, m, w, b12 = [], [], [], []
    for gen_num in range(b18):
        b11 = fonk3(b11, mut_rate, sigma, b9, b10)
        b12.append(gen_num)
        b.append(b11[0].fitness)
        m.append((b11[0].fitness + b11[-1].fitness) / 2)
        w.append(b11[-1].fitness)
        print(f'{gen_num + 1} - {b11[0].fitness}')
    b13 = np.linspace(0, 10, 100)
    b14 = b11[0].b14
    b15 = b14[3] * b13**3 + b14[2] * b13**2 + b14[1] * b13 + b14[0]
    plt.plot(b10, b9, 'co', b13, b15, '-g', b16 = 'Best Fit')
    plt.show()
    plt.plot(b12, b, 'g^', b16 = 'Best')
    plt.plot(b12, m, 'co', b16 = 'Mean')
    plt.plot(b12, w, 'rs', b16 = 'Worst')
    plt.legend()
    plt.show()
if b17 = = "__main__":
    fonk4(b18 = 5000, pop_size=50, tor_size=2, mut_rate=0.1, sigma=0.1)