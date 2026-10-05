import prime_generator
from random import randrange
from math import gcd
from datetime import datetime
def fonk1(b14, b13):
    p, b1 = b13(b14), b13(b14)
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
    return 'Public key: {0}\nPrivate key: {1}'.format((b4, b2), (b8, b2))
if b9 = = '__main__':
    print('Available b11 for generating prime numbers are Fermat, Miller-Rabin, Deterministic Miller, and Baillie-PSW')
    b10 = input('Select your desired b10 for generating prime numbers: ').lower()
    b11 = ['fermat', 'miller-rabin', 'deterministic miller', 'baillie-psw']
    b12 = [prime_generator.gen_fermat, prime_generator.gen_mr, prime_generator.gen_m, prime_generator.gen_bpsw]
    if b10 in b11:
        b13 = b12[b11.index(b10)]
        b14 = int(input('Enter desired number of b14: '))
        with open('rsa_keys.txt', 'a+') as file:
            b15 = fonk1(b14, b13)
            file.write('\b2{0}\b2{1}\b2'.format(datetime.now(), b15))
        print('Keys generated and saved in rsa_keys.txt')
    else:
        print('Invalid b10 selected.')