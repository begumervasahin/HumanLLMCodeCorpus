def fonk1():
    while True :
        try:
            b1 = int(input("Enter an integer: "))
            break
        except ValueError:
            print("You did not enter an integer , try again.")
    b2 = open('b2.txt')
    b3 = b2.read().split(", ")
    print(b3, "HELLO")
    b4 = list(map(int, b3))
    b5 = sorted(b4)
    b6 = len(b5) - 1
    a1 = 0
    while (b6 > a1):
        b7 = ((b6 + a1)
        if (b1 = = b5[b7]) :
            print ("Target found")
            break
        elif (b7 = = a1)  :
            print ("Target not found")
            break
        elif (b1 > b5[b7]) :
            a1 = b7
        elif (b1 < b5[b7]) :
            b6 = b7
    while True :
        b8 = input("Would you like to test another number? (y/n): ")
        if (b8 = = 'y'):
            fonk1()
            break
        elif (b8 = = 'n') :
            print("Roger Dodger")
            break
        else :
            print("You did not enter y or n, try again.")
fonk1()