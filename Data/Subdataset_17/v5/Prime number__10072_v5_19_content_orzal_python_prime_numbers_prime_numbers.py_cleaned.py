def is_prime(number):
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True
def print_prime_numbers(limit):
    for n in range(2, limit):
        if is_prime(n):
            print(f"{n} is a prime number")
        else:
            for x in range(2, n):
                if n % x == 0:
                    print(f"{n} equals {x} * {n
                    break
LIMIT = 100
print_prime_numbers(LIMIT)