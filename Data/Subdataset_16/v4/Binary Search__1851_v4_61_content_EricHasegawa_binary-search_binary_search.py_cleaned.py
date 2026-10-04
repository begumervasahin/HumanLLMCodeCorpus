def fonk1():
    while True:
        try:
            b1 = int(input("Enter an integer: "))
            break
        except ValueError:
            print("You did not enter an integer. Please try again.")
    with open('numberlist.txt') as numberlist:
        b2 = numberlist.read().split(", ")
    b3 = list(map(int, b2))
    b4 = sorted(b3)
    a1 = 0
    b5 = len(b4) - 1
    while b5 > a1:
        b6 = (b5 + a1)
        if b1 = = b4[b6]:
            print("Target found!")
            break
        elif b6 = = a1:
            print("Target not found.")
            break
        elif b1 > b4[b6]:
            a1 = b6
        elif b1 < b4[b6]:
            b5 = b6
    while True:
        b7 = input("Would you like to test another number? (y/n): ").lower()
        if b7 = = 'y':
            fonk1()
            break
        elif b7 = = 'n':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
fonk1()