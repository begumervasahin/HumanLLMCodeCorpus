import random
def is_prime(n):
    if not isinstance(n, int) or n < 2:
        return False
    if n in (2, 3, 5, 7):
        return True
    if n % 2 == 0:
        return False
    s = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1
        s += 1
    assert 2**s * d == n - 1
    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n - 1:
                return False
        return True
    for _ in range(8):
        a = random.randrange(2, n)
        if trial_composite(a):
            return False
    return True
if __name__ == '__main__':
    test_numbers = [
        2, 3, 5, 7, 9, 15, 17, 19, 23, 29, 35, 37, 41, 43, 47, 49, 51, 53,
        57, 59, 61, 67, 69, 71, 73, 79, 83, 89, 97
    ]
    for number in test_numbers:
        result = is_prime(number)
        status = 'a prime number' if result else 'not a prime number'
        print(f"{number} is {status}")