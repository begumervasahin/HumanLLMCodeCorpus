import random
def fonk1(num):
    if num <= 1:
        return False
    for b1 in range(2, int(num**0.5) + 1):
        if num % b1 = = 0:
            return False
    return True
def fonk2(b3, b2):
    while b2:
        b3, b2 = b2, b3 % b2
    return b3
def fonk3(b3, b2):
    if b3 = = 0:
        return b2, 0, 1
    else:
        g, b5, b4 = fonk3(b2 % b3, b3)
        return g, b4 - (b2
def fonk4(b9, b8):
    g, b4, b5 = fonk3(b9, b8)
    if g != 1:
        raise Exception('Modular inverse does not exist.')
    return b4 % b8
def fonk5(b6, b12):
    if b6 = = b12:
        raise Exception(f'{b6} == {b12}')
    if not fonk1(b6) or not fonk1(b12):
        raise Exception(f'{b6} or {b12} is not prime')
    b7 = b6 * b12
    b8 = (b6 - 1) * (b12 - 1)
    b9 = random.randrange(1, b8)
    while fonk2(b9, b8) != 1:
        b9 = random.randrange(1, b8)
    b10 = fonk4(b9, b8)
    return (b9, b7), (b10, b7)
def fonk6(public_key, plaintext):
    b14, b7 = public_key
    return [(ord(char) ** b14) % b7 for char in plaintext]
def fonk7(b13, ciphertext):
    b14, b7 = b13
    return ''.join([chr((char ** b14) % b7) for char in ciphertext])
if b11 = = '__main__':
    b6 = int(input('Input b3 prime number: '))
    b12 = int(input('Input another different prime number: '))
    public_key, b13 = fonk5(b6, b12)
    print(f'Public b14 = {public_key}')
    print(f'Private b14 = {b13}')
    b15 = input('Input b3 b15: ')
    b16 = fonk6(b13, b15)
    print(f'Encrypted b15 = {"".join(map(str, b16))}')
    b17 = fonk7(public_key, b16)
    print(f'Decrypted b15 = {b17}')