import random
import xgcd
def get_random_prime(min_value, max_value):
    primes = [num for num in range(min_value, max_value) if is_prime(num)]
    return random.choice(primes)
def is_prime(number):
    if number in {0, 1, 4, 6, 8, 9}:
        return False
    if number in {2, 3, 5, 7}:
        return True
    d = number - 1
    s = 0
    while d % 2 == 0:
        d
        s += 1
    def is_composite(a):
        if pow(a, d, number) == 1:
            return False
        for i in range(s):
            if pow(a, 2 ** i * d, number) == number - 1:
                return False
        return True
    for _ in range(8):
        a = random.randrange(2, number)
        if is_composite(a):
            return False
    return True
def are_coprime(a, b):
    if xgcd.GCD(a, b) == 1:
        return True
    else:
        return False
min_value = 10
max_value = 100
random_prime = get_random_prime(min_value, max_value)
print("Random prime number between", min_value, "and", max_value, ":", random_prime)
num1 = 15
num2 = 28
print("Are", num1, "and", num2, "coprime?", are_coprime(num1, num2))