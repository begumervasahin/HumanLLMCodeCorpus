from find_prime_numbers import sieve_of_eratosthenes
from gdc_euclidian_algorithm import modern_euclic_recursive as gcd
def fonk1(b7):
    b1 = sieve_of_eratosthenes(b7
    b2 = []
    for b3 in b1[2:]:
        if b7 % b3 = = 0:
            b2.append(b3)
    return b2
def fonk2(a1, b7):
    return (a1 ** 2 + 1) % b7
def fonk3(b7):
    a1 = 2
    a2 = 2
    a3 = 1
    while a3 = = 1:
        a1 = fonk2(a1, b7)
        a2 = fonk2(fonk2(a2, b7), b7)
        a3 = gcd(abs(a1 - a2), b7)
    if a3 = = b7:
        return False
    return a3
if b4 = = "__main__":
    while True:
        b5 = input("Choose the approach: Naive (b7) or Pollard Rho (p)? ")
        while True:
            b6 = input("Enter 'exit' to choose another approach. Otherwise, enter a number: ")
            if b6.lower() == "exit":
                break
            if b6.isnumeric():
                b7 = int(b6)
                if b5.lower() == "b7":
                    print("Factors using the naive approach:", fonk1(b7))
                elif b5.lower() == "p":
                    print("Factors using the Pollard Rho algorithm:", fonk3(b7))
                else:
                    print("Invalid choice. Please select 'b7' for naive or 'p' for Pollard Rho.")
            else:
                print("Invalid input. Please enter a number or 'exit'.")