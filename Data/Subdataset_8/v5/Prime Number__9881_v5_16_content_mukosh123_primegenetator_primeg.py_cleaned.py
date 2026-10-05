def generate_prime_numbers_up_to(num):
    if not isinstance(num, int) or num < 0:
        return 'Invalid argument'
    prime_numbers = []
    for candidate in range(2, num + 1):
        is_prime = True
        for divisor in range(2, int(candidate ** 0.5) + 1):
            if candidate % divisor == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(candidate)
    return prime_numbers
prime_numbers_up_to_10 = generate_prime_numbers_up_to(10)
print(prime_numbers_up_to_10)