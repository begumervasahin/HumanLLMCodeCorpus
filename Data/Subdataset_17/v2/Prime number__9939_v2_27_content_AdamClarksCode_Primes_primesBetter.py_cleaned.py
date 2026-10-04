def sieve_of_eratosthenes(limit):
    sieve = [True] * limit
    sieve[0] = sieve[1] = False
    for num in range(3, int(limit ** 0.5) + 1, 2):
        if sieve[num]:
            sieve[num * num::2 * num] = [False] * ((limit - num * num - 1)
    return [2] + [num for num in range(3, limit, 2) if sieve[num]]
def optimized_sieve_of_eratosthenes(limit):
    sieve = [True] * (limit
    for num in range(3, int(limit ** 0.5) + 1, 2):
        if sieve[num
            sieve[num * num
    return [2] + [2 * num + 1 for num in range(1, limit
if __name__ == "__main__":
    limit = 2000000000
    list_of_primes = optimized_sieve_of_eratosthenes(limit)
    print(f"There are {len(list_of_primes)} primes from 0 to {limit}")