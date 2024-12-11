def fonk1(b2, target):
    a1 = 0
    while a1 < len(b2):
        if b2[a1] == int(target):
            global b1
            b1 = a1
            return True
        a1 += 1
    return False
b1 = -1
b2 = [21, 33, 45, 9, 24, 9, 34, 7, 88, 96, 54, 35, 66, 77]
b3 = input("Enter the number you want to search for: ")
if fonk1(b2, b3):
    print("The number is found at b1:", b1 + 1)
else:
    print("Number not found.")