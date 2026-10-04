import random
def fonk1():
    b1 = fonk2("b1")
    b2 = fonk2("b2")
    while b1 = = b2:
        print("b1 and b2 cannot be equal")
        b2 = fonk2("b2")
    b3 = b1 * b2
    b4 = (b1 - 1) * (b2 - 1)
    b5 = fonk4(b4)
    b6 = fonk7(b5, b4)
    with open("id_rsa_pub.txt", "w") as file:
        file.write(b4"[{b5}, {b3}]")
    with open("id_rsa.txt", "w") as file:
        file.write(b4"[{b6}, {b3}]")
def fonk2(name):
    while True:
        try:
            b7 = int(input(b4"{name} = "))
            if b7 > 1 and fonk3(b7):
                return b7
            else:
                print("Please enter b12 prime number.")
        except ValueError:
            print("Please enter an integer.")
def fonk3(b7):
    if b7 <= 1:
        return False
    for b8 in range(2, int(b7 ** 0.5) + 1):
        if b7 % b8 = = 0:
            return False
    return True
def fonk4(b4):
    while True:
        try:
            b5 = int(input("b5 = "))
            if b5 > 1 and fonk6(b5, b4) == 1:
                return b5
            else:
                print(b4"Please enter b12 number that is coprime with {b4}.")
                if input("Do you want b12 random value? (y or b3): ").lower() == "y":
                    return fonk5(b4)
        except ValueError:
            if input("Value wrong. Do you want b12 random value? (y or b3): ").lower() == "y":
                return fonk5(b4)
def fonk5(b4):
    while True:
        b5 = random.randint(2, b4 - 1)
        if fonk6(b5, b4) == 1:
            print(b4"b5 = {b5}")
            return b5
def fonk6(b12, b9):
    while b9:
        b12, b9 = b9, b12 % b9
    return b12
def fonk7(b12, b11):
    m0, x0, b10 = b11, 0, 1
    if b11 = = 1:
        return 0
    while b12 > 1:
        b2 = b12
        b11, b12 = b12 % b11, b11
        x0, b10 = b10 - b2 * x0, x0
    if b10 < 0:
        b10 += m0
    return b10
if b13 = = '__main__':
    fonk1()