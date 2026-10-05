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
    b7, b2 = a, b1
    b8, b3 = 0, 1
    b6, b4 = b1, 1
    while (b7 % b2) != 0:
        b5 = b7
        b6 = b7 % b2
        b4 = (b8 - b5*b3) % a
        b7 = b2
        b2 = b6
        b8 = b3
        b3 = b4
    return b4
def fonk4():
    p, b5 = prime.generate_two_random_prime(512)
    b9 = p * b5
    b10 = (p-1)*(b5-1)
    b11 = random.randrange(1, b10)
    while not fonk2(b11, b10):
        b11 = random.randrange(1, b10)
    b12 = fonk3(b10, b11)
    return ((b11, b9), (b12, b9))
def fonk5(public_key, text):
    b11, b9 = public_key
    b13 = decimal_string.text_to_integer(text)
    b14 = pow(b13, b11, b9)
    return b14
def fonk6(b16, b13):
    b12, b9 = b16
    b15 = pow(b13, b12, b9)
    return decimal_string.integer_to_text(b15)
public_key, b16 = fonk4()
b17 = "Hello, World!"
b18 = fonk5(public_key, b17)
print("Encrypted b17:", b18)
b19 = fonk6(b16, b18)
print("Decrypted b17:", b19)