
from curve import Curve
from point import Point
from public_key import Public_Key
from random import randint
import math
def encode_string_to_points(string, curve, chunk_length):
    points = []
    chunks = split_string_into_chunks(string, chunk_length)
    for chunk in chunks:
        points.append(encode_chunk(chunk, curve))
    return points
def encode_chunk(chunk, curve):
    a, b, p = curve.a, curve.b, curve.p
    chunk_int = string_to_int(chunk)
    for i in range(1000):
        x = 1000 * chunk_int + i % p
        t = (x ** 3 + a * x + b) % p
        res = prime_mod_sqrt(t, p)
        if len(res) != 0:
            return Point.make_point(x, res[0], 1, p)
def split_string_into_chunks(string, length):
    return [string[i:i+length] for i in range(0, len(string), length)]
def decode_points_to_string(points):
    decoded = []
    for point in points:
        decoded.append(decode_point(point))
    return ''.join(decoded)
def decode_point(point):
    n = (point.x - point.x % 1000)
    chars = []
    while n != 0:
        chars.append(chr(n % 256))
        n
    return ''.join(chars[::-1])
def encrypt_string(string, key):
    curve, p = key.curve, key.curve.p
    chunk_length = int(math.log(p
    encoded_points = encode_string_to_points(string, curve, chunk_length)
    return encrypt_points(encoded_points, key)
def encrypt_points(points, key):
    curve, p = key.curve, key.curve.p
    l = randint(1, p - 1)
    res = [curve.multiply(l, key.P)]
    lQ = curve.multiply(l, key.Q)
    for point in points:
        res.append(curve.add_points(lQ, point))
    return res
def decrypt_points(points, key, k):
    curve = key.curve
    neg_kC1 = curve.multiply(k, points[0]).negate()
    decrypted = []
    for point in points[1:]:
        ans = curve.add_points(point, neg_kC1)
        decrypted.append(ans)
    return decrypted
def generate_random_prime(low, high):
    while True:
        result = randint(low, high)
        if miller_rabin(result, 45):
            return result
