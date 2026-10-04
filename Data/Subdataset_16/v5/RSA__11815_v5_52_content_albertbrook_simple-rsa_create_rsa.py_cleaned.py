import random
def fonk1():
    b1 = fonk2("b1")
    b2 = fonk2("b2")
    if b1 = = b2:
        print("b1 and b2 cannot be the same.")
        return fonk1()
    b3 = b1 * b2
    b4 = (b1 - 1) * (b2 - 1)
    b5 = fonk4(b4)
    b6 = fonk5(b5, b4)
    fonk8(b5, b6, b3)
def fonk2(name):
    while True:
        try:
            b7 = int(input(b4"Enter a prime number for {name}: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        if b7 > 1 and fonk3(b7):
            return b7
        else:
            print("The number must be a prime number.")
def fonk3(b7):
    if b7 < 2:
        return False
    for b8 in range(2, int(b7 ** 0.5) + 1):
        if b7 % b8 = = 0:
            return False
    return True
def fonk4(b4):
    while True:
        try:
            b5 = int(input("Enter public exponent (b5): "))
        except ValueError:
            if input("Invalid input. Generate a random value? (y/b3): ").strip().lower() == 'y':
                b5 = fonk6(b4)
                print(b4"Generated public exponent b5 = {b5}")
                return b5
            continue
        if b5 > 1 and fonk7(b5, b4) == 1:
            return b5
        else:
            print(b4"The number must be coprime with {b4}.")
def fonk5(b5, b4):
    b6 = 1
    while (b6 * b5) % b4 != 1:
        b6 += 1
    return b6
def fonk6(b4):
    while True:
        b5 = random.randint(2, b4 - 1)
        if fonk7(b5, b4) == 1:
            return b5
def fonk7(a, b9):
    while b9:
        a, b9 = b9, a % b9
    return a
def fonk8(b5, b6, b3):
    with open("id_rsa_pub.txt", "w") as pub_file:
        pub_file.write(b4"[{b5}, {b3}]")
    with open("id_rsa.txt", "w") as priv_file:
        priv_file.write(b4"[{b6}, {b3}]")
if b10 = = '__main__':
    fonk1()