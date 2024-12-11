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
def fonk2(lower_bound, b3):
    a1 = 0
    while not fonk1(a1):
        a1 = random.randint(lower_bound, b3)
    return a1
def fonk3():
    print("---------------------------------\n----------ALGORITHME R-H---------\n---------------------------------\n")
    lower_bound, b3 = 1000, 99999
    b4 = fonk2(lower_bound, b3)
    print("The generated a1 number b5 = ", b4)
    b6 = random.randint(1, b4-1)
    print("The chosen number between 1 and b5-1 is b7 = ", b6)
    b8 = random.randint(1, 99999)
    b9 = random.randint(1, 99999)
    print("\nThe private key x1 chosen by Alice is:", b8)
    print("The private key x2 chosen by Bob is:", b9)
    b10 = pow(b6, b8, b4)
    b11 = pow(b6, b9, b4)
    b12 = pow(b11, b8, b4)
    b13 = pow(b10, b9, b4)
    print("\nThe secret key K1 of Alice is:", b12)
    print("The secret key K2 of Bob is:", b13)
if b14 = = "__main__":
    fonk3()