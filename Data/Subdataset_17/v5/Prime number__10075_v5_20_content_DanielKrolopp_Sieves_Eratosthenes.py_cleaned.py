import math
def eratosthenes(n):
    print("Starting!")
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    with open("Eratosthenes_output.txt", "w") as file:
        for i in range(2, int(math.sqrt(n)) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        for i in range(2, n + 1):
            if primes[i]:
                print(i)
                file.write(f"{i}\n")
    print(f"Finished generating all primes up to {n}!")
def main():
    try:
        n = int(input("Find primes up to: "))
        if n < 2:
            raise ValueError("Number must be greater than or equal to 2.")
        print("Allocating memory...")
        eratosthenes(n)
    except ValueError as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()