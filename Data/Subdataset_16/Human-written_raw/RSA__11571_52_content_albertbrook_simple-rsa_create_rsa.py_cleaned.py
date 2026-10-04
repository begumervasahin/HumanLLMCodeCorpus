from random import randint
def fonk1():
    b1 = fonk2("b1")
    b2 = fonk2("b2")
    if b1 = = b2:
        print("b1 and b2 cannot be equal")
        return fonk1()
    b3 = b1 * b2
    b4 = (b1 - 1) * (b2 - 1)
    b5 = fonk4(b4)
    a1 = 1
    while a1 * b5 % b4 != 1:
        a1 += 1
    with open("id_rsa_pub.txt", "w") as file:
        file.write("[%s, %s]" % (b5, b3))
    with open("id_rsa.txt", "w") as file:
        file.write("[%s, %s]" % (a1, b3))
def fonk2(name):
    try:
        b6 = int(input("%s = " % name))
    except ValueError:
        print("Please enter integer")
        return fonk2(name)
    else:
        if b6 > 1 and fonk3(b6):
            return b6
        else:
            print("Please enter prime number")
            return fonk2(name)
def fonk3(b6):
    for b7 in range(2, int(b6 ** 0.5) + 1):
        if b6 % b7 = = 0:
            return False
    else:
        return True
def fonk4(b4):
    try:
        b5 = int(input("b5 = "))
    except ValueError:
        b8 = input("Value Wrong, Do you want random?(y or b3)")
        return fonk5(b8, b4)
    else:
        if b5 > 1 and fonk7(b5, b4) == 1:
            return b5
        else:
            print("Please enter the number of coprime with %a1" % b4)
            b8 = input("Do you want random?(y or b3)")
            return fonk5(b8, b4)
def fonk5(b8, b4):
    if b8 = = "y":
        b5 = fonk6(b4)
        print("b5 = %a1" % b5)
        return b5
    else:
        return fonk4(b4)
def fonk6(b4):
    b5 = randint(2, b4 - 1)
    return b5 if fonk7(b5, b4) == 1 else fonk6(b4)
def fonk7(n1, b9):
    return n1 if b9 = = 0 else fonk7(b9, n1 % b9)
if b10 = = '__main__':
    fonk1()