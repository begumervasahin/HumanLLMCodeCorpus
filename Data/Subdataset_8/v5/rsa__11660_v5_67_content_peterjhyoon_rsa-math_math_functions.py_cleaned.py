def is_prime(n):
    assert isinstance(n, int), "Input must be an integer"
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
def find_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors
def find_prime_factors(x):
    prime_factors = []
    if is_prime(x):
        prime_factors.append(x)
    for i in find_divisors(x):
        if i == 1:
            continue
        elif is_prime(i):
            prime_factors.append(i)
    return prime_factors
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def are_relatively_prime(a, b):
    return gcd(a, b) == 1
def find_common_factors(a, b):
    a_factors = find_divisors(a)
    b_factors = find_divisors(b)
    common_factors = [elem for elem in a_factors if elem in b_factors]
    return common_factors