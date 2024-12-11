import random
def fonk1(a, b1):
    while b1 != 0:
        a, b1 = b1, a % b1
    return a
def fonk2(a, b1):
    if b1 = = 0:
        return (1, 0)
    else:
        a2, b2 = divmod(a, b1)
        s, b3 = fonk2(b1, b2)
        return (b3, s - a2 * b3)
def fonk3(a, b6):
    x, b4 = fonk2(a, b6)
    return x % b6 if fonk1(a, b6) == 1 else None
def fonk4(b7):
    while True:
        b5 = random.randint(2, b7)
        if fonk1(b5, b7) == 1:
            return b5
def fonk5(a1, a2):
    if (a1, a2) == (2, 3) or (a1, a2) == (3, 2):
        return "Choose a different value for 'a1' and 'a2'"
    b6 = a1 * a2
    b7 = (a1 - 1) * (a2 - 1)
    b5 = fonk4(b7)
    b8 = fonk3(b5, b7)
    return {'public_key': (b5, b6), 'private_key': (b8, b6)}
def fonk6(b12, public_key):
    b5, b9 = public_key
    b10 = [hex(pow(byte, b5, b9)).split('x')[1] for byte in b12]
    return b10, b9
def fonk7(b10, private_key):
    b8, b9 = private_key
    b11 = bytes([pow(int(byte, 16), b8, b9) for byte in b10])
    return b11.decode()
b12 = b1'Hello, World!'
a1 = 61
a2 = 53
b13 = fonk5(a1, a2)
print("Public key:", b13['public_key'])
print("Private key:", b13['private_key'])
encrypted, b14 = fonk6(b12, b13['public_key'])
print("\nEncrypted:", encrypted)
b11 = fonk7(encrypted, b13['private_key'])
print("Decrypted:", b11)