import random
def fonk1(a, b1):
    if b1 = = 0:
        return a
    else:
        return fonk1(b1, a % b1)
def fonk2(a, b1):
    if b1 = = 0:
        return (1, 0)
    else:
        a2, b2 = divmod(a, b1)
        s, b3 = fonk2(b1, b2)
        return (b3, s - a2 * b3)
def fonk3(a, b6):
    x, b4 = fonk2(a, b6)
    return x % b6
def fonk4(b7):
    b5 = random.randint(2, b7)
    while fonk1(b5, b7) != 1:
        b5 = random.randint(2, b7)
    return b5
def fonk5(a1, a2):
    if (a1, a2) == (2, 3) or (a1, a2) == (3, 2):
        return "Choose a different value for 'a1' and 'a2'"
    b6 = a1 * a2
    b7 = (a1 - 1) * (a2 - 1)
    b8 = fonk4(b7)
    b9 = fonk3(b8, b7)
    return ((b8, b9), b6)
def fonk6(b10, a1, a2):
    (keys, mod) = fonk5(a1, a2)
    print("Private key:", keys[0])
    print("Public key:", keys[1])
    print("Public modulus:", mod, '\b6')
    return [hex(pow(b1, keys[0], mod)).split('x')[1] for b1 in b10]
def fonk7(ciphertext, exp, mod):
    return bytes([pow(int(b1, 16), exp, mod) for b1 in ciphertext])
b10 = b1'Hello, World!'
a1 = 61
a2 = 53
b11 = fonk6(b10, a1, a2)
print("Encrypted:", b11)
b12 = fonk7(b11, 17, a1 * a2)
print("Decrypted:", b12.decode())