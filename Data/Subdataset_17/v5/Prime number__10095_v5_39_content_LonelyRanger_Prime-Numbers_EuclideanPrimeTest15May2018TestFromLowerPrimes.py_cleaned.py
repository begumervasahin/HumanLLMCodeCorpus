
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def is_prime(suspect_prime, primes_so_far):
    if suspect_prime < 2:
        return False
    for prime in primes_so_far:
        if prime * prime > suspect_prime:
            break
        if gcd(suspect_prime, prime) != 1:
            return False
    return True
def main():
    primes_so_far = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
    squares_of_primes_so_far = [p * p for p in primes_so_far]
    for suspect_prime in range(59, 2001, 2):
        if all(suspect_prime % p != 0 for p in [3, 5, 7]):
            if is_prime(suspect_prime, primes_so_far):
                print(f"{suspect_prime} is prime")
                primes_so_far.append(suspect_prime)
                squares_of_primes_so_far.append(suspect_prime * suspect_prime)
            else:
                print(f"{suspect_prime} is not prime")
    print("Primes so far:", primes_so_far)
    print("Total primes found:", len(primes_so_far))
    print("Squares of primes so far:", squares_of_primes_so_far)
if __name__ == "__main__":
    main()