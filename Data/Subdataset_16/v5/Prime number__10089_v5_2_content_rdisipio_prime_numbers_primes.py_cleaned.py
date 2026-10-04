import sys
import numpy as np
import matplotlib.pyplot as plt
a1 = 24
a2 = 2
def fonk1():
    b1 = a2
    b2 = a1
    if len(sys.argv) > 1:
        b1 = int(sys.argv[1])
    if len(sys.argv) > 2:
        b2 = int(sys.argv[2])
    return b1, b2
def fonk2(b3):
    if b3 < 2:
        return []
    if b3 = = 2:
        return [2]
    b4 = list(range(3, b3 + 1, 2))
    b5 = int(b3 ** 0.5)
    b6 = (b3 + 1)
    a3 = 0
    a4 = 3
    while a4 <= b5:
        if b4[a3]:
            b7 = (a4 * a4 - 3)
            b4[b7] = 0
            while b7 < b6:
                b4[b7] = 0
                b7 += a4
        a3 += 1
        a4 = 2 * a3 + 3
    return [2] + [x for x in b4 if x]
def fonk3(b1, b2, b21, primes):
    b8 = b1 * b2
    b9 = np.zeros(b8)
    b10 = np.zeros(b8)
    b11 = np.zeros(b8)
    b12 = np.zeros(len(primes))
    b13 = np.zeros(len(primes))
    b14 = np.zeros(len(primes))
    b3 = 0
    a5 = 0
    for c in range(b1):
        for a3 in range(b2):
            b9[b3] = b3 + 1
            b10[b3] = c + 1
            b11[b3] = (2. * np.pi / b2) * (a3 + 1)
            if a5 < len(primes) and b9[b3] == primes[a5]:
                b12[a5] = b9[b3]
                b13[a5] = b10[b3]
                b14[a5] = b11[b3]
                a5 += 1
            b3 += 1
    return b9, b10, b11, b12, b13, b14
def fonk4(b1, b2, b9, b10, b11, b12, b13, b14):
    b15 = plt.figure(figsize=(10., 10.))
    b16 = b15.add_subplot(111, projection="polar")
    a6 = 100
    a7 = 12
    if b1 > 10:
        a6 = 50
        a7 = 6
    if b1 > 30:
        a6 = 10
        a7 = 0
    for x, y, b3 in zip(b11, b10, b9):
        b16.scatter((x,), (y,), b17 = "gray", b4=a6)
        if b1 < 30:
            plt.text(x, y, f'{int(b3)}', b18 = a7)
    for x, y, b3 in zip(b14, b13, b12):
        b16.scatter((x,), (y,), b17 = "red", b4=a6)
        if b1 < 30:
            plt.text(x, y, f'{int(b3)}', b18 = a7)
    b16.set_rticks([])
    b19 = 360 / b2
    b16.set_thetagrids([0, 90, 180, 270], b20 = [''] * 4)
    if b1 > 1:
        b16.set_rgrids(np.arange(1, b1 + 1), b20 = [''] * b1)
    b16.grid(True)
    plt.savefig(f"primes_r{b2}_c{b1}.jpg")
    plt.show()
def fonk5():
    b1, b2 = fonk1()
    b21 = b1 * b2
    b22 = fonk2(b21)
    if b1 < 5:
        print(b22)
    b23 = fonk3(b1, b2, b21, b22)
    fonk4(b1, b2, *b23)
if b24 = = "__main__":
    fonk5()