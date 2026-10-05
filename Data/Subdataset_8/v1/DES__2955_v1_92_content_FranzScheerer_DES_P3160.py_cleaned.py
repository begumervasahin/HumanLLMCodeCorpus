import random
import hashlib
def write_number(n, fnam):
    f = open(fnam, 'wb')
    while n > 0:
        b = n & 0xFF
        n >>= 8
        f.write(bytes([b]))
    f.close()
def read_number(fnam):
    f = open(fnam, 'rb')
    n = 0
    for c in reversed(f.read()):
        n = (n << 8) ^ c
    f.close()
    return n
def hex_text_to_number(x):
    res = 0
    for c in x:
        if ord(c) < 58 and ord(c) >= 48:
            res = (res << 4) + ord(c) - 48
        elif ord(c) <= ord('f') and ord(c) >= ord('a'):
            res = (res << 4) + ord(c) - 87
        elif ord(c) <= ord('F') and ord(c) >= ord('A'):
            res = (res << 4) + ord(c) - 55
    return res
def inverse(b, m):
    s = 0
    t = 1
    a = m
    while b != 1:
        q = a
        aa = b
        b = a % b
        a = aa
        ss = t
        t = s - q * t
        s = ss
    if t < 0:
        t = t + m
    return t
def h(x):
    dx1 = hashlib.sha256(x.encode(encoding='UTF-8', errors='strict')).hexdigest()
    res = 0
    for cx in dx1:
        res = (res << 8) ^ ord(cx)
    return res % n4
def generate_P(x, a, b):
    while pow(x ** 3 + a * x + b, (prime - 1)
        x = x + 1
    y = pow(x ** 3 + a * x + b, (prime + 1)
    return [x % prime, y % prime]
def add_P(P, Q):
    x1 = P[0]
    x2 = Q[0]
    y1 = P[1]
    y2 = Q[1]
    while x1 < x2:
        x1 = x1 + prime
    if x1 == x2:
        s = ((3 * (x1 ** 2) + a) * inverse(2 * y1, prime)) % prime
    else:
        s = ((y1 - y2) * inverse(x1 - x2, prime)) % prime
    xr = s ** 2 - x1 - x2
    yr = s * (x1 - xr) - y1
    return [xr % prime, yr % prime]
def multiply_P(P, n):
    isFirst = True
    resP = P
    if n < 0:
        resP[1] = prime - resP[1]
        n = (-1) * n
    PP = resP
    while n > 0:
        if (n % 2 != 0):
            if isFirst:
                resP = PP
                isFirst = False
            else:
                resP = add_P(resP, PP)
        PP = add_P(PP, PP)
        n = n
    return resP
def verify(G, s, Y, e, m):
    return e == h(str(add_P(multiply_P(G, s), multiply_P(Y, e))[0]) + m)
def ecdsa_v(G, m, S, Y):
    si = inverse(S[0], n4)
    hh = h(m + str(S[1]))
    u1 = (si * hh) % n4
    u2 = (si * S[1]) % n4
    return add_P(multiply_P(G, u1), multiply_P(Y, u2))[0] == S[1]
prime = hex_text_to_number("05 177B8A2A 0FD6A4FF 55CDA06B 0924E125 F86CAD9B")
a = hex_text_to_number("04 3182D283 FCE38807 30C9A2FD D3F60165 29A166AF")
b = hex_text_to_number("02 0C61E945 9E53D887 1BCAADC2 DFC8AD52 25228035")
n4 = hex_text_to_number("05 177B8A2A 0FD6A4FF 55CCA7B8 A1E21C88 BD53B2C1")
xx = 1
while pow(xx ** 3 + a * xx + b, (prime - 1)
    xx = xx + 1
yy = pow(xx ** 3 + a * xx + b, (prime + 1)
P = [xx, yy]
f = open(sys.argv[1], 'r')
message = f.read()
f.close()
y = [read_number('y0'), read_number('y1')]
sig = [read_number('s0'), read_number('s1')]
print("Public key: X:", y[0] % prime)
print("Public key: Y:", y[1] % prime)
print("Signature X:", sig[0])
print("Signature Y:", sig[1])
print("")
print("The verification of signature:", verify(P, sig[0], y, sig[1], message))
x = random.randint(2, n4 - 1)
ydsa = multiply_P(P, x)
def ecdsa(G, m, x):
    k = h(m + 'ecdsa')
    R = multiply_P(G, k)
    hh = h(m + str(R[0]))
    s = (inverse(k, n4) * (hh + R[0] * x)) % n4
    return [s, R[0]]
sig = ecdsa(P, message, x)
print("The verification of ECDSA signature:", ecdsa_v(P, message, sig, ydsa))
def sign_schnorr(G, m, x):
    k = h(m + 'kk2')
    R = multiply_P(G, k)
    e = h(str(R[0]) + m)
    return [(k - x * e) % n4, e]
onetime_private_key = h('kk1_' + str(random.randint(2, n4 - 1)))
sig = sign_schnorr(P, message, onetime_private_key)
y = multiply_P(P, onetime_private_key)
write_number(sig[0], 's0')
write_number(sig[1], 's1')
write_number(y[0], 'y0')
write_number(y[1], 'y1')
bit_length = 0
while 2 ** bit_length < n4:
    bit_length = bit_length + 1
print("\nMore security checks")
print("Bit length:", bit_length)
print("\nCheck prime:", pow(7, prime - 1, prime) == 1)
print("Prime order:", pow(7, n4 - 1, n4) == 1)
print("Period:", P == multiply_P(P, n4 + 1))