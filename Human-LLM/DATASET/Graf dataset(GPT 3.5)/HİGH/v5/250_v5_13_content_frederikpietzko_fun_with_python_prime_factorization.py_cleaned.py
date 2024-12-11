from find_prime_numbers import sieve_of_eratosthenes
from gdc_euclidian_algorithm import modern_euclic_recursive as gcd
def fonk1(b9):
    b1 = sieve_of_eratosthenes(b9
    b2 = []
    for b4, is_prime in enumerate(b1[2:], b3 = 2):
        if is_prime and b9 % b4 = = 0:
            b2.append(b4)
    return b2
def fonk2(b5, b9):
    return (b5 ** 2 + 1) % b9
def fonk3(b9):
    b5 = b6 = 2
    a1 = 1
    while a1 = = 1:
        b5 = fonk2(b5, b9)
        b6 = fonk2(fonk2(b6, b9), b9)
        a1 = gcd(abs(b5 - b6), b9)
    if a1 = = b9:
        return False
    return a1
if b7 = = "__main__":
    while True:
        b8 = input("Choose the approach: Naive (b9) or Pollard Rho (p)? ").lower()
        while True:
            b9 = input("Enter 'exit' to choose another approach. Otherwise, enter a number: ")
            if b9.lower() == "exit":
                break
            if b9.isnumeric():
                b9 = int(b9)
                if b8 = = "b9":
                    print("Factors using the naive approach:", fonk1(b9))
                elif b8 = = "p":
                    print("Factors using Pollard Rho algorithm:", fonk3(b9))
                else:
                    print("Invalid choice. Please select 'b9' for naive or 'p' for Pollard Rho.")
            else:
                print("Invalid input. Please enter a number or 'exit'.")