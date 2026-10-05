def generate_prime_numbers(n):
    prime_numbers = []
    for num in range(2, n + 1):
        is_prime = True
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)
    return prime_numbers
prime_numbers_up_to_10 = generate_prime_numbers(10)
print(prime_numbers_up_to_10)