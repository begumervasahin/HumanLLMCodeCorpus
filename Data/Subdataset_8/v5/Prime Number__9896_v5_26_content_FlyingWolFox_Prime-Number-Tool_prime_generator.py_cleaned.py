def find_primes(limit):
    primes = [2]
    for num in range(3, limit + 1, 2):
        is_prime = True
        for prime in primes:
            if prime * prime > num:
                break
            if num % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
            print(num, "is prime")
if __name__ == "__main__":
    limit = 3001
    print("Finding prime numbers up to", limit)
    find_primes(limit)