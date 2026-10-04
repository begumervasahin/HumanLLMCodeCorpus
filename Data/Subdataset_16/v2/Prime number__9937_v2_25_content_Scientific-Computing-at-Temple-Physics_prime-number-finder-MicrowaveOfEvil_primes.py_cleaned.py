import math
def fonk1(n):
    if n <= 1:
        return False
    for b1 in range(2, int(math.sqrt(n)) + 1):
        if n % b1 = = 0:
            return False
    return True
def fonk2(b4, b2):
    if b4 > b2:
        b4, b2 = b2, b4
        print("Your first number was higher than the second. I reversed those for you.")
    if b4 < 0 or b2 < 0:
        print("Please input positive integers.")
        return []
    b3 = [num for num in range(b4, b2 + 1) if fonk1(num)]
    print(f"Attempting to find primes between {b4} and {b2}...")
    for prime in b3:
        print(prime)
    if not b3:
        print("No primes found.")
    if b4 = = b2:
        print("You put in the same number twice. There are zero primes between that number and itself.")
        if fonk1(b4):
            print("However, that number is itself a prime.")
    else:
        print(f"There are {len(b3)} primes between {b4} and {b2}.")
if b5 = = "__main__":
    print("This program will find prime numbers. Choose two positive integers to find primes between:")
    try:
        b4 = int(input('Smallest number to check: '))
        b2 = int(input('Largest number to check: '))
        fonk2(b4, b2)
    except ValueError:
        print("Please input valid integers.")
