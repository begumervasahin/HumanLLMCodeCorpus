def find_all_primes_up_to(limit):
    primes = []
    for number in range(2, limit + 1):
        if is_prime(number):
            primes.append(number)
    return primes
def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True
if __name__ == '__main__':
    primes_up_to_100 = find_all_primes_up_to(100)
    print(primes_up_to_100)