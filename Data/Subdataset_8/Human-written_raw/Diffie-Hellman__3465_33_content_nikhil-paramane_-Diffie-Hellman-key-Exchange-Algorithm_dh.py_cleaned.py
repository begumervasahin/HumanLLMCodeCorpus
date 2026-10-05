from random import randint
import math
def is_prime(num, count):
    if num == 1:
        return False
    if count >= num:
        count = num - 1
    for x in range(count):
        a = randint(1, num - 1)
        if pow(a, num-1, num) != 1:
            return False
    return True
def generate_big_prime(n):
    found_prime = False
    while not found_prime:
        p = randint(2**(n-1), 2**n)
        if is_prime(p, 1000):
            return p
prime1=generate_big_prime(2**10)
print("prime 1: ")
print(prime1)
prime2=generate_big_prime(2**10)
print("prime 2: ")
print(prime2)
alice_private_key=randint(2**10, 2**15)
bob_private_key=randint(2**10, 2**15)
a=pow(prime2,alice_private_key,prime1)
b=pow(prime2,bob_private_key,prime1)
alice_key=pow(b,alice_private_key,prime1)
bob_key=pow(a,bob_private_key,prime1)
print("Alice Secret key :")
print(alice_key)
print("Bob Secret key :")
print(bob_key)