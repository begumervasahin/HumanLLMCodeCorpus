def fonk1():
    while True:
        try:
            b1 = int(input("Enter an integer: "))
            break
        except ValueError:
            print("You did not enter an integer, try again.")
    with open('b2.txt', 'r') as numberlist_file:
        b2 = numberlist_file.read().split(", ")
        b3 = sorted(map(int, b2))
    b4 = len(b3) - 1
    a1 = 0
    while b4 >= a1:
        b5 = (b4 + a1)
        if b1 = = b3[b5]:
            print("Target found")
            break
        elif b5 = = a1:
            print("Target not found")
            break
        elif b1 > b3[b5]:
            a1 = b5 + 1
        elif b1 < b3[b5]:
            b4 = b5 - 1
    while True:
        b6 = input("Would you like to test another number? (y/n): ")
        if b6 = = 'y':
            fonk1()
            break
        elif b6 = = 'n':
            print("Exiting the program")
            break
        else:
            print("You did not enter y or n, try again.")
if b7 = = "__main__":
    fonk1()