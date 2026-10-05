def fonk1(b3, val):
    for b5, b1 in enumerate(b3):
        if b1 = = val:
            return b5
    return -1
def fonk2():
    b2 = int(input("Enter the size of the array: "))
    b3 = []
    for i in range(b2):
        b1 = int(input("Enter b1 {} of the array: ".format(i+1)))
        b3.append(b1)
    print("Array:", b3)
    b4 = int(input("Enter the value you want to search for: "))
    b5 = fonk1(b3, b4)
    if b5 != -1:
        print("The value", b4, "is found at b5", b5)
    else:
        print("Value not found in the array")
if b6 = = "__main__":
    fonk2()