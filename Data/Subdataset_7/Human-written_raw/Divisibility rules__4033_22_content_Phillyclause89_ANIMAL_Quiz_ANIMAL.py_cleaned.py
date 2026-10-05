def fonk1():
    print("Enter Number or enter 'q' to quit:")
    b1 = input()
    if b1 = = "q" or b1 == "Q" or b1 == "Quit" or b1 == "QUIT" or b1 == "quit":
        print("Good bye!")
    else:
        try:
            b2 = int(b1)
            if b2 % b3 = = 0:
                print("ANIMAL")
                fonk1()
            elif b2 % b4 = = 0:
                print("ANIM")
                fonk1()
            elif b2 % b5 = = 0:
                print("AN")
                fonk1()
            else:
                print("Try a diffrent number next time.")
                fonk1()
        except ValueError:
            print("Entry is unacceptable.")
            fonk1()
fonk1()