import math
from Crypto.Util import number
import os
def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b,a%b)
def ext_euclid(a, b):
     if b == 0:
         return 1, 0, a
     else:
         x, y, q = ext_euclid(b, a % b)
         x, y = y, (x - (a
         return x, y, q
def generate(p,q):
    N = p*q
    n = (p-1)*(q-1)
    alle = []
    for e in range(2,n-1):
        if gcd(e,n)==1:
            alle.append(e)
            break
    e = alle[0]
    d = ext_euclid(-n,e)[1]
    if d < 0:
        d = d + n
    else:
        d = d
    d = (d+n) if (d<0) else d
    return N,n,e,d
def encrypt(m,e,N):
    print("[*]encrypt...")
    return fastExpMod(m,e,N)
def decrypt(c,d,N):
    print("[*]decrypt.....")
    return fastExpMod(c,d,N)
def fastExpMod(b, e, m):
    result = 1
    while e != 0:
        if (e&1) == 1:
            result = (result * b) % m
        e >>= 1
        b = (b*b) % m
    return result
def textTonum(c):
    c_bin = ''
    for item in c:
        tmp = bin(int(ord(item)))[2:]
        while len(tmp)!=8:
            tmp = '0'+str(tmp)
        c_bin = c_bin + tmp
    return int(str(c_bin),2)
def numTotext(num):
    tmp = bin(num)[2:]
    while len(tmp)%8!=0:
        tmp = '0' + tmp
    text = ''
    for i in range(len(tmp)
        a = int(tmp[8*i:8*(i+1)],2)
        text += chr(a)
    return text
def RSA(c):
    m = textTonum(c)
    print('[*]this is num....', m)
    p = number.getPrime(256, os.urandom)
    print("[*]getp..",p)
    q = number.getPrime(256, os.urandom)
    print("[*]getq..",q)
    print("[*]start....")
    N,n,e,d = generate(p,q)
    c = encrypt(m,e,N)
    result = numTotext(c)
    print(result)
if __name__ == "__main__":
    c = "Hi,this is RSA!"
    RSA(c)