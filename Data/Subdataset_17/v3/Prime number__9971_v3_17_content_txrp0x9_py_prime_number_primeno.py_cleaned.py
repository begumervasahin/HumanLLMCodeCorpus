def sieve_of_eratosthenes(n):
    if n < 2:
        return []
    primes = [True] * (n + 1)
    primes[0], primes[1] = False, False
    p = 2
    while p * p <= n:
        if primes[p]:
            for multiple in range(p * p, n + 1, p):
                primes[multiple] = False
        p += 1
    prime_numbers = [num for num in range(2, n + 1) if primes[num]]
    return prime_numbers
def main():
    print("Welcome random tester, this program will print all the prime numbers from 2 to n")
    try:
        n = int(input("Enter n: "))
        if n < 2:
            print("There are no prime numbers less than 2.")
        else:
            prime_numbers = sieve_of_eratosthenes(n)
            print(f"Prime numbers up to {n} are: {prime_numbers}")
    except ValueError:
        print("Invalid input. Please enter an integer.")
if __name__ == "__main__":
    main()