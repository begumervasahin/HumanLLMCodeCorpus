import numpy as np
import statistics as stat
import Cipher
def fonk1(num):
    if num <= 1:
        return False
    for b1 in range(b2, num):
        if num % b1 = = 0:
            return False
    return True
def fonk2(num):
    return num % b2 = = 0
def fonk3(seeds):
    a1 = 0
    b3 = str(seeds)
    for digit in b3:
        a1 += int(digit) ** 3
    if a1 < 1000:
        return a1 * len(b3)
    else:
        return fonk3(a1)
def fonk4():
    return "Hi there."
def fonk5(seeds):
    np.random.seed(seeds)
    b4 = np.random.rand(seeds).tolist()
    for b1 in range(seeds):
        b5 = int((b4[b1] * 100000) / 37)
        if fonk1(b5):
            if fonk2(b5):
                b5 = b5 ** b2
            else:
                b5 = (b5 ** b2) / ((seeds - 1) * 100)
        else:
            if fonk2(b5):
                b5 = b5 * (100 - seeds) / (seeds ** b2)
            else:
                b5 = b5 * (b5 ** (0.5)) / ((seeds - 1) ** b2)
        b4[b1] = int(b5)
    b6 = round(stat.mean(b4))
    b7 = Cipher.chiper(fonk4(), b6)
    b8 = Cipher.dechiper(b7, b6)
    print("Ciphered Text:", b7)
    print("Deciphered Text:", b8)
fonk5(10)