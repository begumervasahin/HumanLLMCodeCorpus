def sieve_of_eratosthenes(n):
    primes = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    prime_numbers = [p for p in range(2, n + 1) if primes[p]]
    return prime_numbers
def main():
    print("Welcome random tester, this program will print all the prime numbers from 2 to n")
    n = int(input("Enter n: "))
    prime_numbers = sieve_of_eratosthenes(n)
    print("Prime numbers up to", n, "are:")
    for prime in prime_numbers:
        print(prime)
if __name__ == "__main__":
    main()