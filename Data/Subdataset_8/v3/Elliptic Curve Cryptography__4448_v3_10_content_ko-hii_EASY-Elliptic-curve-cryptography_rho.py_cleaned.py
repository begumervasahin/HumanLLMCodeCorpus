from fractions import gcd
from random import randint
def mapping_func(x):
    return x**2 + x + 1
def is_prime(n):
    if n < 2:
        return False
    elif n < 4:
        return True
    x = 1
    x_list = []
    while True:
        x = mapping_func(x) % n
        for past_x in x_list:
            if gcd(x - past_x, n) > 1:
                return False
        x_list.append(x)
        if len(x_list) > 2 and x_list[0] == x_list[2]:
            break
    return gcd(x_list[1] - x_list[0], n) == 1
def generate_prime(length):
    while True:
        candidate = ''.join(str(randint(0, 9)) for _ in range(length - 1))
        candidate = '1' + candidate + str(randint(1, 5) * 2 - 1)
        if candidate[-1] in '02468':
            continue
        if sum(map(int, candidate)) % 3 == 0:
            continue
        if is_prime(int(candidate)):
            break
    return int(candidate)
if __name__ == "__main__":
    prime_length = 10
    prime_number = generate_prime(prime_length)
    print("Generated prime number:", prime_number)