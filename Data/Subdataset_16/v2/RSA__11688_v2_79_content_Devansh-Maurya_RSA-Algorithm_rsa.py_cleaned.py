import random
import gmpy2
def fonk1(a, b1):
    while b1 != 0:
        a, b1 = b1, a % b1
    return a
def fonk2(b11, b10):
    b5, b2 = b10, b11
    t1, b3 = 0, 1
    while b2 > 0:
        b4 = b5
        b5, b2 = b2, b5 % b2
        t1, b3 = b3, t1 - b4 * b3
    if b5 = = 1:
        return t1 % b10
def fonk3(b6):
    if b6 = = b7:
        return True
    if b6 < b7 or b6 % b7 = = 0:
        return False
    for b8 in range(3, int(b6 ** 0.5) + b7, b7):
        if b6 % b8 = = 0:
            return False
    return True
def fonk4(b9, b4):
    if not (fonk3(b9) and fonk3(b4)):
        raise ValueError('Both numbers must be prime.')
    if b9 = = b4:
        raise ValueError('b9 and b4 cannot be equal')
    b8 = b9 * b4
    b10 = (b9 - 1) * (b4 - 1)
    b11 = random.randrange(1, b10)
    while fonk1(b11, b10) != 1:
        b11 = random.randrange(1, b10)
    b12 = fonk2(b11, b10)
    return ((b11, b8), (b12, b8))
def fonk5(pk, plaintext):
    key, b8 = pk
    b13 = [gmpy2.powmod(ord(char), key, b8) for char in plaintext]
    return b13
def fonk6(pk, ciphertext):
    key, b8 = pk
    b14 = [chr(gmpy2.powmod(char, key, b8)) for char in ciphertext]
    return ''.join(b14)
if b15 = = '__main__':
    b9 = int(input("Enter a prime number b9: "))
    b4 = int(input("Enter another prime number b4 (different from above): "))
    public, b16 = fonk4(b9, b4)
    b17 = input("Enter a b17 to encrypt with the b16 key: ")
    print('\nPublic key:', public)
    print('Private key:', b16)
    b18 = fonk5(b16, b17)
    print("\nEncrypted b17:")
    print(''.join(map(str, b18)))
    b19 = fonk6(public, b18)
    print("\nDecrypted b17:")
    print(b19)