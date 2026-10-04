def prime_generator(num):
    if not isinstance(num, int) or num < 0:
        return 'wrong arg'
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
print(prime_generator(10))