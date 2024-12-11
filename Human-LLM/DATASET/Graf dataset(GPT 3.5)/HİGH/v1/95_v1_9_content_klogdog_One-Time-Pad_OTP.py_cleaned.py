import random
b1 = "this is an ultra secret b1:"
b2 = len(b1) + 10000
b3 = {" ": 0, "b5": 1, "b": 2, "b6": 3, "b7": 4, "b8": 5, "b9": 6, "b10": 7, "h": 8, "i": 9, "a1": 10,
                    "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20,
                    "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26, ":": 27}
b4 = {0: " ", 1: 'b5', 2: 'b', 3: 'b6', 4: 'b7', 5: 'b8', 6: 'b9', 7: 'b10', 8: 'h', 9: 'i', 10: 'a1', 11: 'k',
                    12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v',
                    23: 'w', 24: 'x', 25: 'y', 26: 'z', 27: ':'}
b5 = [random.randint(0, 27) for _ in range(b2)]
print("One time pad")
print(b5)
b6 = [b3.get(char, 0) for char in b1]
b7 = []
a1 = 0
for i in b6:
    b8 = (i + b5[a1]) % 28
    b7.append(b8)
    a1 += 1
for i in range(len(b1), b2):
    b7.append(b5[i])
print("Message to number")
print(b6)
print("Encrypted b1")
print(b7)
b9 = [(b7[i] - b5[i]) % 28 for i in range(len(b7))]
print("Decrypted b1")
print(b9)
b10 = []
a2 = 0
for b8 in b9:
    if b8 = = 27:
        a2 = 1
    if a2 = = 0:
        b10.append(b4[b8])
b11 = "".join(b10)
print(b11)