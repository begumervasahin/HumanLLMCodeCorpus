import random
def fonk1():
    return random.randint(2**127, 2**128 - 1)
def fonk2():
    return [random.randint(2**7, 2**8 - 1) for _ in range(256)]
def fonk3(b6):
    b1 = bin(b6)[2:].zfill(128)
    return [b1[i*8:(i+1)*8] for i in range(16)]
def fonk4(b8, b9):
    for i in range(16):
        b2 = b8[i]
        b3 = int(b2[:4], 2)
        b4 = int(b2[4:], 2)
        b5 = b9[(b4 + b3) % 256]
        b8[i] = format(b5, '08b')
    return b8
def fonk5():
    b6 = fonk1()
    b7 = fonk1()
    print(f"Result of XOR: {bin(b6 ^ b7)}")
    print(f"Plain text: {bin(b6)}")
    b8 = fonk3(b6)
    print("State Array:")
    print(b8)
    b9 = fonk2()
    b8 = fonk4(b8, b9)
    print("State Array after the Substitution process:")
    print(b8)
if b10 = = "__main__":
    fonk5()