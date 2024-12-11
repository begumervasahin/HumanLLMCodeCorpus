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
        (q, r) = divmod(a, b1)
        (s, t) = fonk2(b1, r)
        return (t, s - q * t)
def fonk3(a, b3):
    (x, y) = fonk2(a, b3)
    return x % b3
def fonk4(b4):
    b2 = random.randint(2, b4)
    while fonk1(b2, b4) != 1:
        b2 = random.randint(2, b4)
    return b2
def fonk5(p, q):
    if (p, q) == (2, 3) or (p, q) == (3, 2):
        return "Choose a different value for 'p' and 'q'"
    b3 = p * q
    b4 = (p - 1) * (q - 1)
    b5 = fonk4(b4)
    b6 = fonk3(b5, b4)
    return ((b5, b6), b3)
def fonk6(bstr, p, q):
    (keys, mod) = fonk5(p, q)
    print("Private key:", keys[0])
    print("Public key:", keys[1])
    print("Public modulus:", mod, '\b3')
    return [ hex(pow(b1, keys[0], mod)).split('x')[1] for b1 in bstr ]
def fonk7(arr, exp, mod):
    return bytes( [ pow(int(b1, 16), exp, mod) for b1 in arr ] )