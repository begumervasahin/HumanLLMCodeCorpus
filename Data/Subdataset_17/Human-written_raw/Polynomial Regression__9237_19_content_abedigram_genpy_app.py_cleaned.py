import Ind
import random
import copy
import numpy as np
import matplotlib.pyplot as plt
def crossover(ps):
    child = Ind.Ind()
    r1 = random.randrange(0, 4, 1)
    r2 = random.randrange(0, 4, 1)
    while r2 == r1:
        r2 = random.randrange(0, 4, 1)
    child.cof[r1] = ps[0].cof[r1]
    child.cof[r2] = ps[0].cof[r2]
    r3 = 0
    while r3 == r1 or r3 == r2:
        r3 += 1
    r4 = 0
    while r4 == r1 or r4 == r2 or r4 ==r3:
        r4 += 1
    child.cof[r3] = ps[1].cof[r3]
    child.cof[r4] = ps[1].cof[r4]
    return child
def mutation(guy, mut_rate, sigma):
    rand = random.randrange(0, 1)
    if rand <= mut_rate:
        noise = np.random.normal(0, sigma, 4)
        guy.cof[0] += noise[0]
        guy.cof[1] += noise[1]
        guy.cof[2] += noise[2]
        guy.cof[3] += noise[3]
    return guy
def gen(pop, mut_rate, sigma, ys, xs):
    fathers = []
    for i in range(len(pop)):
        f1 = copy.copy(pop[random.randrange(0, 50, 1)])
        f2 = copy.copy(pop[random.randrange(0, 50, 1)])
        pair = [f1, f2]
        fathers.append(pair)
    new_born = []
    for i in range(len(fathers)):
        new_born.append(crossover(fathers[i]))
    for i in range(len(new_born)):
        new_born[i] = mutation(new_born[i], mut_rate, sigma)
    for i in new_born:
        i.fit_ness(ys, xs)
    hunderd = []
    for i in pop:
        hunderd.append(i)
    for i in new_born:
        hunderd.append(i)
    hunderd.sort(key=lambda x: x.fitness, reverse=True)
    return hunderd[0:50]
def main(gens, pop_size, tor_size, mut_rate, sigma):
    f = open('input.csv','r')
    ys = []
    xs = []
    pop = []
    b = []
    m = []
    w = []
    cnt = []
    for i in range(100):
        ys.append(float(f.readline()[:-1]))
    x = 0.0
    for i in range(100):
        xs.append(round(x, 1))
        x += 0.1
    for i in range(pop_size):
        pop.append(Ind.Ind())
    for i in pop:
        i.fit_ness(ys, xs)
    for i in range(5000):
        pop = gen(pop, mut_rate, sigma, ys, xs)
        cnt.append(i)
        b.append(pop[0].fitness)
        m.append((pop[0].fitness+pop[49].fitness)/2)
        w.append(pop[49].fitness)
        print(f'{i+1} - {pop[0].fitness}')
    x = np.linspace(0, 10, 100)
    cof = pop[0].cof
    y = (cof[3] * x ** 3) + (cof[2] * x ** 2) + (cof[1] * x) + (cof[0])
    plt.plot(xs, ys, 'co', x, y, '-g', label = 'dude')
    plt.show()
    plt.plot(cnt, b, 'g^', cnt, m, 'co', cnt, w, 'rs')
    plt.show()
main(gens=5000, pop_size=50, tor_size=2, mut_rate=0.1, sigma=0.1)