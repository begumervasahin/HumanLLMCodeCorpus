def generate_prime_numbers(n):
    primes = []
    for number in range(2, n + 1):
        if is_prime(number):
            primes.append(number)
    return primes
def is_prime(number):
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True
result = generate_prime_numbers(10)
print(result)