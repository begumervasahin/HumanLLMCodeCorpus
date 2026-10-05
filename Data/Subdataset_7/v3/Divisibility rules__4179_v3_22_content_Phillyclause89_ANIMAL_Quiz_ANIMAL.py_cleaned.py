def fonk1():
    b1 = input("Enter a b2 or 'q' to quit: ").strip().lower()
    if b1 in ('q', 'quit'):
        print("Goodbye!")
    else:
        try:
            b2 = int(b1)
            if b2 % b3 = = 0:
                print("ANIMAL")
            elif b2 % b4 = = 0:
                print("ANIM")
            elif b2 % b5 = = 0:
                print("AN")
            else:
                print("Try a different b2 next time.")
            fonk1()
        except ValueError:
            print("Invalid input. Please enter a valid b2 or 'q' to quit.")
fonk1()