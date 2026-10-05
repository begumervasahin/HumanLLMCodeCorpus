import random
import math
a_spritz = i_spritz = j_spritz = w_spritz = 0
s_spritz = []
def update_spritz():
    global a_spritz, i_spritz, j_spritz, w_spritz, s_spritz
    i_spritz = (i_spritz + w_spritz) % 256
    j_spritz = s_spritz[(j_spritz + s_spritz[i_spritz]) % 256]
    s_spritz[i_spritz], s_spritz[j_spritz] = s_spritz[j_spritz], s_spritz[i_spritz]
def output_spritz():
    global a_spritz, i_spritz, j_spritz, w_spritz, s_spritz
    update_spritz()
    return s_spritz[j_spritz]
def shuffle_spritz():
    global a_spritz, i_spritz, j_spritz, w_spritz, s_spritz
    for _ in range(256):
        update_spritz()
    w_spritz = (w_spritz + 2) % 256
    a_spritz = 0
def absorb_nibble_spritz(x):
    global a_spritz, s_spritz
    if a_spritz == 240:
        shuffle_spritz()
    s_spritz[a_spritz], s_spritz[240 + x] = s_spritz[240 + x], s_spritz[a_spritz]
    a_spritz += 1
def absorb_byte_spritz(b):
    absorb_nibble_spritz(b % 16)
    absorb_nibble_spritz(b
def squeeze_spritz(out, outlen):
    global a_spritz
    if a_spritz != 0:
        shuffle_spritz()
    for _ in range(outlen):
        out.append(output_spritz())
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
def next_prime(p):
    while p % 12 != 11:
        p += 1
    return next_prime_odd(p)
def next_prime_odd(p):
    m_ =  5 * 7 * 11 * 13 * 17 * 19 * 23 * 29 * 31 * 37 * 41 * 43 * 47
    while True:
        while gcd(p, m_) != 1 or gcd((p + 1)
            p += 12
        if pow(7, p - 1, p) != 1 or pow(7, (p + 1)
            p += 12
            continue
        return p
def read_number(filename):
    with open(filename, 'rb') as f:
        n = 0
        snum = f.read()
        for i in range(len(snum)):
            n = (n << 8) ^ ord(snum[len(snum) - i - 1])
    return n
def hex_text_to_num(x):
    res = 0
    for c in x:
        if '0' <= c <= '9':
            res = (res << 4) + ord(c) - ord('0')
        elif 'a' <= c <= 'f':
            res = (res << 4) + ord(c) - ord('a') + 10
        elif 'A' <= c <= 'F':
            res = (res << 4) + ord(c) - ord('A') + 10
    return res
prime = next_prime(12 * 2**141)
print(f"A prime greater than 12 times 2^141 \np = {prime}")
a = 0
b = prime - 3
r = (prime + 1)
hsize = r
def modular_inverse(b, a):
    m = a
    s = 0
    t = 1
    while b != 1:
        q = a
        a_tmp = b
        b = a % b
        a = a_tmp
        s_tmp = t
        t = s - q * t
        s = s_tmp
    if t < 0:
        t += m
    return t
def hash_func(x):
    global a_spritz, w_spritz, s_spritz
    i_spritz = j_spritz = a_spritz = 0
    w_spritz = 1
    s_spritz = list(range(256))
    for c in x:
        absorb_byte_spritz(ord(c))
    res = []
    squeeze_spritz(res, 32)
    out = 0
    for bx in res:
        out = (out << 8) + bx
    return out % hsize
def point_addition(P, Q):
    x1, x2, y1, y2 = P[0], Q[0], P[1], Q[1]
    if x1 == x2:
        s = ((3 * (x1**2) + a) * modular_inverse(2 * y1, prime)) % prime
    else:
        if x1 < x2:
            x1 += prime
        s = ((y1 - y2) * modular_inverse(x1 - x2, prime)) % prime
    xr = s**2 - x1 - x2
    yr = s * (x1 - xr) - y1
    return [xr % prime, yr % prime]
def scalar_multiplication(P, n):
    resP, isFirst = P, True
    if n < 0:
        resP[1] = prime - resP[1]
        n = -n
    PP = resP
    while n > 0:
        if n % 2 != 0:
            resP = PP if isFirst else point_addition(resP, PP)
            isFirst = False
        PP = point_addition(PP, PP)
        n
    return resP
def verify_signature(G, s, Y, e, m):
    return e == hash_func(str(point_addition(scalar_multiplication(G, s), scalar_multiplication(Y, e))[0]) + m)
def ecdsa_verification(G, m, S, Y):
    si = modular_inverse(S[0], r)
    hh = hash_func(m + str(S[1]))
    u1 = (si * hh) % r
    u2 = (si * S[1]) % r
    return point_addition(scalar_multiplication(G, u1), scalar_multiplication(Y, u2))[0] == S[1]
x = 1
while pow(x**3 + a * x + b, (prime - 1) / 2, prime) != 1:
    x += 1
y = pow(x**3 + a * x + b, (prime + 1) / 4, prime)
P = [x % prime, y % prime]
P = scalar_multiplication(P, 12)
message = sys.argv[1]
Y = [7743078162825626208847856060554090836324463, 7535129688736902967896532855534019525412438]
sig = [read_number('s0'), read_number('s1')]
print("Public key: X:", y[0] % prime)
print("Public key: Y:", y[1] % prime)
print("Signature X:", sig[0])
print("Signature Y:", sig[1])
print("")
print("The verification of signature:", verify_signature(P, sig[0], Y, sig[1], message))