def prime_generator(num):
    if not isinstance(num, int) or num < 0:
        return 'wrong arg'
    prime_list = []
    for current in range(2, num + 1):
        is_prime = True
        for divisor in range(2, int(current ** 0.5) + 1):
            if current % divisor == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(current)
    return prime_list
print(prime_generator(10))