import random
def fonk1():
    return random.randint(2**127, 2**128 - 1)
def fonk2():
    return [random.randint(2**7, 2**8 - 1) for _ in range(256)]
def fonk3(b7):
    b1 = bin(b7)[2:].zfill(128)
    return [b1[i*8:(i+1)*8] for i in range(16)]
def fonk4(b9, b10):
    for i in range(16):
        b2 = b9[i]
        b3 = int(b2[:4], 2)
        b4 = int(b2[4:], 2)
        b5 = b10[(b4 + b3) % 16]
        b9[i] = format(b5, '08b')
    return b9
if b6 = = "__main__":
    b7 = fonk1()
    b8 = fonk1()
    print(f"Result of XOR: {bin(b7 ^ b8)}")
    print(f"Plain text: {bin(b7)}")
    b9 = fonk3(b7)
    print("State Array:")
    print(b9)
    b10 = fonk2()
    b9 = fonk4(b9, b10)
    print("State Array after the Substitution process:")
    print(b9)