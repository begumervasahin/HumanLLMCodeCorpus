import prime_generator
from random import randrange
from math import gcd
from datetime import datetime
def fonk1(b17):
    b1 = prime_generator.gen_mr(b17)
    b2 = prime_generator.gen_mr(b17)
    b3 = b1 * b2
    b4 = (b1 - 1) * (b2 - 1)
    while True:
        b5 = randrange(3, b4, 2)
        if gcd(b5, b4) == 1:
            break
    a, b6 = b4, b5
    b9, b7 = 0, 1
    while b6 != 0:
        b8 = a
        b9, b7 = b7, b9 - b8 * b7
        a, b6 = b6, a - b8 * b6
    if b9 < 0:
        b9 = b9 + b4
    b10 = (b5, b3)
    b11 = (b9, b3)
    return 'Public key: {}\nPrivate key: {}'.format(b10, b11)
if b12 = = '__main__':
    print('Available b14 for generating prime numbers are Fermat, Miller-Rabin, Deterministic Miller, and Baillie-Psw')
    b13 = input('Select your desired b13 for generating prime numbers: ')
    b14 = ['Fermat', 'Miller-Rabin', 'Deterministic Miller', 'Baillie-Psw']
    b15 = [prime_generator.gen_fermat, prime_generator.gen_mr, prime_generator.gen_m, prime_generator.gen_bpsw]
    b16 = b15[b14.index(b13)]
    b17 = int(input('Enter the desired number of b17: '))
    with open('rsa_keys.txt', 'a+') as file:
        b18 = fonk1(b17)
        file.write('\b3{}\b3{}'.format(datetime.now(), b18))