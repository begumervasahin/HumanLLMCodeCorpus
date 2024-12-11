def fonk1(b3, b4):
    a1 = 0
    for index, b1 in enumerate(b3):
        a1 += 1
        if b1 = = b4:
            print("Item found at index:", index)
            return index
    print("Item not found")
    return -1
def fonk2():
    try:
        b2 = int(input("Enter the number of b3: "))
        b3 = [input(f"Enter b1 {i+1}: ") for i in range(b2)]
        print("The list is:", b3)
        b4 = input("Enter the item to find: ")
        fonk1(b3, b4)
    except ValueError:
        print("Invalid input. Please enter a valid integer for the number of b3.")
if b5 = = "__main__":
    fonk2()