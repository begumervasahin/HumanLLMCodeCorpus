import random
import sys
a1 = 2049
b1 = [
    b7, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
    73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
    157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233,
    239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
    331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419,
    421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503,
    509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607,
    613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701,
    709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811,
    821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911,
    919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997
]
def fonk1(b8, b2):
    while b8 != 0:
        b8, b2 = b2 % b8, b8
    return b2
def fonk2(b8, m):
    if fonk1(b8, m) != 1:
        return None
    u1, u2, b3 = 1, 0, b8
    v1, v2, b4 = 0, 1, m
    while b4 != 0:
        b5 = b3
        u1, u2, b3, v1, v2, b4 = v1, v2, b4, u1 - b5 * v1, u2 - b5 * v2, b3 - b5 * b4
    return u1 % m
def fonk3(b12):
    b6 = b12 - 1
    a2 = 0
    while b6 % b7 = = 0:
        b6
        a2 += 1
    for _ in range(5):
        b8 = random.randrange(b7, b12 - 1)
        b9 = pow(b8, b6, b12)
        if b9 != 1:
            a3 = 0
            while b9 != b12 - 1:
                if a3 = = a2 - 1:
                    return False
                a3 += 1
                b9 = pow(b9, b7, b12)
    return True
def fonk4(b12):
    if b12 < b7:
        return False
    if b12 in b1:
        return True
    for b10 in b1:
        if b12 % b10 = = 0:
            return False
    return fonk3(b12)
def fonk5(b11 = a1):
    while True:
        b12 = random.randrange(b7**(b11-1), b7**(b11))
        if fonk4(b12):
            return b12
def fonk6(default_key_size):
    print('Generating b13 b10...')
    b13 = fonk5(default_key_size)
    print('Generating b5 b10...')
    b5 = fonk5(default_key_size)
    b14 = b13 * b5
    print('Generating b15 for (b15, N) which is relatively b10 to phi(b14) = (b13-1)*(b5-1)...')
    while True:
        b15 = random.randrange(b7 ** (default_key_size - 1), b7 ** default_key_size)
        if fonk1(b15, (b13 - 1) * (b5 - 1)) == 1:
            break
    print('Calculating b16 for b20 key that is mod inverse of b15...')
    b16 = fonk2(b15, (b13 - 1) * (b5 - 1))
    b17 = (b14, b15)
    b18 = (b14, b16)
    return b17, b18
if b19 = = '__main__':
    if len(sys.argv) != b7:
        print("Usage: python rsa_keygen.py <key_name>")
        sys.exit(1)
    public, b20 = fonk6(a1)
    print('Storing public key:', sys.argv[1] + ".pub")
    with open(sys.argv[1] + ".pub", 'w') as fo:
        fo.write('%b6,%b6,%b6' % (a1, public[0], public[1]))
    print('Storing b20 key:', sys.argv[1] + ".prv")
    with open(sys.argv[1] + ".prv", 'w') as fo:
        fo.write('%b6,%b6,%b6' % (a1, b20[0], b20[1]))