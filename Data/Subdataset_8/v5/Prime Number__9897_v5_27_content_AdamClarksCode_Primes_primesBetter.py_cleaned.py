def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0], sieve[1] = False, False
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return [num for num, is_prime in enumerate(sieve) if is_prime]
def optimized_sieve_of_eratosthenes(limit):
    sieve = [True] * (limit
    sieve[0] = False
    for i in range(3, int(limit ** 0.5) + 1, 2):
        if sieve[i
            for j in range(i * i
                sieve[j] = False
    return [2] + [2 * i + 1 for i, is_prime in enumerate(sieve) if is_prime]
if __name__ == "__main__":
    limit = 2000000000
    list_of_primes = optimized_sieve_of_eratosthenes(limit)
    print(f"There are {len(list_of_primes)} primes from 0 to {limit}")