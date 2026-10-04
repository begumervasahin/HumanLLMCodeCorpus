def fonk1():
    while True:
        try:
            b1 = int(input("Enter an integer: "))
            break
        except ValueError:
            print("You did not enter an integer. Please try again.")
    with open('numberlist.txt', 'r') as file:
        b2 = file.read().split(", ")
    b3 = list(map(int, b2))
    b4 = sorted(b3)
    a1 = 0
    b5 = len(b4) - 1
    while a1 <= b5:
        b6 = (a1 + b5)
        if b1 = = b4[b6]:
            print("Target found!")
            break
        elif b1 > b4[b6]:
            a1 = b6 + 1
        else:
            b5 = b6 - 1
    else:
        print("Target not found.")
    while True:
        b7 = input("Would you like to test another number? (y/n): ").lower()
        if b7 = = 'y':
            fonk1()
            break
        elif b7 = = 'n':
            print("Exiting program. Goodbye!")
            break
        else:
            print("You did not enter 'y' or 'n'. Please try again.")
fonk1()