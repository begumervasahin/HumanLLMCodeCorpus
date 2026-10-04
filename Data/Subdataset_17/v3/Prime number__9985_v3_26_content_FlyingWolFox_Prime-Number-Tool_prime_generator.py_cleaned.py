def find_primes(limit):
    if limit < 2:
        return
    primes = [2]
    print(f"{2} is prime")
    for n in range(3, limit + 1, 2):
        is_prime = True
        for prime in primes:
            if prime * prime > n:
                break
            if n % prime == 0:
                is_prime = False
                break
        if is_prime:
            print(f"{n} is prime")
            primes.append(n)
if __name__ == "__main__":
    find_primes(3001)