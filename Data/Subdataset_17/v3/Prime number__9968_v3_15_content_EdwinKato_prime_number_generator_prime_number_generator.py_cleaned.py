def generate_prime_numbers(n):
    if n < 2:
        return []
    def is_prime(num):
        if num < 2:
            return False
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                return False
        return True
    prime_numbers = [number for number in range(2, n + 1) if is_prime(number)]
    return prime_numbers
print(generate_prime_numbers(10))