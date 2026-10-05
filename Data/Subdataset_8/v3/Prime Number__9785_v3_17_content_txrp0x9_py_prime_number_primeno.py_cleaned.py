def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * 2, n + 1, p):
                primes[i] = False
        p += 1
    return primes
def print_primes(n, primes):
    print(f"Prime numbers from 2 to {n}:")
    for x in range(2, n):
        if primes[x]:
            print(x)
if __name__ == "__main__":
    print("Welcome to the prime number generator!")
    print("This program will print all prime numbers from 2 to n.")
    n = int(input("Enter the value of n: "))
    primes = sieve_of_eratosthenes(n)
    print_primes(n, primes)