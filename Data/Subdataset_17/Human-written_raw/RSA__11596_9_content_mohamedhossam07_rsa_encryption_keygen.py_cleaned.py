from binary_mult import *
from keygen_extras import *
from random import *
import random
def hcfnaive(a,b):
    if(b==0):
        return a
    else:
        return hcfnaive(b,a%b)
def main():
    mlen = 512
    rlen = 512
    leng = 512
    eleng = 1024
    m = rand_bin(leng)
    m =two_com(m,mlen)
    while isPrime(binary2dec(m) ) != True :
        m = rand_bin(leng)
        m =two_com(m,leng)
    r = rand_bin(leng)
    r = two_com(r,leng)
    while isPrime(binary2dec(r)) != True :
        r = rand_bin(leng)
        r =two_com(r,eleng)
    e = rand_bin(eleng)
    e = two_com(e,eleng)
    m = binary2dec(m)
    r = binary2dec(r)
    fi = (m-1)*(r-1)
    g = 5
    e = binary2dec(e)
    while g != 1:
        while isPrime(e) != True :
            e = rand_bin(eleng)
            e =two_com(e,eleng)
            e = binary2dec(e)
        g = gcd(e, fi)
    print('n is = '+str(fi))
    print('')
    print('Public Key is = '+str(e))
    print('')
    d = multiplicative_inverse(e, fi)
    print('Private Key is = '+str(d))
    print('')
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b
def isPrime(n, k=1):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s
    for _ in range(0,k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(0,r - 1):
            x = power(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
if __name__ == "__main__":
    main()