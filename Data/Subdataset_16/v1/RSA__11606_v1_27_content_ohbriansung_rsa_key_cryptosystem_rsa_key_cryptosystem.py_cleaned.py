import random
def fonk1(num):
    if num > 1:
        for b1 in range(2, int(num**0.5) + 1):
            if num % b1 = = 0:
                return False
        return True
    return False
def fonk2(b3, b2):
    while b2 != 0:
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
    else:
        return b4 % b8
def fonk5(b6, q):
    if b6 = = q:
        raise Exception(f'{b6} == {q}')
    elif not fonk1(b6) or not fonk1(q):
        raise Exception(f'{b6} or {q} is not prime')
    b7 = b6 * q
    b8 = (b6 - 1) * (q - 1)
    b9 = random.randrange(1, b8)
    b10 = fonk2(b9, b8)
    while b10 != 1:
        b9 = random.randrange(1, b8)
        b10 = fonk2(b9, b8)
    b11 = fonk4(b9, b8)
    return (b9, b7), (b11, b7)
def fonk6(pk, plaintext):
    b18, b7 = pk
    b12 = [(ord(char) ** b18) % b7 for char in plaintext]
    return b12
def fonk7(pk, b12):
    b18, b7 = pk
    b13 = [chr((char ** b18) % b7) for char in b12]
    return ''.join(b13)
if b14 = = '__main__':
    b15 = int(input('Input b3 prime number: '))
    b16 = int(input('Input another different prime number: '))
    public, b17 = fonk5(b6=b15, q=b16)
    print(f'Public b18 = {public}')
    print(f'Private b18 = {b17}')
    b19 = input('Input b3 b21: ')
    b20 = fonk6(b17, b19)
    print(f'Encrypted b21 = {" ".join([str(msg) for msg in b20])}')
    b22 = fonk7(public, b20)
    print(f'Decrypted b21 = {b22}')