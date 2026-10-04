def fonk1():
    while True:
        try:
            b1 = int(input("Enter an integer to search: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    with open('numberlist.txt', 'r') as file:
        b2 = file.read().split(", ")
    b3 = sorted(map(int, b2))
    b6, b4 = 0, len(b3) - 1
    while b6 <= b4:
        b5 = (b6 + b4)
        if b3[b5] == b1:
            print(f"Target {b1} found in the list!")
            break
        elif b3[b5] < b1:
            b6 = b5 + 1
        else:
            b4 = b5 - 1
    else:
        print(f"Target {b1} not found in the list.")
    while True:
        b7 = input("Would you like to search for another number? (y/n): ").strip().lower()
        if b7 = = 'y':
            fonk1()
            break
        elif b7 = = 'n':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")
fonk1()