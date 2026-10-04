from find_prime_numbers import sieve_of_eratosthenes
from gdc_euclidian_algorithm import modern_euclid_recursive as gcd
def fonk1(b10):
    b1 = []
    b2 = sieve_of_eratosthenes(b10
    b3 = [i for i in range(2, len(b2)) if b2[i]]
    for b4 in b3:
        if b10 % b4 = = 0:
            b1.append(b4)
    return b1
def fonk2(b6, b10):
    return (b6**2 + 1) % b10
def fonk3(b10):
    b6, b7, b5 = 2, 2, 1
    while b5 = = 1:
        b6 = fonk2(b6, b10)
        b7 = fonk2(fonk2(b7, b10), b10)
        b5 = gcd(abs(b6 - b7), b10)
    return b5 if b5 != b10 else None
def fonk4():
    while True:
        b8 = input("Choose algorithm - Naive (b10) or Pollard Rho (p): ").lower()
        if b8 in ['b10', 'p']:
            return b8
        print("Invalid choice. Please choose 'b10' for Naive or 'p' for Pollard Rho.")
def fonk5(prompt):
    while True:
        b9 = input(prompt)
        if b9.isnumeric():
            return int(b9)
        print("Invalid input. Please enter a numeric value.")
def fonk6():
    while True:
        b8 = fonk4()
        while True:
            b10 = input("Enter a number (or type 'exit' to choose algorithm again): ").lower()
            if b10 = = 'exit':
                break
            if b10.isnumeric():
                b10 = int(b10)
                if b8 = = 'b10':
                    b1 = fonk1(b10)
                    print(f"Factors of {b10} using the naive approach: {b1}")
                elif b8 = = 'p':
                    b11 = fonk3(b10)
                    if b11:
                        print(f"A non-trivial b11 of {b10} using the Pollard Rho algorithm: {b11}")
                    else:
                        print(f"Pollard Rho algorithm failed to find a non-trivial b11 of {b10}")
            else:
                print("Invalid input. Please enter a numeric value.")
if b12 = = "__main__":
    fonk6()