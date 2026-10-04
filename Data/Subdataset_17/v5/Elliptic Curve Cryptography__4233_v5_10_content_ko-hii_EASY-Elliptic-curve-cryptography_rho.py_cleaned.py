from math import gcd
from random import randint
def mapping_func(x):
    return x**2 + x + 1
def is_composite_rho(n):
    if n < 2:
        return True
    elif n < 4:
        return False
    x = 1
    x_list = []
    result = 1
    while result == 1:
        x = mapping_func(x) % n
        for past_x in x_list:
            result = gcd(x - past_x, n)
            if result > 1:
                break
        x_list.append(x)
    return result != n
def generate_prime(length):
    while True:
        n = str(randint(1, 9))
        for _ in range(length - 2):
            n += str(randint(0, 9))
        n += str(randint(1, 5) * 2 - 1)
        if n[-1] == '5':
            continue
        if sum(int(digit) for digit in n) % 3 == 0:
            continue
        if not is_composite_rho(int(n)):
            return int(n)
if __name__ == "__main__":
    prime_length = 10
    prime_number = generate_prime(prime_length)
    print(f"Generated prime number of length {prime_length}: {prime_number}")