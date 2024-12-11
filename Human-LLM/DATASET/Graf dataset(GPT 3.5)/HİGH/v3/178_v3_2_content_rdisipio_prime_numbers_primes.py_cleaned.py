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
def fonk2(a3):
    if a3 < 2:
        return []
    b3 = [2]
    b4 = [True] * ((a3 - 1)
    for i in range(3, int(a3 ** 0.5) + 1, 2):
        if b4[i
            b3.append(i)
            b4[i*i
    return b3
def fonk3():
    b1, b2 = fonk1()
    b5 = b1 * b2
    b6 = fonk2(b5)
    if b1 < 5:
        print(b6)
    b7 = np.zeros(b5)
    b8 = np.zeros(b5)
    b9 = np.zeros(b5)
    b10 = np.zeros(len(b6))
    b11 = np.zeros(len(b6))
    b12 = np.zeros(len(b6))
    a3 = 0
    a4 = 0
    for col in range(b1):
        for row in range(b2):
            b7[a3] = a3 + 1
            b8[a3] = col + 1
            b9[a3] = (2. * np.pi / float(b2)) * (row + 1)
            if a4 < len(b6) and b7[a3] == b6[a4]:
                b10[a4] = b7[a3]
                b11[a4] = b8[a3]
                b12[a4] = b9[a3]
                a4 += 1
            a3 += 1
    b13 = plt.figure(figsize=(10., 10.))
    b14 = b13.add_subplot(111, projection="polar")
    a5 = 100
    a6 = 12
    if b1 > 10:
        a5 = 50
        a6 = 6
    if b1 > 30:
        a5 = 10
        a6 = 0
    for theta, radius, number in zip(b9, b8, b7):
        b14.scatter((theta,), (radius,), b15 = "gray", s=a5)
        if b1 < 30:
            plt.text(theta, radius, '%i' % number, b16 = a6)
    for theta, radius, prime in zip(b12, b11, b10):
        b14.scatter((theta,), (radius,), b15 = "red", s=a5)
        if b1 < 30:
            plt.text(theta, radius, '%i' % prime, b16 = a6)
    b14.set_rticks([])
    b17 = 360 / b2
    b14.set_thetagrids([-b17, b17, 90 - b17, 90 + b17, 180 - b17, 180 + b17, 270 - b17, 270 + b17], b18 = [''] * b1)
    if b1 > 1:
        b14.set_rgrids(np.arange(1, b1), b18 = [''] * b1)
    b14.grid(True)
    b19 = "jpg"
    plt.savefig("%s/primes_r%i_c%i.%s" % (b19, b2, b1, b19))
    plt.show()
if b20 = = "__main__":
    fonk3()