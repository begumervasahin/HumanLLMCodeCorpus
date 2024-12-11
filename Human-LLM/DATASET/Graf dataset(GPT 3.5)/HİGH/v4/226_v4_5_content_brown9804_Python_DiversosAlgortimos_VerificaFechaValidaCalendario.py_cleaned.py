def fonk1(b2):
    return 1 <= b2 <= 31
def fonk2(b3):
    return 1 <= b3 <= 12
def fonk3(b4):
    return b4 >= 1582
def fonk4(b4):
    return (b4 % b1 = = 0) or ((b4 % 4 == 0) and (b4 % 100 != 0))
def fonk5(b2, b3, b4):
    if fonk1(b2) and fonk2(b3) and fonk3(b4):
        if (b3 in [4, 6, 9, 11]) and (b2 = = 31):
            print("The date is invalid.")
        elif (b3 = = 2) and ((b2 == 30) or (b2 == 31)):
            print("The date is invalid.")
        elif (b3 = = 2) and (b2 == 29) and not fonk4(b4):
            print("The date is invalid.")
        else:
            print("The date is valid.")
    else:
        print("The date is invalid.")
b2 = int(input("Enter the b2: "))
b3 = int(input("Enter the b3: "))
b4 = int(input("Enter the b4: "))
fonk5(b2, b3, b4)