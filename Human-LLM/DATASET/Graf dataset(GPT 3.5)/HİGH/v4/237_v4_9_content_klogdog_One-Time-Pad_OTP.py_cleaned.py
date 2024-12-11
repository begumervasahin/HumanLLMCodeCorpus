import random
b1 = "this is an ultra secret b1:"
b2 = []
b3 = []
b4 = []
a1 = 0
for i in range(len(b1) + 10000):
    b5 = random.randint(0, 27)
    b3.append(b5)
b6 = {" ": 0, "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10,
                      "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20,
                      "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26, ":": 27}
b7 = {0: " ", 1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j',
                      11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't',
                      21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z', 27: ':'}
for char in b1:
    b2.append(b6[char])
for j in range(len(b1)):
    b8 = b2[j] + b3[j]
    if b8 > 28:
        b8 = b8 % 28
    b4.append(b8)
for i in range(len(b1), len(b3)):
    b4.append(b3[i])
for b10 in b4:
    b9 = b10 - b3[j]
    if b9 < 0:
        b9 = b9 + 28
    j += 1
    b4.append(b9)
for b10 in b4:
    if b10 = = 27:
        a1 = 1
    if a1 = = 0:
        b9 = b7[b10]
        b4.append(b9)
b11 = "".join(b4)
print("One-time pad:")
print("Key:", b3)
print("Message to number:", b2)
print("Encrypted b1:", b4)
print("Decrypted b1:", b11)