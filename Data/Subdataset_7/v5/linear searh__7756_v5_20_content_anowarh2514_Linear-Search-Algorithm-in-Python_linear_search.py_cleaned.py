def fonk1(lst, target):
    for index, b1 in enumerate(lst):
        if b1 = = int(target):
            global b2
            b2 = index
            return True
    return False
b2 = -1
b3 = [21, 33, 45, 9, 24, 9, 34, 7, 88, 96, 54, 35, 66, 77]
b4 = input("Enter the b1 you want to search for: ")
if fonk1(b3, b4):
    print("The b1 is found at b2:", b2 + 1)
else:
    print("Number not found.")