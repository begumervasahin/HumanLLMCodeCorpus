def fonk1():
    while True:
        b1 = input("Please enter a b2: ")
        try:
            return int(b1)
        except ValueError:
            print("The value entered is not an integer. Please try again.")
def fonk2(b2):
    if b2 <= 1:
        return False
    if b2 = = 2:
        return True
    for b3 in range(2, int(b2 ** 0.5) + 1):
        if b2 % b3 = = 0:
            return False
    return True
def fonk3():
    print("Provide a range of numbers to find out which numbers are prime numbers.")
    b4 = fonk1()
    b5 = fonk1()
    return fonk4(min(b4, b5), max(b4, b5))
def fonk4(num1, num2):
    return [b3 for b3 in range(num1, num2 + 1) if fonk2(b3)]
def fonk5(b2):
    b6 = []
    b7 = b2
    while len(b6) < 100:
        b7 += 1
        if fonk2(b7):
            b6.append(b7)
    return b6
if b8 = = "__main__":
    b9 = fonk1()
    if fonk2(b9):
        print(f"{b9} is a Prime")
    else:
        print(f"{b9} is not a Prime")
    b10 = fonk3()
    print(f"The list of b6 in the given range is: {b10}")
    b11 = fonk5(b9)
    print(f"The list of the next 100 b6 after {b9} is: {b11}")