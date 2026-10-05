def is_prime(n, primes):
    for prime in primes:
        if prime * prime > n:
            break
        if n % prime == 0:
            return False
    return True
def find_primes(limit):
    primes = [2]
    for n in range(3, limit + 1, 2):
        if is_prime(n, primes):
            primes.append(n)
    return primes
def main():
    limit = 3001
    primes = find_primes(limit)
    for prime in primes:
        print(prime, "is prime")
if __name__ == "__main__":
    main()