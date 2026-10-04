def is_prime(num):
    if num < 2:
        return False
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            return False
    return True
def generate_prime_numbers(n):
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes
print(generate_prime_numbers(10))