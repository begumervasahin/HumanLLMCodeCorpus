import sys
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
def random_seed(m):
    md = hashlib.sha256("***RANDOM-SEED_X***".encode())
    md.update('large key value for generation of random number'.encode())
    md.update(m.encode())
    result = 0
    largest_r = md.digest()
    for i in range(len(largest_r)):
        result = (result << 8) ^ ord(largest_r[i])
    return result
def generate_point(x, a, b):
    if (4 * a * a * a + 27 * b * b) % prime == 0:
        b += 1
    while pow(c * x ** 3 + a * x + b, (prime - 1)
        x += 1
    y = pow(c * x ** 3 + a * x + b, (prime + 1)
    return [x % prime, y % prime]
def multiply_point(P, n):
    isFirst = True
    res_P = P
    if n < 0:
        res_P[1] = prime - res_P[1]
        n = -n
    bsize = 20
    while 2 ** bsize < n:
        bsize += 1
    PP = res_P
    for b in range(bsize + 1):
        if n & (1 << b) != 0:
            if isFirst:
                res_P = PP
                isFirst = False
            else:
                res_P = add_point(res_P, PP)
        PP = double_point(PP)
    return res_P
if __name__ == "__main__":
    P = generate_point(x, a, b)
    P = multiply_point(P, 4)
