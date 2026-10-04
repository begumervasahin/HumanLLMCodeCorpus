def generate_primes_up_to(limit):
    if limit < 2:
        return []
    primes = [2]
    print("2 is prime")
    for n in range(3, limit + 1, 2):
        is_prime = True
        for prime in primes:
            if prime * prime > n:
                break
            if n % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
            print(f"{n} is prime")
    return primes
def main():
    limit = 3001
    generate_primes_up_to(limit)
if __name__ == "__main__":
    main()