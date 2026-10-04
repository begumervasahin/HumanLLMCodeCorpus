from find_prime_numbers import sieve_of_eratosthenes
from gdc_euclidian_algorithm import modern_euclid_recursive as gcd
def fonk1(b11):
    b1 = []
    b2 = sieve_of_eratosthenes(b11
    b3 = [i for i in range(2, len(b2)) if b2[i]]
    for b4 in b3:
        if b11 % b4 = = 0:
            b1.append(b4)
    return b1
def fonk2(b6, b11):
    return (b6**2 + 1) % b11
def fonk3(b11):
    b6, b7, b5 = 2, 2, 1
    while b5 = = 1:
        b6 = fonk2(b6, b11)
        b7 = fonk2(fonk2(b7, b11), b11)
        b5 = gcd(abs(b6 - b7), b11)
    return b5 if b5 != b11 else None
def fonk4():
    while True:
        b8 = input("Choose algorithm - Naive (b11) or Pollard Rho (p): ").lower()
        if b8 in ['b11', 'p']:
            return b8
        print("Invalid choice. Please choose 'b11' for Naive or 'p' for Pollard Rho.")
def fonk5(prompt):
    while True:
        b9 = input(prompt)
        if b9.isnumeric():
            return int(b9)
        print("Invalid input. Please enter a numeric value.")
def fonk6(b8, b11):
    if b8 = = 'b11':
        b1 = fonk1(b11)
        print(f"Factors of {b11} using the naive approach: {b1}")
    elif b8 = = 'p':
        b10 = fonk3(b11)
        if b10:
            print(f"A non-trivial b10 of {b11} using the Pollard Rho algorithm: {b10}")
        else:
            print(f"Pollard Rho algorithm failed to find a non-trivial b10 of {b11}")
def fonk7():
    while True:
        b8 = fonk4()
        while True:
            b11 = input("Enter a number (or type 'exit' to choose algorithm again): ").lower()
            if b11 = = 'exit':
                break
            if b11.isnumeric():
                b11 = int(b11)
                fonk6(b8, b11)
            else:
                print("Invalid input. Please enter a numeric value.")
if b12 = = "__main__":
    fonk7()