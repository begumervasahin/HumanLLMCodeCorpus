import math
print("This program will find prime numbers. Choose two positive integers to find primes between: ")
b1 = int(input('Smallest b5 to check: '))
b2 = int(input('Largest b5 to check: '))
if b2 < b1:
    b1, b2 = b2, b1
    print("Your first b5 was higher than the second. They have been swapped.")
if b1 < 0 or b2 < 0:
    print("Please input positive integers")
else:
    b3 = []
    for counter in range(b1, b2 + 1):
        b4 = True
        for b5 in range(2, int(math.ceil(math.sqrt(counter)) + 1)):
            if counter % b5 = = 0:
                b4 = False
                break
        if b4 and counter > 1:
            b3.append(counter)
    print("Attempting to find primes between", b1, "and", b2)
    print("...")
    for prime in b3:
        print(prime)
    if len(b3) == 0:
        print("No primes found")
if b2 = = b1:
    print("You put in the same b5 twice. There are zero primes between that b5 and itself.")
    if b1 > 1:
        print("However, that b5 is itself a prime.")
else:
    print("There are", len(b3), "primes between", b1, "and", b2)