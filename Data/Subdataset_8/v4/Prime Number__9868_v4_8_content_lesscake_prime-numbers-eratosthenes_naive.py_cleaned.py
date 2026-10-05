def find_all_primes_up_to(n):
    primes = []
    for number in range(0, n + 1):
        if is_prime(number):
            primes.append(number)
    return primes
def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True
if __name__ == '__main__':
    print(find_all_primes_up_to(100))