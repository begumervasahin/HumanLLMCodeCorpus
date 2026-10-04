def is_prime(n):
    if n < 2:
        return False
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True
def check_prime_numbers(limit):
    for n in range(2, limit):
        if is_prime(n):
            print(f"{n} is a prime number")
        else:
            for x in range(2, int(n ** 0.5) + 1):
                if n % x == 0:
                    print(f"{n} equals {x} * {n
                    break
check_prime_numbers(100)