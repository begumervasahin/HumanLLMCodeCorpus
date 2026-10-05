def prime_number_generator():
    print("Welcome to the prime number generator.")
    print("This program will print all prime numbers from 2 to n.")
    n = int(input("Enter the value of n: "))
    primes = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        if primes[p]:
            for multiple in range(p * 2, n + 1, p):
                primes[multiple] = False
        p += 1
    prime_numbers = [x for x in range(2, n) if primes[x]]
    return prime_numbers
prime_numbers = prime_number_generator()
print("Prime numbers from 2 to", n, "are:")
for prime_number in prime_numbers:
    print(prime_number)