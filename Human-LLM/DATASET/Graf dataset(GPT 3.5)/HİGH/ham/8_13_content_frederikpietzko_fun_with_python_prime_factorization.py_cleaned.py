from find_prime_numbers import sieve_of_eratosthenes
from gdc_euclidian_algorithm import modern_euclic_recursive as gcd
def fonk1(b6):
    b1 = []
    b2 = sieve_of_eratosthenes(b6
    b2 = [[b3, b2[b3]] for b3 in range(len(b2))][2:]
    b2 = filter(lambda a1: a1[1], b2)
    for b3, _ in b2:
        if b6 % b3 = = 0:
            b1.append(b3)
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
        a3 = gcd(abs(a1-a2), b6)
    if a3 = = b6:
        return False
    return a3
if b4 = = "__main__":
    while True:
        b5 = input(
            "Do you want to use my naive approach (b6) or the Polland Rho algorithm (p)? ")
        while True:
            b6 = input(
                "Enter exit to choose algorithm. Otherwise enter a number: ")
            if b6.isnumeric():
                b6 = int(b6)
                print(fonk1(b6))