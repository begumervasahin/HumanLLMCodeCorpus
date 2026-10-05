import math
def find_primes():
    print("This program will find prime numbers. Please choose two positive integers to find primes between:")
    x1 = int(input('Smallest number to check: '))
    x2 = int(input('Largest number to check: '))
    if x2 < x1:
        x1, x2 = x2, x1
        print("Your first number was higher than the second. They have been reversed.")
    if x1 < 0 or x2 < 0:
        print("Please input positive integers")
        return
    primes_list = []
    for num in range(x1, x2 + 1):
        is_prime = True
        for i in range(2, int(math.ceil(math.sqrt(num)) + 1)):
            if num % i == 0:
                is_prime = False
                break
        if is_prime and num > 1:
            primes_list.append(num)
    print("Attempting to find primes between", x1, "and", x2)
    print("...")
    if primes_list:
        for prime in primes_list:
            print(prime)
    else:
        print("No primes found")
    if x2 == x1:
        print("You entered the same number twice. There are no primes between that number and itself.")
        if primes_list:
            print("However, that number itself is a prime.")
    else:
        print("There are", len(primes_list), "primes between", x1, "and", x2)
if __name__ == "__main__":
    find_primes()