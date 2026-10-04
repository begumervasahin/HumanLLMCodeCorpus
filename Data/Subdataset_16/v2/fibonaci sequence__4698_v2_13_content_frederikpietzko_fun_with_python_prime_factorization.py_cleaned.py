from find_prime_numbers import sieve_of_eratosthenes
from gdc_euclidian_algorithm import modern_euclid_recursive as gcd
def fonk1(b9):
    b1 = []
    b2 = sieve_of_eratosthenes(b9
    b3 = [i for i in range(2, len(b2)) if b2[i]]
    for b4 in b3:
        if b9 % b4 = = 0:
            b1.append(b4)
    return b1
def fonk2(b6, b9):
    return (b6**2 + 1) % b9
def fonk3(b9):
    b6, b7, b5 = 2, 2, 1
    while b5 = = 1:
        b6 = fonk2(b6, b9)
        b7 = fonk2(fonk2(b7, b9), b9)
        b5 = gcd(abs(b6 - b7), b9)
    return b5 if b5 != b9 else None
def fonk4():
    while True:
        b8 = input("Choose algorithm - Naive (b9) or Pollard Rho (p): ").lower()
        if b8 not in ['b9', 'p']:
            print("Invalid choice. Please choose 'b9' for Naive or 'p' for Pollard Rho.")
            continue
        while True:
            b9 = input("Enter a number (or type 'exit' to choose algorithm again): ").lower()
            if b9 = = 'exit':
                break
            if b9.isnumeric():
                b9 = int(b9)
                if b8 = = 'b9':
                    b1 = fonk1(b9)
                    print(f"Factors of {b9} using the naive approach: {b1}")
                elif b8 = = 'p':
                    b10 = fonk3(b9)
                    if b10:
                        print(f"A non-trivial b10 of {b9} using the Pollard Rho algorithm: {b10}")
                    else:
                        print(f"Pollard Rho algorithm failed to find a non-trivial b10 of {b9}")
            else:
                print("Invalid input. Please enter a numeric value.")
if b11 = = "__main__":
    fonk4()