from fractions import gcd
from random import randint
def mapping_func(x):
    return pow(x, 2) + x + 1
def is_prime(n):
    if n < 2:
        return False
    elif n < 4:
        return True
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
    return result == n
def generate_prime(length):
    while True:
        n = str(randint(1, 9))
        for i in range(length - 2):
            n += str(randint(0, 9))
        n += str(randint(1, 5) * 2 - 1)
        if n[length - 1] == '5':
            continue
        if sum(int(digit) for digit in n) % 3 == 0:
            continue
        if is_prime(int(n)):
            break
    return int(n)
if __name__ == "__main__":
    prime_length = 10
    prime_number = generate_prime(prime_length)
    print("Generated prime number:", prime_number)