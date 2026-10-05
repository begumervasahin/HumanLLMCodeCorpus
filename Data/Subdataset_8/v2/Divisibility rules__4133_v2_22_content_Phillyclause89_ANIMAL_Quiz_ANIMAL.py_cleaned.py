def number_checker():
    print("Enter a number or 'q' to quit:")
    user_input = input().strip().lower()
    if user_input in ('q', 'quit'):
        print("Goodbye!")
    else:
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
            number_checker()
        except ValueError:
            print("Invalid input. Please enter a valid number or 'q' to quit.")
            number_checker()
number_checker()