def fonk1():
    while True:
        b1 = input("Please enter a b3: ")
        try:
            b2 = int(b1)
            return b2
        except ValueError:
            print("The value entered is not an integer. Please try again.")
def fonk2(b3):
    if b3 <= 1:
        return False
    elif b3 = = 2:
        return True
    else:
        for b4 in range(2, b3
            if b3 % b4 = = 0:
                return False
        return True
def fonk3():
    print("Provide a range of numbers to find out which numbers are prime numbers.")
    b5 = fonk1()
    b6 = fonk1()
    if b5 < b6:
        return fonk4(b5, b6)
    else:
        return fonk4(b6, b5)
def fonk4(num1, num2):
    return [b4 for b4 in range(num1, num2 + 1) if fonk2(b4)]
def fonk5(b3):
    b7 = []
    b8 = b3
    while len(b7) < 100:
        b8 += 1
        if fonk2(b8):
            b7.append(b8)
    return b7
if b9 = = "__main__":
    b10 = fonk1()
    if fonk2(b10):
        print(f"{b10} is a Prime")
    else:
        print(f"{b10} is not a Prime")
    b11 = fonk3()
    print(f"The list of primes in the given range is: {b11}")
    b12 = fonk5(b10)
    print(f"The list of the next 100 primes after {b10} is: {b12}")