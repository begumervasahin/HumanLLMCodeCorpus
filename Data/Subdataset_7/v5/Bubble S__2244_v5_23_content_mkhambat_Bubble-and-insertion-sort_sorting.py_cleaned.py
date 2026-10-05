import random
import pickle
import time
import matplotlib.pyplot as plt
def fonk1(b9):
    b1 = len(b9)
    for b3 in range(b1):
        for j in range(b1 - 1):
            if b9[j] > b9[j + 1]:
                b9[j], b9[j + 1] = b9[j + 1], b9[j]
def fonk2(b9):
    b1 = len(b9)
    for j in range(1, b1):
        b2 = b9[j]
        b3 = j - 1
        while b3 >= 0 and b9[b3] > b2:
            b9[b3 + 1] = b9[b3]
            b3 -= 1
        b9[b3 + 1] = b2
def fonk3():
    b4 = []
    b5 = []
    b6 = []
    b7 = []
    b8 = []
    b9 = random.sample(range(1, 300000), 200000)
    with open("data.txt", 'wb') as fp:
        pickle.dump(b9, fp)
    with open("data.txt", 'rb') as fp:
        b9 = pickle.load(fp)
    a1 = 2000
    for _ in range(25):
        b4.clear()
        b5.clear()
        a2 = 0.0
        a3 = 0.0
        for _ in range(10):
            b10 = random.sample(b9, a1)
            b11 = random.sample(b9, a1)
            b12 = time.time()
            fonk1(b10)
            b13 = time.time()
            b14 = b13 - b12
            b4.append(b14)
            a2 += b14
            b15 = time.time()
            fonk2(b11)
            b16 = time.time()
            b17 = b16 - b15
            b5.append(b17)
            a3 += b17
        b6.append(a2 / 10)
        b7.append(a3 / 10)
        a1 += 2000
    for b3 in range(1, 26):
        b8.append(2000 * b3)
    plt.plot(b8, b6, 'r--', b8, b7, 'b--')
    plt.show()
fonk3()