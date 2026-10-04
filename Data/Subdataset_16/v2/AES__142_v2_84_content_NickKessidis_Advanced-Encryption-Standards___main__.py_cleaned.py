import random
def fonk1():
    return random.randrange(2**127, 2**128)
def fonk2():
    return [random.randrange(2**7, 2**8) for _ in range(256)]
def fonk3(b7):
    b1 = ["0"] * 16
    b2 = bin(b7)[2:].zfill(128)
    for i in range(16):
        b1[i] = b2[8 * i: 8 * (i + 1)]
    return b1
def fonk4(b1, b9):
    for i in range(16):
        b3 = b1[i]
        b4 = int(b3[:4], 2)
        b5 = int(b3[4:], 2)
        b1[i] = format(b9[(b5 + b4) % 16], '08b')
    return b1
if b6 = = "__main__":
    b7 = fonk1()
    b8 = fonk1()
    print("Result of XOR:", bin(b7 ^ b8))
    print("Plain text:", bin(b7))
    b1 = fonk3(b7)
    print("State Array:")
    print(b1)
    b9 = fonk2()
    b1 = fonk4(b1, b9)
    print("State Array after the Substitution process:")
    print(b1)