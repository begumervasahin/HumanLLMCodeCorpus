import prime_generator
from random import randrange
from math import gcd
from datetime import datetime
def fonk1(b16, b15):
    p, b1 = b15(b16), b15(b16)
    b2 = p * b1
    b3 = (p - 1) * (b1 - 1)
    while True:
        b4 = randrange(3, b3, 2)
        if gcd(b4, b3) == 1:
            break
    a, b5 = b3, b4
    b8, b6 = 0, 1
    while b5 != 0:
        b7 = a
        b8, b6 = b6, b8 - b7 * b6
        a, b5 = b5, a - b7 * b5
    if b8 < 0:
        b8 = b8 + b3
    b9 = (b4, b2)
    b10 = (b8, b2)
    return 'Public key: {}\nPrivate key: {}'.format(b9, b10)
if b11 = = '__main__':
    print('Available methods for generating prime numbers are Fermat, Miller-Rabin, Deterministic Miller, and Baillie-PSW')
    b12 = input('Select your desired method for generating prime numbers: ').lower()
    b13 = ['fermat', 'miller-rabin', 'deterministic miller', 'baillie-psw']
    b14 = [prime_generator.gen_fermat, prime_generator.gen_mr, prime_generator.gen_m, prime_generator.gen_bpsw]
    if b12 in b13:
        b15 = b14[b13.index(b12)]
        b16 = int(input('Enter the desired number of b16: '))
        with open('rsa_keys.txt', 'a+') as file:
            b17 = fonk1(b16, b15)
            file.write('\b2{}\b2{}\b2'.format(datetime.now(), b17))
        print('Keys generated and saved in rsa_keys.txt')
    else:
        print('Invalid method selected.')