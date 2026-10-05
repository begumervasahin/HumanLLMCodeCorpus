def is_prime(n):
    assert type(n) == int
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
def divisor(n):
    lst = []
    for i in range(1, n + 1):
        if n % i == 0:
            lst.append(i)
    return lst
def prime_factor(x):
    fact_lst = []
    if is_prime(x):
        fact_lst.append(x)
    for i in divisor(x):
        if i == 1:
            pass
        elif is_prime(i):
            fact_lst.append(i)
    return fact_lst
def gcd(a, b):
    if b > a:
        return gcd(b, a)
    elif a % b == 0:
        return b
    return gcd(b, a % b)
def relatively_prime(a, b):
    while a > 0 and b > 0:
        if gcd(a, b) == 1:
            return True
        else:
            return False
def common_factor(a, b):
    a_fact = divisor(a)
    b_fact = divisor(b)
    common_fact = []
    for elem in a_fact:
        if elem in b_fact:
            common_fact.append(elem)
    return common_fact