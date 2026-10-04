import random
def fonk1(num):
    if num <= 1:
        return False
    for b1 in range(2, int(num**0.5) + 1):
        if num % b1 = = 0:
            return False
    return True
def fonk2(b3, b2):
    while b2 != 0:
        b3, b2 = b2, b3 % b2
    return b3
def fonk3(b3, b2):
    if b3 = = 0:
        return b2, 0, 1
    g, b5, b4 = fonk3(b2 % b3, b3)
    return g, b4 - (b2
def fonk4(b9, b8):
    g, b4, b5 = fonk3(b9, b8)
    if g != 1:
        raise Exception('Modular inverse does not exist.')
    return b4 % b8
def fonk5(b6, q):
    if b6 = = q:
        raise ValueError('The two prime numbers must be different.')
    if not fonk1(b6) or not fonk1(q):
        raise ValueError('Both numbers must be prime.')
    b7 = b6 * q
    b8 = (b6 - 1) * (q - 1)
    b9 = random.randrange(1, b8)
    while fonk2(b9, b8) != 1:
        b9 = random.randrange(1, b8)
    b10 = fonk4(b9, b8)
    return (b9, b7), (b10, b7)
def fonk6(pk, plaintext):
    b15, b7 = pk
    return [(ord(char) ** b15) % b7 for char in plaintext]
def fonk7(pk, cipher):
    b15, b7 = pk
    return ''.join([chr((char ** b15) % b7) for char in cipher])
if b11 = = '__main__':
    try:
        b12 = int(input('Input b3 prime number: '))
        b13 = int(input('Input another different prime number: '))
        public_key, b14 = fonk5(b12, b13)
        print(f'Public b15 = {public_key}')
        print(f'Private b15 = {b14}')
        b16 = input('Input b3 b16: ')
        b17 = fonk6(b14, b16)
        b18 = ' '.join(map(str, b17))
        print(f'Encrypted b16 = {b18}')
        b19 = fonk7(public_key, b17)
        print(f'Decrypted b16 = {b19}')
    except Exception as b9:
        print(f'Error: {b9}')