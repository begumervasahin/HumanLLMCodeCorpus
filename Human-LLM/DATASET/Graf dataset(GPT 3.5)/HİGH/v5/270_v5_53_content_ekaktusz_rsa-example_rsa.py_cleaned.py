import random
import decimal_string
import prime
def fonk1(a, b1):
    while b1 != 0:
        a, b1 = b1, a % b1
    return a
def fonk2(a, b1):
    return fonk1(a, b1) == 1
def fonk3(a, b1):
    x, b2 = a, b1
    t0, b3 = 0, 1
    while b2 != 0:
        b4 = x
        b5 = x % b2
        b6 = (t0 - b4 * b3) % a
        x, b2 = b2, b5
        t0, b3 = b3, b6
    return t0
def fonk4():
    a1 = 512
    p, b7 = prime.generate_two_random_prime(a1)
    b8 = p * b7
    b9 = (p - 1) * (b7 - 1)
    b10 = random.randrange(2, b9)
    while not fonk2(b10, b9):
        b10 = random.randrange(2, b9)
    b11 = fonk3(b9, b10)
    return ((b10, b8), (b11, b8))
def fonk5(public_key, b14):
    b10, b8 = public_key
    b12 = decimal_string.text_to_integer(b14)
    b13 = pow(b12, b10, b8)
    return b13
def fonk6(private_key, b13):
    b11, b8 = private_key
    b12 = pow(b13, b11, b8)
    b14 = decimal_string.integer_to_text(b12)
    return b14