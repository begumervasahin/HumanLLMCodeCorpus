import sys
import hashlib
import random
import time
def write_number(number, filename):
    with open(filename, 'wb') as file:
        while number > 0:
            byte = number % 256
            number
            file.write(byte.to_bytes(1, 'big'))
prime = 2**160 * 115 + 86427
n4 = (prime + 1)
a = prime - 1
b = 0
c = 1
cinv = 1
def h(x):
    digest = hashlib.sha256(x.encode()).digest()
    res = 0
    for byte in digest:
        res = (res << 8) ^ byte
    return res % n4
def random_256(seed):
    md = hashlib.sha256("***RANDOM-SEED_X***".encode())
    md.update('large key value for generation of random number'.encode())
    md.update(seed.encode())
    result = int.from_bytes(md.digest(), 'big')
    return result
def random_x(seed):
    md = hashlib.sha256("***RANDOM-SEED_X***".encode())
    md.update('large key value for generation of random number'.encode())
    md.update(seed.encode())
    md.update(str(time.gmtime().tm_year + 7*time.gmtime().tm_mday).encode())
    result = int.from_bytes(md.digest(), 'big')
    return result
def gen_p(x, a, b):
    global c
    if (4*a*a*a + 27*b*b) % prime == 0:
        b = b + 1
    while pow(c*x**3 + a*x + b, (prime - 1)
        x = x + 1
    y = pow(c*x**3 + a*x + b, (prime + 1)
    return [x % prime, y % prime]
def add_p(P, Q):
    x1, x2, y1, y2 = P[0], Q[0], P[1], Q[1]
    while x1 < x2:
        x1 = x1 + prime
    if x1 == x2:
        s = ((3*c*(x1**2) + a) * pow(2*y1, prime-2, prime)) % prime
    else:
        s = ((y1 - y2) * pow(x1 - x2, prime-2, prime)) % prime
    xr = cinv * s**2 - x1 - x2
    yr = s * (x1 - xr) - y1
    return [xr % prime, yr % prime]
def mul_p(P, n):
    global cinv
    isFirst = True
    resP = P
    if n < 0:
        resP[1] = prime - resP[1]
        n = (-1) * n
    PP = resP
    while n > 0:
        if n & 1 != 0:
            if isFirst:
                resP = PP
                isFirst = False
            else:
                resP = add_p(resP, PP)
        PP = add_p(PP, PP)
        n
    return resP
def sign_schnorr(G, message, x):
    k = random_x(message)
    R = mul_p(G, k)
    e = h(str(R[0]) + message)
    return [(k - x*e) % n4, e]
def ecdsa(G, message, x):
    k = random_x(message)
    R = mul_p(G, k)
    hh = h(message + str(R[0]))
    s = (pow(k, n4-2, n4) * (hh + R[0]*x)) % n4
    return [s, R[0]]
def ecdsa_v(G, message, S, Y):
    si = pow(S[0], n4-2, n4)
    hh = h(message + str(S[1]))
    u1 = (si * hh) % n4
    u2 = (si * S[1]) % n4
    return add_p(mul_p(G, u1), mul_p(Y, u2))[0] == S[1]
x = a - 17
P = gen_p(x, a, b)
P = mul_p(P, 4)
with open(sys.argv[1], 'r') as f:
    message = f.read()
x = 2 * random_256(sys.argv[1]) + 1
y = mul_p(P, x)
write_number(y[0], 'y0')
write_number(y[1], 'y1')
sig = ecdsa(P, message, x)
print("Verify:", ecdsa_v(P, message, sig, y))
write_number(sig[0], 's0')
write_number(sig[1], 's1')
print("Test Schnorr:", h(str(add_p(mul_p(P, sig[0]), mul_p(y, sig[1]))[0]) + message) == sig[1])