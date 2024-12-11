def fonk1(prompt):
    while True:
        try:
            b1 = input(prompt)
            b2 = int(b1)
            return b2
        except ValueError:
            print("Please enter an integer.")
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
    b5 = fonk1("Enter the starting b3: ")
    b6 = fonk1("Enter the ending b3: ")
    b7 = fonk4(b5, b6)
    return b7
def fonk4(start, end):
    b8 = []
    for num in range(start, end + 1):
        if fonk2(num):
            b8.append(num)
    return b8
def fonk5(b3):
    b9 = []
    b10 = b3 + 1
    while len(b9) < 100:
        if fonk2(b10):
            b9.append(b10)
        b10 += 1
    return b9
if b11 = = "__main__":
    b12 = fonk1("Please enter a b3: ")
    print(b12)
    if fonk2(b12):
        print(f"{b12} is a prime b3")
    else:
        print(f"{b12} is not a prime b3")
    print()
    b13 = fonk3()
    print(f"The list of prime numbers in the range are {b13}")
    print()
    b14 = fonk5(b12)
    print(f"The next 100 prime numbers after {b12} are {b14}")