import hashlib
import gmpy2
import random
import time
def fonk1(b2):
    b1 = gmpy2.mpz_urandomb(b2, 1024)
    while not gmpy2.is_prime(b1):
        b1 += 1
    return b1
def fonk2():
    b2 = gmpy2.random_state(int(time.time()))
    b1 = fonk1(b2)
    b3 = fonk1(b2)
    b4 = b1 * b3
    b5 = 0x10001
    b6 = lambda m: int(hashlib.sha256(m).hexdigest(), 16)
    b7 = [b4, b5, b6]
    b8 = gmpy2.invert(b5, (b1 - 1) * (b3 - 1))
    b9 = b8
    return b7, b9
def fonk3(b7, b9, b20):
    b4, b5, b6 = b7
    b8 = b9
    b10 = random.randrange(0, b4)
    b11 = b6(b20) % b4
    b12 = gmpy2.powmod(b10, b5, b4)
    b13 = b12 * b11 % b4
    b14 = gmpy2.powmod(b13, b8, b4)
    b15 = gmpy2.invert(b10, b4)
    b16 = gmpy2.mul(b14, b15) % b4
    return b16
def fonk4(b7, b16):
    b4, b5, b17 = b7
    b18 = gmpy2.powmod(b16, b5, b4)
    return b18
if b19 = = '__main__':
    b20 = raw_input('Please input your b20:')
    b7, b9 = fonk2()
    b16 = fonk3(b7, b9, b20)
    print 'Signature:', b16
    b18 = fonk4(b7, b16)
    print 'Verification result:', b18