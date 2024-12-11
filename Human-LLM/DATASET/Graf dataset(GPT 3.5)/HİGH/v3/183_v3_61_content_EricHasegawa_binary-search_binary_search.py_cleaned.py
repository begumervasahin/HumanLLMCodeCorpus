def fonk1(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")
def fonk2(filename):
    with open(filename, 'r') as file:
        b1 = file.read().split(", ")
        return sorted(map(int, b1))
def fonk3():
    b2 = fonk1("Enter an integer to search: ")
    b3 = fonk2('numberlist.txt')
    b6, b4 = 0, len(b3) - 1
    while b4 >= b6:
        b5 = (b4 + b6)
        if b2 = = b3[b5]:
            print("Target found.")
            return
        elif b5 = = b6:
            print("Target not found.")
            return
        elif b2 > b3[b5]:
            b6 = b5 + 1
        elif b2 < b3[b5]:
            b4 = b5 - 1
if b7 = = "__main__":
    fonk3()