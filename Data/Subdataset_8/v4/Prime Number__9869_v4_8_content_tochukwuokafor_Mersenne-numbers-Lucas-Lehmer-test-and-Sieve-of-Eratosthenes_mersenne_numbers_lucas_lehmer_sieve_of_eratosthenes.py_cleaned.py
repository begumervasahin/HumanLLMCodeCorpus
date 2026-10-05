def mersenne_number(p):
    return (2 ** p) - 1
mersenne_number(5)
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
def get_primes(a, b):
    prime_list = []
    for j in range(a, b):
        if is_prime(j):
            prime_list.append(j)
    return prime_list
primes = get_primes(3, 65)
mersenne_list = [mersenne_number(prime) for prime in primes]
print(mersenne_list)
print(len(mersenne_list))
n_start = 3
n_end = 65
mersennes = []
for number in range(n_start, n_end):
    if is_prime(number):
        mersenne_number = (2 ** number) - 1
        mersennes.append(mersenne_number)
print(mersennes)
print(len(mersennes))
def lucas_lehmer(p):
    lucas_lehmer_sequence = [4] * (p - 1)
    for i in range(1, p - 1):
        lucas_lehmer_sequence[i] = (((lucas_lehmer_sequence[i - 1]) ** 2) - 2) % ((2 ** p) - 1)
    if lucas_lehmer_sequence[p - 2] == 0:
        return 1
    else:
        return 0
my_logic = []
my_primes = get_primes(3, 65)
for idx in my_primes:
    my_logic.append(lucas_lehmer(idx))
print(list(zip(get_primes(3, 65), my_logic)))
import math
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
fast_list = []
for n in range(10000):
    fast_list.append(is_prime_fast(n))
slow_list = []
for n in range(10000):
    slow_list.append(is_prime(n))
slow_list == fast_list
for n in range(10000):
    assert is_prime(n) == is_prime_fast(n)
def get_primes_fast(n):
    my_list = []
    for number in range(n):
        if is_prime_fast(number):
            my_list.append(number)
    return my_list
get_primes_fast(20)
def list_true(n):
    my_list = []
    for i in range(n + 1):
        if i <= 1:
            my_list.append(False)
        if i >= 2:
            my_list.append(True)
    return my_list
list_true(6)
assert len(list_true(20)) == 21
assert list_true(20)[0] is False
assert list_true(20)[1] is False
def mark_false(bool_list, p):
    for i in range(2, len(bool_list)):
        if (p * i) < len(bool_list):
            bool_list[p * i] = False
    return bool_list
assert mark_false(list_true(6), 2) == [False, False, True, True, False, True, False]
def find_next(bool_list, p):
    for i in range(len(bool_list)):
        if (bool_list[i] == True) and i > p:
            return i
    return None
assert find_next([True, True, True, True], 2) == 3
assert find_next([True, True, True, False], 2) is None
def prime_from_list(bool_list):
    index_true = []
    for i in range(len(bool_list)):
        if bool_list[i] == True:
            index_true.append(i)
    return index_true
assert prime_from_list([False, False, True, True, False]) ==  [2, 3]
def sieve(n):
    bool_list = list_true(n)
    p = 2
    while p is not None:
        bool_list = mark_false(bool_list, p)
        p = find_next(bool_list, p)
    return prime_from_list(bool_list)
assert sieve(1000) == get_primes(0, 1000)