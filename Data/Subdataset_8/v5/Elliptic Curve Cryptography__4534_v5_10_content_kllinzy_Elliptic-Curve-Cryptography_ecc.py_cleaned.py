from curve import Curve
from random import randint
import math
from point import Point
from public_key import Public_Key
def ECencode(s, curve):
    a = curve.a
    b = curve.b
    p = curve.p
    s = str(s)
    x0 = 0
    for i in range(len(s)):
        x0 += ord(s[i]) * 256 ** i
    for i in range(1000):
        x = 1000 * x0 + i % p
        t = (x ** 3 + a * x + b) % p
        res = prime_mod_sqrt(t, p)
        if len(res) != 0:
            return Point.make_point(x, res[0], 1, p)
def encode_string(s, curve, length):
    arr = []
    l = list(chunkstring(s, length))
    for i in range(len(l)):
        arr.append(ECencode(l[i], curve))
    return arr
def encrypt(s, key):
    curve = key.curve
    p = curve.p
    return encrypt_long(encode_string(s, curve, int(math.log(p
def decrypt(arr, key, k):
    return decode_string(decrypt_long(arr, key, k))
def random_prime(low, high):
    result = 0
    while True:
        result = randint(low, high)
        if miller_rabin(result, 45):
            break
    return result
def miller_rabin(n, k):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
