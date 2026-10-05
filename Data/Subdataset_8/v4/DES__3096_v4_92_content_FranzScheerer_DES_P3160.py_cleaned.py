import random
import hashlib
import sys
def writeNumber(n, filename):
    with open(filename, 'wb') as file:
        while n > 0:
            b = n & 0xFF
            n >>= 8
            file.write(bytes([b]))
def readNumber(filename):
    with open(filename, 'rb') as file:
        n = 0
        for c in reversed(file.read()):
            n = (n << 8) ^ c
    return n
def hexTextToNum(x):
    res = 0
    for c in x:
        if '0' <= c <= '9':
            res = (res << 4) + ord(c) - ord('0')
        elif 'a' <= c <= 'f':
            res = (res << 4) + ord(c) - ord('a') + 10
        elif 'A' <= c <= 'F':
            res = (res << 4) + ord(c) - ord('A') + 10
    return res
def inv(b, m):
    s, t, a = 0, 1, m
    while b != 1:
        q = a
        aa = b
        b = a % b
        a = aa
        ss = t
        t = s - q * t
        s = ss
    if t < 0:
        t += m
    return t
def h(x):
    dx1 = hashlib.sha256(x.encode(encoding='UTF-8')).hexdigest()
    res = 0
    for cx in dx1:
        res = (res << 8) ^ ord(cx)
    return res % n4
def genP(x, a, b):
    while pow(x**3 + a*x + b, (prime - 1)
        x += 1
    y = pow(x**3 + a*x + b, (prime + 1)
    return [x % prime, y % prime]
def addP(P, Q):
    x1, x2, y1, y2 = P[0], Q[0], P[1], Q[1]
    while x1 < x2:
        x1 += prime
    if x1 == x2:
        s = ((3*(x1**2) + a) * inv(2*y1, prime)) % prime
    else:
        s = ((y1-y2) * inv(x1-x2, prime)) % prime
    xr = s**2 - x1 - x2
    yr = s * (x1-xr) - y1
    return [xr % prime, yr % prime]
def mulP(P, n):
    isFirst = True
    resP = P
    if n < 0:
        resP[1] = prime - resP[1]
        n = (-1)*n
    PP = resP
    while n > 0:
        if (n % 2 != 0):
            if isFirst:
                resP = PP
                isFirst = False
            else:
                resP = addP(resP, PP)
        PP = addP(PP, PP)
        n = n
    return resP
def verify(G, s, Y, e, m):
    return e == h(str(addP(mulP(G, s), mulP(Y, e))[0]) + m)
def ecdsa_v(G, m, S, Y):
    si = inv(S[0], n4)
    hh = h(m + str(S[1]))
    u1 = (si * hh) % n4
    u2 = (si * S[1]) % n4
    return addP(mulP(G, u1), mulP(Y, u2))[0] == S[1]
xx = 1
while pow(xx**3 + a*xx + b, (prime - 1)
    xx += 1
yy = pow(xx**3 + a*xx + b, (prime + 1)
P = [xx, yy]
f = open(sys.argv[1], 'r')
message = f.read()
f.close()
y = [readNumber('y0'), readNumber('y1')]
sig = [readNumber('s0'), readNumber('s1')]
print("Public key: X:", y[0] % prime)
print("Public key: Y:", y[1] % prime)
print("Signature X:", sig[0])
print("Signature Y:", sig[1])
print()
print("The verification of signature:", verify(P, sig[0], y, sig[1], message))
x = random.randint(2, n4 - 1)
ydsa = mulP(P, x)
sig = ecdsa(P, message, x)
print("The verification of ECDSA signature:", ecdsa_v(P, message, sig, ydsa))
onetime_private_key = h('kk1_' + str(random.randint(2, n4 - 1)))
sig = signSchnorr(P, message, onetime_private_key)
writeNumber(sig[0], 's0')
writeNumber(sig[1], 's1')
y = mulP(P, onetime_private_key)
writeNumber(y[0], 'y0')
writeNumber(y[1], 'y1')
bit_length = 0
while 2 ** bit_length < n4:
    bit_length += 1
print("\nMore security checks")
print("Bit length:", bit_length)
print("\nCheck prime:", pow(7, prime - 1, prime) == 1)
print("Prime order:", pow(7, n4 - 1, n4) == 1)
print("Period:", P == mulP(P, n4 + 1))