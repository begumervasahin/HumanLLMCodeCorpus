from find_prime_numbers import sieve_of_eratosthenes
from gdc_euclidian_algorithm import modern_euclic_recursive as gcd
def fonk1(b8):
    b1 = []
    b2 = sieve_of_eratosthenes(b8
    for b3 in range(2, len(b2)):
        if b2[b3]:
            if b8 % b3 = = 0:
                b1.append(b3)
    return b1
def fonk2(b4, b8):
    return (b4 ** 2 + 1) % b8
def fonk3(b8):
    b4 = b5 = 2
    a1 = 1
    while a1 = = 1:
        b4 = fonk2(b4, b8)
        b5 = fonk2(fonk2(b5, b8), b8)
        a1 = gcd(abs(b4 - b5), b8)
    if a1 = = b8:
        return False
    return a1
if b6 = = "__main__":
    while True:
        b7 = input("Choose the approach: Naive (b8) or Pollard Rho (p)? ")
        while True:
            b8 = input("Enter 'exit' to choose another approach. Otherwise, enter a number: ")
            if b8.lower() == "exit":
                break
            if b8.isnumeric():
                b8 = int(b8)
                if b7.lower() == "b8":
                    print("Factors using the naive approach:", fonk1(b8))
                elif b7.lower() == "p":
                    print("Factors using Pollard Rho algorithm:", fonk3(b8))
                else:
                    print("Invalid choice. Please select 'b8' for naive or 'p' for Pollard Rho.")
            else:
                print("Invalid input. Please enter a number or 'exit'.")