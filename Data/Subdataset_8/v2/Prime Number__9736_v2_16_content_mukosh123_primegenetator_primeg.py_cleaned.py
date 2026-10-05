def generate_primes_up_to(num):
    if not isinstance(num, int) or num < 0:
        return 'Argument must be a non-negative integer'
    prime_list = []
    for i in range(2, num + 1):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(i)
    return prime_list
result = generate_primes_up_to(20)
print(result)