def fonk1():
    while True:
        b1 = input("Enter a b2 or enter 'q' to quit: ")
        if b1.lower() in ['q', 'quit']:
            print("Goodbye!")
            break
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
        except ValueError:
            print("Entry is unacceptable. Please enter a valid b2.")
fonk1()