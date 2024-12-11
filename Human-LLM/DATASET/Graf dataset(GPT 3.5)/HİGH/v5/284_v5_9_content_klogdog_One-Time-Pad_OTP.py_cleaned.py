import random
def fonk1(message_length):
    return [random.randint(0, 27) for _ in range(message_length)]
def fonk2(b3, b6):
    b1 = [(b4[char] + b6[i]) % 28 for i, char in enumerate(b3)]
    return b1
def fonk3(b1, b6):
    b2 = [(b1[i] - b6[i]) % 28 for i in range(len(b1))]
    return b2
def fonk4(numbers):
    return ''.join(b5[num] for num in numbers)
b3 = "this is an ultra secret b3:"
b4 = {" ": 0, "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10,
                      "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20,
                      "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26, ":": 27}
b5 = {0: " ", 1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j',
                      11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't',
                      21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z', 27: ':'}
b6 = fonk1(len(b3))
b1 = fonk2(b3, b6)
b2 = fonk3(b1, b6)
b7 = fonk4(b2)
print("One-time pad:")
print("Key:", b6)
print("Message to number:", b1)
print("Decrypted b3:", b7)