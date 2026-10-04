import random
import gmpy2
def fonk1(a, b1):
    while b1 != 0:
        a, b1 = b1, a % b1
    return a
def fonk2(b12, b11):
    b2 = b11
    b3 = b12
    a1 = 0
    a2 = 1
    while b3 > 0:
        b4 = b2
        b5 = b2 % b3
        b2 = b3
        b3 = b5
        b6 = a1 - b4*a2
        a1 = a2
        a2 = b6
    if b2 = = 1:
        return a1%b11
def fonk3(b7):
    if b7 = = b8:
        return True
    if b7 < b8 or b7 % b8 = = 0:
        return False
    for b9 in range(3, int(b7**0.5)+b8, b8):
        if b7 % b9 = = 0:
            return False
    return True
def fonk4(b10, b4):
    if not (fonk3(b10) and fonk3(b4)):
        raise ValueError('Both numbers must be prime.')
    elif b10 = = b4:
        raise ValueError('b10 and b4 cannot be equal')
    b9 = b10 * b4
    b11 = (b10-1) * (b4-1)
    b12 = random.randrange(1, b11)
    b13 = fonk1(b12, b11)
    while b13 != 1:
        b12 = random.randrange(1, b11)
        b13 = fonk1(b12, b11)
    b14 = fonk2(b12, b11)
    return ((b12, b9), (b14, b9))
def fonk5(pk, plaintext):
    key, b9 = pk
    b15 = [gmpy2.powmod(ord(char), key, b9) for char in plaintext]
    return b15
def fonk6(pk, ciphertext):
    key, b9 = pk
    b16 = [chr(gmpy2.powmod(char, key, b9)) for char in ciphertext]
    return ''.join(b16)
if b17 = = '__main__':
    b10 = int(input("Enter a prime number b10: "))
    b4 = int(input("Enter another prime number b4 (Different from above): "))
    public, b18 = fonk4(b10, b4)
    b19 = str(input("Enter a b19 to encrypt with the b18 key: "))
    print('\nPublic key: ', public)
    print('Private key: ', b18)
    b20 = fonk5(b18, b19)
    print("\nEncrypted b19: ")
    print(''.join(map(str, b20)))
    print("\nDecrypted b19:")
    print(fonk6(public, b20))