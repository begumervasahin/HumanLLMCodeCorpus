import prime_generator
from random import randrange
from math import gcd
from datetime import datetime
def fonk1(b16, b15):
    b1 = b15(b16)
    b2 = b15(b16)
    b3 = b1 * b2
    b4 = (b1 - 1) * (b2 - 1)
    while True:
        b5 = randrange(3, b4, 2)
        if gcd(b5, b4) == 1:
            break
    a, b6 = b4, b5
    t, b7 = 0, 1
    while b6 != 0:
        b8 = a
        t, b7 = b7, t - b8 * b7
        a, b6 = b6, a - b8 * b6
    if t < 0:
        t += b4
    b9 = (b5, b3)
    b10 = (t, b3)
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
            file.write('\b3{}\b3{}\b3'.format(datetime.now(), b17))
        print('Keys generated and saved in rsa_keys.txt')
    else:
        print('Invalid method selected.')