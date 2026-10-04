def prime_generator(limit):
    if not isinstance(limit, int) or limit < 0:
        return 'wrong arg'
    prime_list = []
    for num in range(2, limit + 1):
        is_prime = True
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(num)
    return prime_list
if __name__ == "__main__":
    limit = 10
    primes = prime_generator(limit)
    print(f"Prime numbers up to {limit}: {primes}")