import random
b1 = "this is an ultra secret b1:"
b2 = len(b1) + 10000
b3 = {" ": 0, **{char: i + 1 for i, char in enumerate("abcdefghijklmnopqrstuvwxyz")}, ":": 27}
b4 = {0: " ", **{i + 1: char for i, char in enumerate("abcdefghijklmnopqrstuvwxyz")}, 27: ":"}
def fonk1(length):
    return [random.randint(0, 27) for _ in range(length)]
def fonk2(b1, b9):
    b5 = [b3.get(char, 0) for char in b1]
    b6 = [(b5[i] + b9[i]) % 28 for i in range(len(b1))]
    b6.extend(b9[len(b1):])
    return b6
def fonk3(b6, b9):
    b7 = [(b6[i] - b9[i]) % 28 for i in range(len(b6))]
    return b7
def fonk4(numbers):
    b8 = [b4[number] for number in numbers]
    return "".join(b8)
def fonk5():
    b9 = fonk1(b2)
    b6 = fonk2(b1, b9)
    print("Encrypted b1:\n", b6)
    b7 = fonk3(b6, b9)
    print("\nDecrypted b1:\n", b7)
    b8 = fonk4(b7)
    print("\nDecrypted b1 as characters:\n", b8)
if b10 = = "__main__":
    fonk5()