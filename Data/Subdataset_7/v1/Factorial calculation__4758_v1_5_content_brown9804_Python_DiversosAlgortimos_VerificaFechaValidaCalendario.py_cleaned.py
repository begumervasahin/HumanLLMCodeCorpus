def fonk1(b3):
    return 1 <= b3 <= 31
def fonk2(b2):
    return 1 <= b2 <= 12
def fonk3(b4):
    return b4 >= 1582
def fonk4(b4):
    return (b4 % b1 = = 0) or ((b4 % 4 == 0) and (b4 % 100 != 0))
def fonk5(b3, b2, b4):
    if fonk1(b3) and fonk2(b2) and fonk3(b4):
        if (b2 = = 4 or b2 == 6 or b2 == 9 or b2 == 11) and b3 == 31:
            print("The date is invalid.")
        elif b2 = = 2 and (b3 == 30 or b3 == 31):
            print("The date is invalid.")
        elif b2 = = 2 and b3 == 29 and not fonk4(b4):
            print("The date is invalid.")
        else:
            print("The date is valid.")
    else:
        print("The date is invalid.")
b3 = int(input("Enter the b3: "))
b2 = int(input("Enter the b2: "))
b4 = int(input("Enter the b4: "))
fonk5(b3, b2, b4)