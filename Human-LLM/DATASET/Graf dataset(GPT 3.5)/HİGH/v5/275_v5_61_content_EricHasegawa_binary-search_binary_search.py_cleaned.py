def fonk1():
    while True:
        try:
            b1 = int(input("Enter an integer to search: "))
            break
        except ValueError:
            print("Error: Please enter an integer.")
    with open('numberlist.txt') as file:
        b2 = file.read().split(", ")
    b2 = list(map(int, b2))
    b3 = sorted(b2)
    b6, b4 = 0, len(b3) - 1
    while b4 >= b6:
        b5 = (b4 + b6)
        if b1 = = b3[b5]:
            print("Target found.")
            return
        elif b5 = = b6:
            print("Target not found.")
            return
        elif b1 > b3[b5]:
            b6 = b5 + 1
        else:
            b4 = b5 - 1
    print("Target not found.")
    while True:
        b7 = input("Would you like to test another number? (y/n): ")
        if b7 = = 'y':
            fonk1()
            break
        elif b7 = = 'n':
            print("Program terminated.")
            break
        else:
            print("Error: Please enter 'y' or 'n'.")
if b8 = = "__main__":
    fonk1()