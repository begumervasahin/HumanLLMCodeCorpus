import random
import hashlib
import sys
A_SPRITZ = I_SPRITZ = J_SPRITZ = W_SPRITZ = 0
S_SPRITZ = []
def update_spritz():
    global A_SPRITZ, I_SPRITZ, J_SPRITZ, W_SPRITZ, S_SPRITZ
    I_SPRITZ = (I_SPRITZ + W_SPRITZ) % 256
    J_SPRITZ = S_SPRITZ[(J_SPRITZ + S_SPRITZ[I_SPRITZ]) % 256]
    S_SPRITZ[I_SPRITZ], S_SPRITZ[J_SPRITZ] = S_SPRITZ[J_SPRITZ], S_SPRITZ[I_SPRITZ]
def output_spritz():
    global A_SPRITZ, I_SPRITZ, J_SPRITZ, W_SPRITZ, S_SPRITZ
    update_spritz()
    return S_SPRITZ[J_SPRITZ]
def shuffle_spritz():
    global A_SPRITZ, I_SPRITZ, J_SPRITZ, W_SPRITZ, S_SPRITZ
    for _ in range(256):
        update_spritz()
    W_SPRITZ = (W_SPRITZ + 2) % 256
    A_SPRITZ = 0
def absorb_nibble_spritz(x):
    global A_SPRITZ, I_SPRITZ, J_SPRITZ, W_SPRITZ, S_SPRITZ
    if A_SPRITZ == 240:
        shuffle_spritz()
    S_SPRITZ[A_SPRITZ], S_SPRITZ[240 + x] = S_SPRITZ[240 + x], S_SPRITZ[A_SPRITZ]
    A_SPRITZ += 1
def absorb_byte_spritz(b):
    absorb_nibble_spritz(b % 16)
    absorb_nibble_spritz(b
def squeeze_spritz(out, outlen):
    global A_SPRITZ, I_SPRITZ, J_SPRITZ, W_SPRITZ, S_SPRITZ
    if A_SPRITZ != 0:
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
        if (pow(7, p - 1, p) != 1 or pow(7, (p + 1)
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
        if ord(c) < 58 and ord(c) >= 48:
            res = (res << 4) + ord(c) - 48
        elif ord(c) <= ord('f') and ord(c) >= ord('a'):
            res = (res << 4) + ord(c) - 87
        elif ord(c) <= ord('F') and ord(c) >= ord('A'):
            res = (res << 4) + ord(c) - 55
    return res
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
    global A_SPRITZ, I_SPRITZ, J_SPRITZ, W_SPRITZ, S_SPRITZ
    I_SPRITZ = J_SPRITZ = A_SPRITZ = 0
    W_SPRITZ = 1
    S_SPRITZ = list(range(256))
    for c in x:
        absorb_byte_spritz(ord(c))
    res = []
    squeeze_spritz(res, 32)
    out = 0
    for bx in res:
        out = (out << 8) + bx
    return out % H_SIZE
def point_addition(P, Q):
    x1, x2 = P[0], Q[0]
    y1, y2 = P[1], Q[1]
    if x1 == x2:
        s = ((3 * (x1**2) + A) * modular_inverse(2 * y1, PRIME)) % PRIME
    else:
        if x1 < x2:
            x1 += PRIME
        s = ((y1 - y2) * modular_inverse(x1 - x2, PRIME)) % PRIME
    xr = s**2 - x1 - x2
    yr = s * (x1 - xr) - y1
    return [xr % PRIME, yr % PRIME]
def scalar_multiplication(P, n):
    isFirst = True
    resP = P
    if n < 0:
        resP[1] = PRIME - resP[1]
        n = (-1) * n
    PP = resP
    while n > 0:
        if (n % 2 != 0):
            if isFirst:
                resP = PP
                isFirst = False
            else:
                resP = point_addition(resP, PP)
        PP = point_addition(PP, PP)
        n = n
    return resP
def verify_signature(G, s, Y, e, m):
    return e == hash_func(str(point_addition(scalar_multiplication(G, s), scalar_multiplication(Y, e))[0]) + m)
def ecdsa_verification(G, m, S, Y):
    si = modular_inverse(S[0], R)
    hh = hash_func(m + str(S[1]))
    u1 = (si * hh) % R
    u2 = (si * S[1]) % R
    return point_addition(scalar_multiplication(G, u1), scalar_multiplication(Y, u2))[0] == S[1]
PRIME = next_prime(12 * 2**141)
print("A prime greater than 12 times 2^141 \np = ", PRIME)
A = 0
B = PRIME - 3
R = (PRIME + 1)
H_SIZE = R
x = 1
while pow(x**3 + A*x + B, (PRIME - 1)
    x += 1
y = pow(x**3 + A*x + B, (PRIME + 1)
P = [x % PRIME, y % PRIME]
P = scalar_multiplication(P, 12)
message = sys.argv[1]
Y = [7743078162825626208847856060554090836324463, 7535129688736902967896532855534019525412438]
sig = [read_number('s0'), read_number('s1')]
print("Public key: X: ", Y[0] % PRIME)
print("Public key: Y: ", Y[1] % PRIME)
print("Signature X: ", sig[0])
print("Signature Y: ", sig[1])
print("")
print("The verification of signature: ", verify_signature(P, sig[0], Y, sig[1], message))