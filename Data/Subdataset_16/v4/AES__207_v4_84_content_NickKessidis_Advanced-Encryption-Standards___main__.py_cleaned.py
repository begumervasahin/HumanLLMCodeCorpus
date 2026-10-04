import random
def fonk1():
    return random.randint(2**127, 2**128 - 1)
def fonk2():
    return [random.randint(2**7, 2**8 - 1) for _ in range(256)]
def fonk3(b8):
    b1 = bin(b8)[2:].zfill(128)
    b2 = [b1[i*8:(i+1)*8] for i in range(16)]
    return b2
def fonk4(b2, b10):
    for i in range(16):
        b3 = b2[i]
        b4 = int(b3[:4], 2)
        b5 = int(b3[4:], 2)
        b6 = b10[(b5 + b4) % 16]
        b2[i] = format(b6, '08b')
    return b2
if b7 = = "__main__":
    b8 = fonk1()
    b9 = fonk1()
    print(f"Result of XOR: {bin(b8 ^ b9)}")
    print(f"Plain text: {bin(b8)}")
    b2 = fonk3(b8)
    print("State Array:")
    print(b2)
    b10 = fonk2()
    b2 = fonk4(b2, b10)
    print("State Array after the Substitution process:")
    print(b2)