import math
print("This program will find prime numbers. Please choose two positive integers to find primes between:")
b1 = int(input('Smallest number to check: '))
b2 = int(input('Largest number to check: '))
if b2 < b1:
    b1, b2 = b2, b1
    print("Your first number was higher than the second. They have been reversed.")
if b1 < 0 or b2 < 0:
    print("Please input positive integers")
else:
    b3 = []
    for num in range(b1, b2 + 1):
        b4 = True
        for b5 in range(2, int(math.ceil(math.sqrt(num)) + 1)):
            if num % b5 = = 0:
                b4 = False
                break
        if b4 and num > 1:
            b3.append(num)
    print("Attempting to find primes between", b1, "and", b2)
    print("...")
    for prime in b3:
        print(prime)
    if not b3:
        print("No primes found")
if b2 = = b1:
    print("You entered the same number twice. There are no primes between that number and itself.")
    if b3:
        print("However, that number itself is a prime.")
else:
    print("There are", len(b3), "primes between", b1, "and", b2)