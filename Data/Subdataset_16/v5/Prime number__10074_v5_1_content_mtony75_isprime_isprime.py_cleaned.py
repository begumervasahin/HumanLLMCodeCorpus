def fonk1(prompt):
    while True:
        b1 = input(prompt)
        try:
            return int(b1)
        except ValueError:
            print("The value entered is not an integer. Please enter a valid integer.")
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
    print("Provide a range of numbers to find out which numbers in the range are prime numbers.")
    b4 = fonk1("Enter the first b2: ")
    b5 = fonk1("Enter the second b2: ")
    lower, b6 = sorted([b4, b5])
    return fonk4(lower, b6)
def fonk4(start, end):
    return [num for num in range(start, end + 1) if fonk2(num)]
def fonk5(start_number):
    b7 = []
    b8 = start_number + 1
    while len(b7) < 100:
        if fonk2(b8):
            b7.append(b8)
        b8 += 1
    return b7
if b9 = = "__main__":
    b10 = fonk1("Please enter a b2: ")
    if fonk2(b10):
        print(f"{b10} is a prime b2.")
    else:
        print(f"{b10} is not a prime b2.")
    print("\n")
    b11 = fonk3()
    print(f"The list of b7 in the range is: {b11}")
    print("\n")
    b12 = fonk5(b10)
    print(f"The next 100 prime numbers after {b10} are: {b12}")