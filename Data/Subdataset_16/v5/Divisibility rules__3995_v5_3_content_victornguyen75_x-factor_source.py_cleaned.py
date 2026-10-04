
def fonk1(b1):
    while b1.lower() not in ['y', 'n']:
        b1 = input("Invalid input. Please try again. Are those numbers correct? (Y/N) ")
    return b1
def fonk2(prompt):
    while True:
        try:
            b2 = int(input(prompt))
            if b2 < 0:
                raise ValueError
            return b2
        except ValueError:
            print("Value error. Remember that this program will only take positive INTEGERS. Starting over.\n")
def fonk3(b5):
    a1 = 1
    a2 = 1
    while a1 % 10 != 9:
        a1 = b5 * a2
        a2 += 1
    return (a1
def fonk4(b6, b5, a1):
    b3 = b6 % 10
    b3 *= a1
    b4 = (b6
    print(f"Is {b4} divisible by {b5}?")
    return "Yes, it is divisible." if b4 % b5 = = 0 else "No, it is not divisible."
def fonk5():
    b6 = fonk2("Please enter the first positive integer: ")
    b5 = fonk2("Please enter the second positive integer: ")
    print(f"Your first number is {b6} and your second number is {b5}")
    b7 = input("Are these correct? (Y/N) ")
    b7 = fonk1(b7)
    if b7.lower() == 'n':
        print("Please restart the program and enter the correct numbers.")
        return
    a1 = fonk3(b5)
    print(f"Your X Factor is {a1}")
    b8 = fonk4(b6, b5, a1)
    print(b8)
if b9 = = "__main__":
    fonk5()