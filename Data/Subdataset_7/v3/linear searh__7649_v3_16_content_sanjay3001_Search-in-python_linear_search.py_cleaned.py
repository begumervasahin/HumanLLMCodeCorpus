def fonk1(b4, b5):
    a1 = 0
    b1 = False
    for position, b2 in enumerate(b4):
        a1 += 1
        if b2 = = b5:
            b1 = True
            print("Found")
            break
    return a1, b1
def fonk2():
    b3 = int(input("Enter the number of elements: "))
    b4 = [input("Enter b2 {}: ".format(i + 1)) for i in range(b3)]
    print("THE LIST IS", b4)
    b5 = input("Enter the item to find: ")
    a1, b1 = fonk1(b4, b5)
    print("Number of iterations:", a1)
    if not b1:
        print("Item not b1.")
if b6 = = "__main__":
    fonk2()