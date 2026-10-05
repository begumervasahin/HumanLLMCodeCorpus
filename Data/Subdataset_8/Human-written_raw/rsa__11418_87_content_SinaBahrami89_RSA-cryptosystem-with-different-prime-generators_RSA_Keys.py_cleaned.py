import prime_generator
from random import randrange
from math import gcd
from datetime import datetime
def Keys(bits):
    p,q=generator(bits),generator(bits)
    n=p*q
    phi=(p-1)*(q-1)
    while True:
        e=randrange(3,phi,2)
        if gcd(e,phi)==1:
            break
    a,b=phi,e
    t,t1= 0,1
    while b != 0:
        d = a
        t,t1 = t1, t - d * t1
        a, b = b, a - d * b
    if t < 0:
        t = t + phi
    return 'public key:{0} \n private key:{1}'.format((e,n),(t,n))
if __name__ == '__main__':
    print('available methods for generating prime numbers are fermat, miller-rabin, deterministic miller, and baillie-psw')
    method=input('select your desired method for generating prime numbers:')
    methods=['fermat', 'miller-rabin', 'deterministic miller', 'baillie-psw']
    functions=[prime_generator.gen_fermat, prime_generator.gen_mr, prime_generator.gen_m, prime_generator.gen_bpsw]
    generator=functions[methods.index(method)]
    bits=int(input('enter desired number of bits:'))
    file=open('rsa_keys.txt','a+')
    file.write('\n {0} \n {1}'.format(datetime.now(),Keys(bits)))
    file.close()