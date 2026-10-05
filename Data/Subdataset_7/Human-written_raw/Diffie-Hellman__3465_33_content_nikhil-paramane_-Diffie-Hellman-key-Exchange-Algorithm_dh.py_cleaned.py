from random import randint
import math
def fonk1(b1, b2):
    if b1 = = 1:
        return False
    if b2 >= b1:
        b2 = b1 - 1
    for x in range(b2):
        b3 = randint(1, b1 - 1)
        if pow(b3, b1-1, b1) != 1:
            return False
    return True
def fonk2(n):
    b4 = False
    while not b4:
        b5 = randint(2**(n-1), 2**n)
        if fonk1(b5, 1000):
            return b5
b6 = fonk2(2**10)
print("prime 1: ")
print(b6)
b7 = fonk2(2**10)
print("prime 2: ")
print(b7)
b8 = randint(2**10, 2**15)
b9 = randint(2**10, 2**15)
b3 = pow(b7,b8,b6)
b10 = pow(b7,b9,b6)
b11 = pow(b10,b8,b6)
b12 = pow(b3,b9,b6)
print("Alice Secret key :")
print(b11)
print("Bob Secret key :")
print(b12)