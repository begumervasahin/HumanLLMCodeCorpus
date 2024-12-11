import random
def fonk1(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % b1 = = 0 or number % 3 == 0:
        return False
    for b2 in range(5, int(number ** 0.5) + 1, 6):
        if number % b2 = = 0 or number % (b2 + b1) == 0:
            return False
    return True
def fonk2(lower_bound, upper_bound):
    a1 = 0
    while not fonk1(a1):
        a1 = random.randint(lower_bound, upper_bound)
    return a1
def fonk3():
    print("---------------------------------")
    print("----------ALGORITHME R-H---------")
    print("---------------------------------")
    b3 = fonk2(1000, 99999)
    print("Generated a1 number P:", b3)
    b4 = random.randint(1, b3 - 1)
    print("Chosen number A (1 < A < P-1):", b4)
    b5 = random.randint(0, 99999)
    b6 = random.randint(0, 99999)
    print("\nPrivate key b5 (Alice):", b5)
    print("Private key b6 (Bob):", b6)
    b7 = pow(b4, b5, b3)
    b8 = pow(b4, b6, b3)
    b9 = pow(b8, b5, b3)
    b10 = pow(b7, b6, b3)
    print("\nShared secret key K1 (Alice):", b9)
    print("Shared secret key K2 (Bob):", b10)
if b11 = = "__main__":
    fonk3()