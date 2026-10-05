def generate_prime_numbers(n):
    prime_numbers = []
    for j in range(2, n + 1):
        is_prime = True
        for k in range(2, j):
            if j % k == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(j)
    return prime_numbers
generate_prime_numbers(10)