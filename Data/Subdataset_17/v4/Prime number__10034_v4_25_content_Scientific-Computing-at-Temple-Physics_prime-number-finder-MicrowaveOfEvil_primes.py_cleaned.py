import math
def get_prime_numbers_in_range(start, end):
    primes_list = []
    for number in range(start, end + 1):
        if is_prime(number):
            primes_list.append(number)
    return primes_list
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True
def main():
    print("This program will find prime numbers. Choose two positive integers to find primes between:")
    x1 = int(input('Smallest number to check: '))
    x2 = int(input('Largest number to check: '))
    if x2 < x1:
        x1, x2 = x2, x1
        print("Your first number was higher than the second. I reversed those for you.")
    if x1 < 0 or x2 < 0:
        print("Please input positive integers.")
        return
    if x2 == x1:
        print("You entered the same number twice. There are zero primes between that number and itself.")
        if is_prime(x1):
            print(f"However, the number {x1} is itself a prime.")
        return
    primes_list = get_prime_numbers_in_range(x1, x2)
    print(f"Attempting to find primes between {x1} and {x2}...")
    if primes_list:
        for prime in primes_list:
            print(prime)
        print(f"There are {len(primes_list)} primes between {x1} and {x2}.")
    else:
        print("No primes found.")
if __name__ == "__main__":
    main()