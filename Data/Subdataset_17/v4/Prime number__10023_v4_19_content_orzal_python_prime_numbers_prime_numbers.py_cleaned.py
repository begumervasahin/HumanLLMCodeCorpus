def print_prime_numbers(limit):
    for n in range(2, limit):
        for x in range(2, n):
            if n % x == 0:
                print(f"{n} equals {x} * {n
                break
        else:
            print(f"{n} is a prime number")
LIMIT = 100
print_prime_numbers(LIMIT)