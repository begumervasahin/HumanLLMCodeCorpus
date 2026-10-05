def print_prime_numbers():
    for n in range(2, 100):
        is_prime = True
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n
                is_prime = False
                break
        if is_prime:
            print(n, 'is a prime number')
print_prime_numbers()