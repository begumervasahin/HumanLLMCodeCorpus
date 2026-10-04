from fractions import gcd
from random import randint
def mapping_func(x):
    return pow(x, 2) + x + 1
def rho(n):
    if n < 2:
        return False
    elif n < 4:
        return True
    x = 1
    x_list = list()
    result = 1
    while result == 1:
        x = mapping_func(x) % n
        for past_x in x_list:
            result = gcd(x-past_x, n)
            if result > 1:
                break
        x_list.append(x)
    if result == n:
        return True
    else:
        return False
def get_prime(length):
    while True:
        n = str(randint(1, 9))
        for i in range(length-2):
            n += str(randint(0, 9))
        n += str(randint(1, 5) * 2 - 1)
        if n[length-1] == '5':
            continue
        if sum([int(i) for i in n]) % 3 == 0:
            continue
        if rho(int(n)):
            break
    return int(n)