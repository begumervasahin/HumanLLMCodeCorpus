import math
def mersenne_number(p):
    return (2 ** p) - 1
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True
def get_primes(a, b):
    prime_list = []
    for j in range(a, b):
        if is_prime(j):
            prime_list.append(j)
    return prime_list
def lucas_lehmer(p):
    lucas_lehmer_sequence = [4] * (p - 1)
    for i in range(1, p - 1):
        lucas_lehmer_sequence[i] = (((lucas_lehmer_sequence[i - 1]) ** 2) - 2) % ((2 ** p) - 1)
    return lucas_lehmer_sequence[p - 2] == 0
def is_prime_fast(number):
    if number <= 1:
        return False
    if number % 2 == 0:
        if number > 2:
            return False
    for factor in range(3, int(math.sqrt(number)) + 1, 2):
        if number % factor == 0:
            return False
    return True
def get_primes_fast(n):
    my_list = []
    for number in range(n):
        if is_prime_fast(number):
            my_list.append(number)
    return my_list
def list_true(n):
    my_list = []
    for i in range(n + 1):
        if i <= 1:
            my_list.append(False)
        if i >= 2:
            my_list.append(True)
    return my_list
def mark_false(bool_list, p):
    for i in range(2, len(bool_list)):
        if (p * i) < len(bool_list):
            bool_list[p * i] = False
    return bool_list
def find_next(bool_list, p):
    for i in range(len(bool_list)):
        if bool_list[i] and i > p:
            return i
    return None
def prime_from_list(bool_list):
    index_true = []
    for i in range(len(bool_list)):
        if bool_list[i]:
            index_true.append(i)
    return index_true
def sieve(n):
    bool_list = list_true(n)
    p = 2
    while p is not None:
        bool_list = mark_false(bool_list, p)
        p = find_next(bool_list, p)
    return prime_from_list(bool_list)
assert sieve(1000) == get_primes(0, 1000)