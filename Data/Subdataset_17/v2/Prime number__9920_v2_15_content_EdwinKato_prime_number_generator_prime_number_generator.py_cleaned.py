def generate_prime_numbers(n):
    if n < 2:
        return []
    prime_numbers = []
    for current_number in range(2, n + 1):
        is_prime = True
        for divisor in range(2, int(current_number ** 0.5) + 1):
            if current_number % divisor == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(current_number)
    return prime_numbers
print(generate_prime_numbers(10))