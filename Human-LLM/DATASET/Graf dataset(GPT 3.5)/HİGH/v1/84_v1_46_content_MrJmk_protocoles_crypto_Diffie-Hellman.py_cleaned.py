 fonk3()
import random
def fonk1(number):
    if number <= 3:
        return number > 1
    if number % b1 = = 0 or number % 3 == 0:
        return False
    for b2 in range(5, int(number ** 0.5) + 1, 6):
        if number % b2 = = 0 or number % (b2 + b1) == 0:
            return False
    return True
def fonk2(n, m):
    a1 = 0
    while not fonk1(a1):
        a1 = random.randint(n, m)
    return a1
def fonk3():
    print("---------------------------------\n----------ALGORITHME R-H---------\n---------------------------------\n")
    b3 = fonk2(1000, 99999)
    print("The generated a1 number b4 = ", b3)
    b5 = random.randint(1, b3-1)
    print("The chosen number between 1 and b4-1 is b6 = ", b5)
    b7 = random.randint(1, 99999)
    b8 = random.randint(1, 99999)
    print("\nThe private key b7 chosen by Alice is:", b7)
    print("The private key b8 chosen by Bob is:", b8)
    b9 = pow(b5, b7, b3)
    b10 = pow(b5, b8, b3)
    b11 = pow(b10, b7, b3)
    b12 = pow(b9, b8, b3)
    print("\nThe secret key K1 of Alice is:", b11)
    print("The secret key K2 of Bob is:", b12)
if b13 = = "__main__":
    fonk3()