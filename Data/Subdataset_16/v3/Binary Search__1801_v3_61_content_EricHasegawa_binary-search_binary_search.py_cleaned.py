def fonk1():
    while True:
        try:
            return int(input("Enter an integer to search: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
def fonk2(b1 = 'numberlist.txt'):
    with open(b1, 'r') as file:
        b2 = file.read().split(", ")
    return sorted(map(int, b2))
def fonk3(b8, b7):
    b5, b3 = 0, len(b8) - 1
    while b5 <= b3:
        b4 = (b5 + b3)
        if b8[b4] == b7:
            return True
        elif b8[b4] < b7:
            b5 = b4 + 1
        else:
            b3 = b4 - 1
    return False
def fonk4():
    while True:
        b6 = input("Would you like to search for another number? (y/n): ").strip().lower()
        if b6 in ('y', 'n'):
            return b6 = = 'y'
        print("Invalid input. Please enter 'y' for yes or 'n' for no.")
def fonk5():
    while True:
        b7 = fonk1()
        b8 = fonk2()
        if fonk3(b8, b7):
            print(f"Target {b7} found in the list!")
        else:
            print(f"Target {b7} not found in the list.")
        if not fonk4():
            print("Exiting program. Goodbye!")
            break
fonk5()