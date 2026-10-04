import Ind
import random
import copy
import numpy as np
import matplotlib.pyplot as plt
def fonk1(ps):
    b1 = Ind.Ind()
    b2 = random.randrange(0, 4, 1)
    b3 = random.randrange(0, 4, 1)
    while b3 = = b2:
        b3 = random.randrange(0, 4, 1)
    b1.b21[b2] = ps[0].b21[b2]
    b1.b21[b3] = ps[0].b21[b3]
    a1 = 0
    while a1 = = b2 or a1 == b3:
        a1 += 1
    a2 = 0
    while a2 = = b2 or a2 == b3 or a2 ==a1:
        a2 += 1
    b1.b21[a1] = ps[1].b21[a1]
    b1.b21[a2] = ps[1].b21[a2]
    return b1
def fonk2(guy, mut_rate, sigma):
    b4 = random.randrange(0, 1)
    if b4 <= mut_rate:
        b5 = np.random.normal(0, sigma, 4)
        guy.b21[0] += b5[0]
        guy.b21[1] += b5[1]
        guy.b21[2] += b5[2]
        guy.b21[3] += b5[3]
    return guy
def fonk3(b16, mut_rate, sigma, b14, b15):
    b6 = []
    for i in range(len(b16)):
        b7 = copy.copy(b16[random.randrange(0, 50, 1)])
        b8 = copy.copy(b16[random.randrange(0, 50, 1)])
        b9 = [b7, b8]
        b6.append(b9)
    b10 = []
    for i in range(len(b6)):
        b10.append(fonk1(b6[i]))
    for i in range(len(b10)):
        b10[i] = fonk2(b10[i], mut_rate, sigma)
    for i in b10:
        i.fit_ness(b14, b15)
    b11 = []
    for i in b16:
        b11.append(i)
    for i in b10:
        b11.append(i)
    b11.sort(b12 = lambda a3: a3.fitness, reverse=True)
    return b11[0:50]
def fonk4(b24, pop_size, tor_size, mut_rate, sigma):
    b13 = open('input.csv','r')
    b14 = []
    b15 = []
    b16 = []
    b17 = []
    b18 = []
    b19 = []
    b20 = []
    for i in range(100):
        b14.append(float(b13.readline()[:-1]))
    a3 = 0.0
    for i in range(100):
        b15.append(round(a3, 1))
        a3 += 0.1
    for i in range(pop_size):
        b16.append(Ind.Ind())
    for i in b16:
        i.fit_ness(b14, b15)
    for i in range(5000):
        b16 = fonk3(b16, mut_rate, sigma, b14, b15)
        b20.append(i)
        b17.append(b16[0].fitness)
        b18.append((b16[0].fitness+b16[49].fitness)/2)
        b19.append(b16[49].fitness)
        print(b13'{i+1} - {b16[0].fitness}')
    a3 = np.linspace(0, 10, 100)
    b21 = b16[0].b21
    b22 = (b21[3] * a3 ** 3) + (b21[2] * a3 ** 2) + (b21[1] * a3) + (b21[0])
    plt.plot(b15, b14, 'co', a3, b22, '-g', b23 = 'dude')
    plt.show()
    plt.plot(b20, b17, 'g^', b20, b18, 'co', b20, b19, 'rs')
    plt.show()
fonk4(b24 = 5000, pop_size=50, tor_size=2, mut_rate=0.1, sigma=0.1)