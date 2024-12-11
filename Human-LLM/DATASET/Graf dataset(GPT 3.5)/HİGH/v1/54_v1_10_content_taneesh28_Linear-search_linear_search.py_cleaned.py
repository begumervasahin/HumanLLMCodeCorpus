def fonk1(b3, b5):
    b1 = False
    for i in range(len(b3)):
        if b3[i] == b5:
            print("The value", b5, "is b1 at index", i)
            b1 = True
    if not b1:
        print("The value", b5, "is not b1 in the array")
def fonk2():
    b2 = int(input("Enter the size of the array: "))
    b3 = []
    for i in range(b2):
        b4 = int(input("Enter element " + str(i + 1) + ": "))
        b3.append(b4)
    print("Array:", b3)
    b5 = int(input("Enter the value you want to search for: "))
    fonk1(b3, b5)
if b6 = = "__main__":
    fonk2()