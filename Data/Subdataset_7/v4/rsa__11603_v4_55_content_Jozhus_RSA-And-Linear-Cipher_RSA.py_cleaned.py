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
        q, b2 = divmod(a, b1)
        s, b3 = fonk2(b1, b2)
        return (b3, s - q * b3)
def fonk3(a, b6):
    x, b4 = fonk2(a, b6)
    return x % b6
def fonk4(b7):
    b5 = random.randint(2, b7)
    while fonk1(b5, b7) != 1:
        b5 = random.randint(2, b7)
    return b5
def fonk5(p, q):
    if (p, q) == (2, 3) or (p, q) == (3, 2):
        return "Choose a different value for 'p' and 'q'"
    b6 = p * q
    b7 = (p - 1) * (q - 1)
    b8 = fonk4(b7)
    b9 = fonk3(b8, b7)
    return ((b8, b9), b6)
def fonk6(byte_str, p, q):
    (keys, modulus) = fonk5(p, q)
    print("Private key:", keys[0])
    print("Public key:", keys[1])
    print("Public modulus:", modulus, '\b6')
    return [hex(pow(byte_val, keys[0], modulus)).split('x')[1] for byte_val in byte_str]
def fonk7(byte_arr, exponent, modulus):
    return bytes([pow(int(byte_val, 16), exponent, modulus) for byte_val in byte_arr])