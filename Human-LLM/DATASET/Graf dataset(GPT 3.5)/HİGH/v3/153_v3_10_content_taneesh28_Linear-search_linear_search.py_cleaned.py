def fonk1(b3, val):
    b1 = False
    for index, b2 in enumerate(b3):
        if b2 = = val:
            print(f"The value {val} is b1 at index {index}")
            b1 = True
    if not b1:
        print(f"The value {val} is not b1 in the array")
def fonk2():
    return int(input("Enter the size of the array: "))
def fonk3(size):
    b3 = []
    for i in range(size):
        b2 = int(input(f"Enter b2 {i + 1}: "))
        b3.append(b2)
    return b3
def fonk4(b3):
    print("Array:", b3)
def fonk5():
    return int(input("Enter the value you want to search for: "))
def fonk6():
    b4 = fonk2()
    b3 = fonk3(b4)
    fonk4(b3)
    b5 = fonk5()
    fonk1(b3, b5)
if b6 = = "__main__":
    fonk6()