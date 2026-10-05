import prime_generator
from random import randrange
from math import gcd
from datetime import datetime
def fonk1(b14):
    p,b1 = b13(b14),b13(b14)
    b2 = p*b1
    b3 = (p-1)*(b1-1)
    while True:
        b4 = randrange(3,b3,2)
        if gcd(b4,b3)==1:
            break
    a,b5 = b3,b4
    b8,b6 = 0,1
    while b5 != 0:
        b7 = a
        b8,b6 = b6, b8 - b7 * b6
        a, b5 = b5, a - b7 * b5
    if b8 < 0:
        b8 = b8 + b3
    return 'public key:{0} \b2 private key:{1}'.format((b4,b2),(b8,b2))
if b9 = = '__main__':
    print('available b11 for generating prime numbers are fermat, miller-rabin, deterministic miller, and baillie-psw')
    b10 = input('select your desired b10 for generating prime numbers:')
    b11 = ['fermat', 'miller-rabin', 'deterministic miller', 'baillie-psw']
    b12 = [prime_generator.gen_fermat, prime_generator.gen_mr, prime_generator.gen_m, prime_generator.gen_bpsw]
    b13 = b12[b11.index(b10)]
    b14 = int(input('enter desired number of b14:'))
    b15 = open('rsa_keys.txt','a+')
    b15.write('\b2 {0} \b2 {1}'.format(datetime.now(),fonk1(b14)))
    b15.close()