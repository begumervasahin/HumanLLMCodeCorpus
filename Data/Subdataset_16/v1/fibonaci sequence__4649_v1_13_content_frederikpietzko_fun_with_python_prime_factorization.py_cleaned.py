from find_prime_numbers import sieve_of_eratosthenes
from gdc_euclidian_algorithm import modern_euclid_recursive as gcd
def fonk1(b6):
    b1 = []
    b2 = sieve_of_eratosthenes(b6
    b3 = [i for i in range(2, len(b2)) if b2[i]]
    for b4 in b3:
        if b6 % b4 = = 0:
            b1.append(b4)
    return b1
def fonk2(a1, b6):
    return (a1**2 + 1) % b6
def fonk3(b6):
    a1 = 2
    a2 = 2
    a3 = 1
    while a3 = = 1:
        a1 = fonk2(a1, b6)
        a2 = fonk2(fonk2(a2, b6), b6)
        a3 = gcd(abs(a1 - a2), b6)
    if a3 = = b6:
        return False
    return a3
def fonk4():
    while True:
        b5 = input("Do you want to use my naive approach (b6) or the Pollard Rho algorithm (p)? ").lower()
        while True:
            b6 = input("Enter a number (or type 'exit' to choose algorithm again): ").lower()
            if b6 = = 'exit':
                break
            if b6.isnumeric():
                b6 = int(b6)
                if b5 = = 'b6':
                    b1 = fonk1(b6)
                    print(f"Factors of {b6} using the naive approach: {b1}")
                elif b5 = = 'p':
                    b7 = fonk3(b6)
                    if b7:
                        print(f"A non-trivial b7 of {b6} using the Pollard Rho algorithm: {b7}")
                    else:
                        print(f"Pollard Rho algorithm failed to find a non-trivial b7 of {b6}")
                else:
                    print("Invalid algorithm choice. Please choose 'b6' for naive or 'p' for Pollard Rho.")
            else:
                print("Invalid input. Please enter a numeric value.")
if b8 = = "__main__":
    fonk4()