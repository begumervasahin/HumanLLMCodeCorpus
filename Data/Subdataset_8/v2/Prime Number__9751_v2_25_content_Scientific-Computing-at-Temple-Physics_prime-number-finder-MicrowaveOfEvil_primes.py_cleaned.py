import math
print("This program will find prime numbers. Choose two positive integers to find primes between: ")
x1 = int(input('Smallest number to check: '))
x2 = int(input('Largest number to check: '))
if x2 < x1:
    x1, x2 = x2, x1
    print("Your first number was higher than the second. They have been swapped.")
if x1 < 0 or x2 < 0:
    print("Please input positive integers")
else:
    primes_list = []
    for number in range(x1, x2 + 1):
        is_prime = True
        for divisor in range(2, int(math.ceil(math.sqrt(number))) + 1):
            if number % divisor == 0:
                is_prime = False
                break
        if is_prime and number > 1:
            primes_list.append(number)
    print("Attempting to find primes between", x1, "and", x2)
    print("...")
    for prime in primes_list:
        print(prime)
    if len(primes_list) == 0:
        print("No primes found")
if x2 == x1:
    print("You put in the same number twice. There are zero primes between that number and itself.")
    if x1 > 1:
        print("However, that number is itself a prime.")
else:
    print("There are", len(primes_list), "primes between", x1, "and", x2)