print("Welcome to the prime number generator.")
print("This program will print all prime numbers from 2 to n.")
n = int(input("Enter the value of n: "))
primes = [True for i in range(n + 1)]
p = 2
while p * p <= n:
    if primes[p]:
        for i in range(p * 2, n + 1, p):
            primes[i] = False
    p += 1
print("Prime numbers from 2 to", n, "are:")
for x in range(2, n):
    if primes[x]:
        print(x)