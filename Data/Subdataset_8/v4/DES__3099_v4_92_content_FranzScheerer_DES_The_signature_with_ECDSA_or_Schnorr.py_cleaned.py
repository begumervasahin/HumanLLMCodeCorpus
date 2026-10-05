import sys
import math
import hashlib
import random
import time
def write_number(number, fname):
    with open(fname, 'wb') as f:
        while number > 0:
            byte = number % 256
            number
            f.write(chr(byte))
def h(x):
    dx1 = hashlib.sha256(x).digest()
    res = 0
    for cx in dx1:
        res = (res << 8) ^ ord(cx)
    return res % n4
def random256(m):
    md = hashlib.sha256("***RANDOM-SEED_X***")
    md.update('large key value for generation of random number')
    md.update(m)
    result = 0
    largestr = md.digest()
    for i in range(len(largestr)):
        result = (result << 8) ^ ord(largestr[i])
    return result
def randomX(m):
    md = hashlib.sha256("***RANDOM-SEED_X***")
    md.update('large key value for generation of random number')
    md.update(m)
    md.update(str(time.gmtime().tm_year + time.gmtime().tm_mday))
    result = 0
    largestr = md.digest()
    for i in range(len(largestr)):
        result = (result << 8) ^ ord(largestr[i])
    return result
def genP(x, a, b):
    if (4 * a * a * a + 27 * b * b) % prime == 0:
        b = b + 1
    while pow(c * x ** 3 + a * x + b, (prime - 1)
        x = x + 1
    y = pow(c * x ** 3 + a * x + b, (prime + 1)
    return [x % prime, (y) % prime]
def dpoint(P):
    x = P[0]
    y = P[1]
    s = ((3 * c * (x ** 2) + a) * inv(2 * y, prime)) % prime
    xr = (cinv * s ** 2 - 2 * x) % prime
    yr = (-y + s * (x - xr)) % prime
    return [xr, yr]
def addP(P, Q):
    if P == Q:
        return dpoint(P)
    x1 = P[0]
    x2 = Q[0]
    y1 = P[1]
    y2 = Q[1]
    while x1 < x2:
        x1 = x1 + prime
    while y1 < y2:
        y1 = y1 + prime
    s = ((y1 - y2) * inv(x1 - x2, prime)) % prime
    xr = cinv * s ** 2 - x1 - x2
    yr = s * (x1 - xr) - y1
    return [xr % prime, yr % prime]
def mulP(P, n):
    isFirst = True
    resP = P
    if n < 0:
        resP[1] = prime - resP[1]
        n = (-1) * n
    bsize = 20
    while 2 ** bsize < n:
        bsize = bsize + 1
    PP = resP
    for b in range(bsize + 1):
        if (n & (1 << b) != 0):
            if isFirst:
                resP = PP
                isFirst = False
            else:
                resP = addP(resP, PP)
        PP = dpoint(PP)
    return resP
def signSchnorr(G, m, x):
    k = randomX(m)
    R = mulP(G, k)
    e = h(str(R[0]) + m)
    return [(k - x * e) % n4, e]
def ecdsa(G, m, x):
    k = randomX(m)
    R = mulP(G, k)
    hh = h(m + str(R[0]))
    s = (inv(k, n4) * (hh + R[0] * x)) % n4
    return [s, R[0]]
def ecdsa_v(G, m, S, Y):
    si = inv(S[0], n4)
    hh = h(m + str(S[1]))
    u1 = (si * hh) % n4
    u2 = (si * S[1]) % n4
    return addP(mulP(G, u1), mulP(Y, u2))[0] == S[1]
prime = 2 ** 256 - 2 ** 224 + 2 ** 192 + 2 ** 96 - 1
n4 = (prime + 1)
a = prime - 1
c = 1
cinv = 1
x = a - 17
P = genP(x, a, b)
P = mulP(P, 4)
f = open(sys.argv[1], 'r')
message = f.read()
f.close()
x = 2 * random256(sys.argv[1]) + 1
y = mulP(P, x)
write_number(y[0], 'y0')
write_number(y[1], 'y1')
sig = ecdsa(P, message, x)
print("Verify:", ecdsa_v(P, message, sig, y))
write_number(sig[0], 's0')
write_number(sig[1], 's1')
print("Test Schnorr:", h(str(addP(mulP(P, sig[0]), mulP(y, sig[1]))[0]) + message) == sig[1])