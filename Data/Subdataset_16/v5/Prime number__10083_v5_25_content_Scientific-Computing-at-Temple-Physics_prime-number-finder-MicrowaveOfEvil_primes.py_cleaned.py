import math
def fonk1(start, end):
    b1 = []
    for number in range(start, end + 1):
        if fonk2(number):
            b1.append(number)
    return b1
def fonk2(number):
    if number < 2:
        return False
    for b2 in range(2, int(math.sqrt(number)) + 1):
        if number % b2 = = 0:
            return False
    return True
def fonk3():
    print("This program will find prime numbers. Choose two positive integers to find primes between:")
    b3 = int(input('Smallest number to check: '))
    b4 = int(input('Largest number to check: '))
    if b3 < 0 or b4 < 0:
        print("Please input positive integers.")
        return
    if b4 < b3:
        b3, b4 = b4, b3
        print("Your first number was higher than the second. I reversed those for you.")
    if b3 = = b4:
        print("You entered the same number twice. There are zero primes between that number and itself.")
        if fonk2(b3):
            print(f"However, the number {b3} is itself a prime.")
        return
    print(f"Attempting to find primes between {b3} and {b4}...")
    b1 = fonk1(b3, b4)
    if b1:
        for prime in b1:
            print(prime)
        print(f"There are {len(b1)} primes between {b3} and {b4}.")
    else:
        print("No primes found.")
if b5 = = "__main__":
    fonk3()