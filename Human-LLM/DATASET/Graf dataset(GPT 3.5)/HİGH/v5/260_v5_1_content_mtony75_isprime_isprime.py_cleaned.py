def fonk1(prompt):
    while True:
        try:
            b1 = int(input(prompt))
            return b1
        except ValueError:
            print("Invalid input! Please enter an integer.")
def fonk2(number):
    if number < 2:
        return False
    for b2 in range(2, int(number ** 0.5) + 1):
        if number % b2 = = 0:
            return False
    return True
def fonk3(start, end):
    b3 = [b4 for b4 in range(start, end + 1) if fonk2(b4)]
    return b3
def fonk4(start):
    b3 = []
    b4 = start + 1
    while len(b3) < 100:
        if fonk2(b4):
            b3.append(b4)
        b4 += 1
    return b3
if b5 = = "__main__":
    b6 = fonk1("Please enter a number: ")
    if fonk2(b6):
        print(f"{b6} is a prime number.")
    else:
        print(f"{b6} is not a prime number.")
    print()
    print("Enter the range of numbers to find prime numbers within it:")
    b7 = fonk1("Enter the start of the range: ")
    b8 = fonk1("Enter the end of the range: ")
    b9 = fonk3(b7, b8)
    print(f"The prime numbers in the range [{b7}, {b8}] are: {b9}")
    print()
    b10 = fonk4(b6)
    print(f"The next 100 prime numbers after {b6} are: {b10}")