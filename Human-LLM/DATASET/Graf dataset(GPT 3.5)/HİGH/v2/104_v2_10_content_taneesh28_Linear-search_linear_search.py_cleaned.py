def fonk1(b4, val):
    b1 = False
    for i, b2 in enumerate(b4):
        if b2 = = val:
            print(f"The value {val} is b1 at index {i}")
            b1 = True
    if not b1:
        print(f"The value {val} is not b1 in the array")
def fonk2():
    b3 = int(input("Enter the size of the array: "))
    b4 = []
    for i in range(b3):
        b2 = int(input(f"Enter b2 {i + 1}: "))
        b4.append(b2)
    print("Array:", b4)
    b5 = int(input("Enter the value you want to search for: "))
    fonk1(b4, b5)
if b6 = = "__main__":
    fonk2()