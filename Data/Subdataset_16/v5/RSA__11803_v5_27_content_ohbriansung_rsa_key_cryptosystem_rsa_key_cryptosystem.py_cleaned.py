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
def fonk5(b6, b11):
    if b6 = = b11:
        raise Exception('b6 and b11 cannot be the same')
    if not fonk1(b6) or not fonk1(b11):
        raise Exception('Both b6 and b11 must be prime numbers')
    b7 = b6 * b11
    b8 = (b6 - 1) * (b11 - 1)
    b9 = random.randrange(1, b8)
    while fonk2(b9, b8) != 1:
        b9 = random.randrange(1, b8)
    b10 = fonk4(b9, b8)
    return (b9, b7), (b10, b7)
def fonk6(public_key, plaintext):
    b13, b7 = public_key
    return [(ord(char) ** b13) % b7 for char in plaintext]
def fonk7(b12, ciphertext):
    b13, b7 = b12
    return ''.join([chr((char ** b13) % b7) for char in ciphertext])
def fonk8():
    b6 = int(input('Input b3 prime number: '))
    b11 = int(input('Input another different prime number: '))
    public_key, b12 = fonk5(b6, b11)
    print(f'Public b13 = {public_key}')
    print(f'Private b13 = {b12}')
    b14 = input('Input b3 b14: ')
    b15 = fonk6(b12, b14)
    print(f'Encrypted b14 = {"".join(map(str, b15))}')
    b16 = fonk7(public_key, b15)
    print(f'Decrypted b14 = {b16}')
if b17 = = '__main__':
    fonk8()