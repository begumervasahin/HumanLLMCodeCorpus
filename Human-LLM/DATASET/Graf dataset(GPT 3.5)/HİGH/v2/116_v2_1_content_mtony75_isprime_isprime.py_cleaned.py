def fonk1():
    while True:
        try:
            b1 = input("Please enter a b3: ")
            b2 = int(b1)
            return b2
        except ValueError:
            print("The value entered is not an integer")
def fonk2(b3):
    if b3 = = 1:
        return False
    elif b3 = = 2:
        return True
    else:
        for b4 in range(2, b3
            if b3 % b4 = = 0:
                return False
        return True
def fonk3():
    print("Provide a range of numbers to find out which ones are prime.")
    b5 = fonk1()
    b6 = fonk1()
    b7 = fonk4(b5, b6)
    return b7
def fonk4(num1, num2):
    b8 = []
    for b4 in range(num1, num2 + 1):
        if fonk2(b4):
            b8.append(b4)
    return b8
def fonk5(b3):
    b8 = []
    b9 = b3 + 1
    while len(b8) < 100:
        if fonk2(b9):
            b8.append(b9)
        b9 += 1
    return b8
if b10 = = "__main__":
    b11 = fonk1()
    print(b11)
    if fonk2(b11):
        print(f"{b11} is a prime b3")
    else:
        print(f"{b11} is not a prime b3")
    print()
    b12 = fonk3()
    print(f"The list of prime numbers in the range are {b12}")
    print()
    b13 = fonk5(b11)
    print(f"The next 100 prime numbers after {b11} are {b13}")