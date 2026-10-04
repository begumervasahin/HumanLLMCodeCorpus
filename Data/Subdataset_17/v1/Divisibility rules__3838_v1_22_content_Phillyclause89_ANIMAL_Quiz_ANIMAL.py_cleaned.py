def numberchecker():
    while True:
        user_input = input("Enter Number or enter 'q' to quit: ")
        if user_input.lower() in ['q', 'quit']:
            print("Good bye!")
            break
        try:
            number = int(user_input)
            if number % 32 == 0:
                print("ANIMAL")
            elif number % 16 == 0:
                print("ANIM")
            elif number % 8 == 0:
                print("AN")
            else:
                print("Try a different number next time.")
        except ValueError:
            print("Entry is unacceptable.")
numberchecker()