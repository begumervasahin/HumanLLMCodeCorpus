def primes(n):
    sieve = [True] * n
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False] * ((n - i*i - 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]
def primes1(n):
    sieve = [True] * (n
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i
            sieve[i*i
    return [2] + [2*i + 1 for i in range(1, n
if __name__ == "__main__":
    limit = 2000000000
    listOfPrimes = primes1(limit)
    print(f"There are {len(listOfPrimes)} primes from 0 to {limit}")