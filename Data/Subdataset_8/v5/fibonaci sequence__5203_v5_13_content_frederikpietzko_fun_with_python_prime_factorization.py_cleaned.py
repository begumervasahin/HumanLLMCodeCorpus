from find_prime_numbers import sieve_of_eratosthenes
from gdc_euclidian_algorithm import modern_euclic_recursive as gcd
def naive_factorization(n):
    primes = sieve_of_eratosthenes(n
    factors = []
    for i, is_prime in enumerate(primes[2:], start=2):
        if is_prime and n % i == 0:
            factors.append(i)
    return factors
def g(x, n):
    return (x ** 2 + 1) % n
def pollard_rho(n):
    x = y = 2
    d = 1
    while d == 1:
        x = g(x, n)
        y = g(g(y, n), n)
        d = gcd(abs(x - y), n)
    if d == n:
        return False
    return d
if __name__ == "__main__":
    while True:
        algorithm_choice = input("Choose the approach: Naive (n) or Pollard Rho (p)? ").lower()
        while True:
            n = input("Enter 'exit' to choose another approach. Otherwise, enter a number: ")
            if n.lower() == "exit":
                break
            if n.isnumeric():
                n = int(n)
                if algorithm_choice == "n":
                    print("Factors using the naive approach:", naive_factorization(n))
                elif algorithm_choice == "p":
                    print("Factors using Pollard Rho algorithm:", pollard_rho(n))
                else:
                    print("Invalid choice. Please select 'n' for naive or 'p' for Pollard Rho.")
            else:
                print("Invalid input. Please enter a number or 'exit'.")