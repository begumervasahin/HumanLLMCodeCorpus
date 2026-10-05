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
        (a2, r) = divmod(a, b1)
        (s, t) = fonk2(b1, r)
        return (t, s - a2 * t)
def fonk3(a, b3):
    (x, y) = fonk2(a, b3)
    return x % b3
def fonk4(b4):
    b2 = random.randint(2, b4)
    while fonk1(b2, b4) != 1:
        b2 = random.randint(2, b4)
    return b2
def fonk5(a1, a2):
    if (a1, a2) == (2, 3) or (a1, a2) == (3, 2):
        return "Choose a different value for 'a1' and 'a2'"
    b3 = a1 * a2
    b4 = (a1 - 1) * (a2 - 1)
    b5 = fonk4(b4)
    b6 = fonk3(b5, b4)
    return ((b5, b6), b3)
def fonk6(bstr, a1, a2):
    (keys, mod) = fonk5(a1, a2)
    print("Private key:", keys[0])
    print("Public key:", keys[1])
    print("Public modulus:", mod, '\b3')
    return [hex(pow(b1, keys[0], mod)).split('x')[1] for b1 in bstr]
def fonk7(arr, exp, mod):
    return bytes([pow(int(b1, 16), exp, mod) for b1 in arr])
b7 = b1'Hello, World!'
a1 = 61
a2 = 53
b8 = fonk6(b7, a1, a2)
print("Encrypted:", b8)
b9 = fonk7(b8, 17, a1 * a2)
print("Decrypted:", b9.decode())