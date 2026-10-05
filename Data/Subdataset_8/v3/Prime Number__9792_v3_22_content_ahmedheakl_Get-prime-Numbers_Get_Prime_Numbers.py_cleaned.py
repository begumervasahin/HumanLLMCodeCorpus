def find_prime_numbers(end_range):
    primes = []
    for i in range(1, int((end_range / 24) ** 0.5) + 1):
        potential_prime = 24 * i + 1
        if is_prime(potential_prime):
            primes.append(potential_prime)
    primes = [num for num in primes if is_prime(num)]
    squared_primes = [num ** 2 for num in primes]
    primes = [prime for prime in primes if prime not in squared_primes]
    initial_primes = [2, 3, 5, 7]
    primes.extend(initial_primes)
    return sorted(primes)
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
if __name__ == "__main__":
    end_range = int(input('Enter the end of the range: '))
    prime_numbers = find_prime_numbers(end_range)
    print(prime_numbers)