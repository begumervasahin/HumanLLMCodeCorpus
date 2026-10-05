import math
def sieve_of_eratosthenes(n):
    print("Starting Sieve of Eratosthenes algorithm...")
    primes = []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    with open("Eratosthenes_output.txt", "w") as file:
        for i in range(2, n + 1):
            if sieve[i]:
                primes.append(i)
                print(i)
                file.write(str(i) + "\n")
    print("Finished generating all primes less than or equal to", n)
    return primes
if __name__ == "__main__":
    try:
        n = int(input("Find primes up to: "))
        if n <= 1:
            print("Enter a valid number greater than 1.")
            sys.exit()
    except ValueError:
        print("Enter a valid integer.")
        sys.exit()
    prime_numbers = sieve_of_eratosthenes(n)