import math
def fonk1():
    print("This program will find prime numbers. Choose two positive integers to find primes between: ")
    b1 = int(input('Smallest number to check: '))
    b2 = int(input('Largest number to check: '))
    return min(b1, b2), max(b1, b2)
def fonk2(number):
    if number < 2:
        return False
    for b3 in range(2, int(math.sqrt(number)) + 1):
        if number % b3 = = 0:
            return False
    return True
def fonk3(b1, b2):
    b4 = [number for number in range(b1, b2 + 1) if fonk2(number)]
    return b4
def fonk4(b4, b1, b2):
    print(f"Attempting to find primes between {b1} and {b2}...")
    if b4:
        for prime in b4:
            print(prime)
    else:
        print("No primes found")
def fonk5():
    b1, b2 = fonk1()
    b4 = fonk3(b1, b2)
    fonk4(b4, b1, b2)
    if b1 = = b2:
        print("You put in the same number twice. There are zero primes between that number and itself.")
        if b1 > 1:
            print("However, that number is itself a prime.")
    else:
        print(f"There are {len(b4)} primes between {b1} and {b2}")
if b5 = = '__main__':
    fonk5()