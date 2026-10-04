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
    return [j for j in range(a, b) if is_prime(j)]
def lucas_lehmer(p):
    lucas_lehmer_sequence = [4] * (p - 1)
    for i in range(1, p - 1):
        lucas_lehmer_sequence[i] = (((lucas_lehmer_sequence[i - 1]) ** 2) - 2) % ((2 ** p) - 1)
    return lucas_lehmer_sequence
def lucas_lehmer_prime(p):
    lucas_lehmer_sequence = lucas_lehmer(p)
    return lucas_lehmer_sequence[-1] == 0
def is_prime_fast(number):
    if number <= 1:
        return False
    if number % 2 == 0:
        return number == 2
    for factor in range(3, int(math.sqrt(number)) + 1, 2):
        if number % factor == 0:
            return False
    return True
def get_primes_fast(n):
    return [number for number in range(n) if is_prime_fast(number)]
def list_true(n):
    return [False, False] + [True] * (n - 1)
def mark_false(bool_list, p):
    for i in range(2, len(bool_list)):
        if p * i < len(bool_list):
            bool_list[p * i] = False
    return bool_list
def find_next(bool_list, p):
    for i in range(p + 1, len(bool_list)):
        if bool_list[i]:
            return i
    return None
def prime_from_list(bool_list):
    return [i for i, is_prime in enumerate(bool_list) if is_prime]
def sieve(n):
    bool_list = list_true(n)
    p = 2
    while p is not None:
        bool_list = mark_false(bool_list, p)
        p = find_next(bool_list, p)
    return prime_from_list(bool_list)
if __name__ == '__main__':
    primes = get_primes(3, 65)
    mersenne_list = [mersenne_number(prime) for prime in primes]
    print("Mersenne numbers:", mersenne_list)
    print("Number of Mersenne numbers:", len(mersenne_list))
    mersennes = [mersenne_number(prime) for prime in get_primes(3, 65)]
    print("Checked Mersenne numbers:", mersennes)
    print("Number of checked Mersenne numbers:", len(mersennes))
    my_primes = get_primes(3, 65)
    my_logic = [lucas_lehmer_prime(p) for p in my_primes]
    print("Lucas-Lehmer test results:", list(zip(my_primes, my_logic)))
    fast_list = [is_prime_fast(n) for n in range(10000)]
    slow_list = [is_prime(n) for n in range(10000)]
    print("Fast and slow prime lists are identical:", slow_list == fast_list)
    fast_primes = get_primes_fast(20)
    print("Primes up to 20:", fast_primes)
    assert len(list_true(20)) == 21
    assert list_true(20)[0] is False
    assert list_true(20)[1] is False
    assert mark_false(list_true(6), 2) == [False, False, True, True, False, True, False]
    assert find_next([True, True, True, True], 2) == 3
    assert find_next([True, True, True, False], 2) is None
    assert prime_from_list([False, False, True, True, False]) == [2, 3]
    assert sieve(1000) == get_primes(0, 1000)
    print("All assertions passed successfully.")