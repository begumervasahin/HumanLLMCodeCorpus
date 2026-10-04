import random
from random import randrange
def binary2dec(binary):
    return int(binary, 2)
def dec2binary(dec, length):
    return bin(dec)[2:].zfill(length)
def rand_bin(length):
    return ''.join([str(randrange(0, 2)) for _ in range(length)])
def two_com(binary, length):
    if binary[0] == '1':
        complement = ''.join('1' if bit == '0' else '0' for bit in binary)
        return bin(binary2dec(complement) + 1)[2:].zfill(length)
    return binary.zfill(length)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = egcd(b % a, a)
        return g, y - (b
def multiplicative_inverse(e, phi):
    g, x, y = egcd(e, phi)
    if g != 1:
        raise Exception('No modular inverse')
    else:
        return x % phi
def isPrime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True
def main():
    mlen = 512
    rlen = 512
    eleng = 1024
    m = rand_bin(mlen)
    m = two_com(m, mlen)
    while not isPrime(binary2dec(m)):
        m = rand_bin(mlen)
        m = two_com(m, mlen)
    r = rand_bin(rlen)
    r = two_com(r, rlen)
    while not isPrime(binary2dec(r)):
        r = rand_bin(rlen)
        r = two_com(r, rlen)
    e = rand_bin(eleng)
    e = two_com(e, eleng)
    m = binary2dec(m)
    r = binary2dec(r)
    n = m * r
    phi = (m - 1) * (r - 1)
    e = binary2dec(e)
    while gcd(e, phi) != 1 or not isPrime(e):
        e = rand_bin(eleng)
        e = two_com(e, eleng)
        e = binary2dec(e)
    d = multiplicative_inverse(e, phi)
    print('n =', n)
    print('Public Key (e) =', e)
    print('Private Key (d) =', d)
if __name__ == "__main__":
    main()