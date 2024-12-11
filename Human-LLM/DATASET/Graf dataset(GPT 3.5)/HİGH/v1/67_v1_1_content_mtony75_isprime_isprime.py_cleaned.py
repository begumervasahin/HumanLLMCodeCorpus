def fonk1():
    b1 = input("Please enter a b3: ")
    while True:
        try:
            b2 = int(b1)
            break
        except ValueError:
            print("The value entered is not an integer")
            b1 = input("Please enter a new value: ")
    return b2
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
    print("Give me a range of numbers and find out which numbers in the")
    print("range are prime numbers?")
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
    b9 = b3
    b8 = []
    b10 = b9
    while len(b8) < 100:
        b10 += 1
        if fonk2(b10):
            b8.append(b10)
    return b8
if b11 = = "__main__":
    b9 = fonk1()
    print(b9)
    if fonk2(b9):
        print(f"{b9} is a Prime")
    else:
        print(f"{b9} is not a Prime")
    print()
    b12 = fonk3()
    print(f"The list of primes in the range are {b12}")
    print()
    b13 = fonk5(b9)
    print(f"The list of next 100 primes after {b9} are {b13}")