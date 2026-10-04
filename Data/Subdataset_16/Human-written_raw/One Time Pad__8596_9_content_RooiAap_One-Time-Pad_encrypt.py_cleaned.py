import random
from modules import algorithms
b1 = [None, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'b4', 'b8', 'z']
b2 = input("Enter plaintext data: ")
b3 = []
for i in range(len(b2)):
    b4 = random.choice(b1)
    b3.append(b4)
b5 = algorithms.alph_pos(b2)
b6 = algorithms.alph_pos(b3)
b7 = []
for p in range(len(b5)):
    b8 = (b5[p] + b6[p]) % 26
    b7.append(b8)
b9 = []
for n in range(len(b7)):
    for z in range(len(b1)):
        if b7[n] == z:
            b9.append(b1[z])
print("Your ciphertext encrypted with the b3:" + str("".join(b3)) + " is: " + str("".join(b9)))