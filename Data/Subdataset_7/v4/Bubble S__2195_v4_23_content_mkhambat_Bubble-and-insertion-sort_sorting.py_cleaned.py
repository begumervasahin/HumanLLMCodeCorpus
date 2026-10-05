import random
import pickle
import time
import matplotlib.pyplot as plt
def fonk1(b10):
    b1 = len(b10)
    for b4 in range(b1):
        for j in range(b1 - 1):
            if b10[j] > b10[j + 1]:
                b2 = b10[j]
                b10[j] = b10[j + 1]
                b10[j + 1] = b2
def fonk2(b10):
    b1 = len(b10)
    for j in range(1, b1):
        b3 = b10[j]
        b4 = j - 1
        while b4 >= 0 and b10[b4] > b3:
            b10[b4 + 1] = b10[b4]
            b4 -= 1
        b10[b4 + 1] = b3
def fonk3():
    b5 = []
    b6 = []
    b7 = []
    b8 = []
    b9 = []
    b10 = random.sample(range(1, 300000), 200000)
    with open("data.txt", 'wb') as fp:
        pickle.dump(b10, fp)
    with open("data.txt", 'rb') as fp:
        b10 = pickle.load(fp)
    a1 = 2000
    for _ in range(25):
        b5.clear()
        b6.clear()
        a2 = 0.0
        a3 = 0.0
        for _ in range(10):
            b11 = random.sample(b10, a1)
            b12 = random.sample(b10, a1)
            b13 = time.time()
            fonk1(b11)
            b14 = time.time()
            b15 = b14 - b13
            b5.append(b15)
            a2 += b15
            b16 = time.time()
            fonk2(b12)
            b17 = time.time()
            b18 = b17 - b16
            b6.append(b18)
            a3 += b18
        b7.append(a2 / 10)
        b8.append(a3 / 10)
        a1 += 2000
    for b4 in range(1, 26):
        b9.append(2000 * b4)
    plt.plot(b9, b7, 'r--', b9, b8, 'b--')
    plt.show()
fonk3()