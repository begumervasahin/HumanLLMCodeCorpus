from find_prime_numbers import sieve_of_eratosthenes
from gdc_euclidian_algorithm import modern_euclid_recursive as gcd
def naive_factorization(n):
    factors = []
    sieve = sieve_of_eratosthenes(n
    primes = [i for i in range(2, len(sieve)) if sieve[i]]
    for prime in primes:
        if n % prime == 0:
            factors.append(prime)
    return factors
def g(x, n):
    return (x**2 + 1) % n
def pollard_rho(n):
    x, y, d = 2, 2, 1
    while d == 1:
        x = g(x, n)
        y = g(g(y, n), n)
        d = gcd(abs(x - y), n)
    return d if d != n else None
def main():
    while True:
        alg = input("Choose algorithm - Naive (n) or Pollard Rho (p): ").lower()
        if alg not in ['n', 'p']:
            print("Invalid choice. Please choose 'n' for Naive or 'p' for Pollard Rho.")
            continue
        while True:
            n = input("Enter a number (or type 'exit' to choose algorithm again): ").lower()
            if n == 'exit':
                break
            if n.isnumeric():
                n = int(n)
                if alg == 'n':
                    factors = naive_factorization(n)
                    print(f"Factors of {n} using the naive approach: {factors}")
                elif alg == 'p':
                    factor = pollard_rho(n)
                    if factor:
                        print(f"A non-trivial factor of {n} using the Pollard Rho algorithm: {factor}")
                    else:
                        print(f"Pollard Rho algorithm failed to find a non-trivial factor of {n}")
            else:
                print("Invalid input. Please enter a numeric value.")
if __name__ == "__main__":
    main()