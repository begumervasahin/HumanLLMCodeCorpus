from curve import Curve
from random import randint
import math
import sys
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
        x = (1000 * x0 + i) % p
        t = (x ** 3 + a * x + b) % p
        res = prime_mod_sqrt(t, p)
        if res:
            return Point.make_point(x, res[0], 1, p)
def encode_string(s, curve, length):
    arr = []
    chunks = list(chunkstring(s, length))
    for chunk in chunks:
        arr.append(ECencode(chunk, curve))
    return arr
def encrypt_long(arr, key):
    curve = key.curve
    p = curve.p
    P = key.P
    Q = key.Q
    l = randint(1, p - 1)
    res = [curve.multiply(l, P)]
    lQ = curve.multiply(l, Q)
    for point in arr:
        res.append(curve.add_points(lQ, point))
    return res
def decrypt_long(arr, key, k):
    res = []
    curve = key.curve
    neg_kC1 = curve.multiply(k, arr[0]).negate()
    for point in arr[1:]:
        res.append(curve.add_points(point, neg_kC1))
    return res
def decode_string(arr):
    return ''.join(ECdecode(point) for point in arr)
def chunkstring(string, length):
    return (string[i:i + length] for i in range(0, len(string), length))
def ECdecode(P):
    n = (P.x - P.x % 1000)
    v = []
    while n != 0:
        v.append(chr(n % 256))
        n
    return ''.join(v)
def encrypt(s, key):
    curve = key.curve
    p = curve.p
    return encrypt_long(encode_string(s, curve, int(math.log(p
def decrypt(arr, key, k):
    return decode_string(decrypt_long(arr, key, k))
def miller_rabin(n, k):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s
    for _ in range(k):
        a = randint(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True
def random_prime(low, high):
    while True:
        candidate = randint(low, high)
        if miller_rabin(candidate, 45):
            return candidate
def main():
    print("\nElliptic Curve Cryptosystem: written by Kyle Linzy")
    print("*Note* Press Ctrl-C to exit the loop and the demo\n")
    num_zeros = int(input("Enter a number of digits for the prime number (i.e. 3 => 100 < prime < 1000).\nMinimum is 6 \nNumber of Zeros = "))
    if num_zeros < 6:
        num_zeros = 6
    low = 10 ** (num_zeros - 1)
    high = low * 10
    prime = random_prime(low, high)
    private_key = randint(1, prime - 1)
    public_key = Public_Key.make_public_key(prime, private_key)
    print(public_key)
    print()
    while True:
        message = input("Enter a message to be encrypted\n")
        print()
        encrypted_message = encrypt(message, public_key)
        print("Encrypted array of points on the curve:\n", encrypted_message)
        print()
        decrypted_message = decrypt(encrypted_message, public_key, private_key)
        print("Decrypted string:\n", decrypted_message)
        print()
if __name__ == "__main__":
    main()