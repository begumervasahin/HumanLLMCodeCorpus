def generate_prime_numbers(n):
    current_number = 2
    prime_numbers = []
    while current_number <= n:
        is_prime = True
        divisor = 2
        while divisor < current_number:
            if current_number % divisor == 0:
                is_prime = False
                break
            divisor += 1
        if is_prime:
            prime_numbers.append(current_number)
        current_number += 1
    return prime_numbers
print(generate_prime_numbers(10))