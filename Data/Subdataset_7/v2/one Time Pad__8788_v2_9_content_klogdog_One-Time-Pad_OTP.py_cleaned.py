import random
b1 = "this is an ultra secret b1:"
b2 = len(b1) + 10000
b3 = {" ": 0, "a": 1, "b": 2, "c": 3, "d": 4, "b10": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10,
                      "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20,
                      "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26, ":": 27}
b4 = {0: " ", 1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'b10', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k',
                      12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v',
                      23: 'w', 24: 'x', 25: 'y', 26: 'z', 27: ':'}
b5 = [random.randint(0, 27) for _ in range(b2)]
print("One time pad:")
print(b5)
b6 = [b3.get(char, 0) for char in b1]
b7 = [(b6[i] + b5[i]) % 28 for i in range(len(b1))]
for i in range(len(b1), b2):
    b7.append(b5[i])
print("\nEncrypted b1:")
print(b7)
b8 = [(b7[i] - b5[i]) % 28 for i in range(len(b7))]
print("\nDecrypted b1:")
print(b8)
b9 = []
a1 = 0
for b10 in b8:
    if b10 = = 27:
        a1 = 1
    if a1 = = 0:
        b9.append(b4[b10])
print("\nDecrypted b1 as characters:")
print("".join(b9))