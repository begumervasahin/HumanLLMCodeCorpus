def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True
def all_primes(limit):
    return [num for num in range(2, limit + 1) if is_prime(num)]
if __name__ == '__main__':
    upper_limit = 100
    primes = all_primes(upper_limit)
    print(f"Prime numbers up to {upper_limit}: {primes}")