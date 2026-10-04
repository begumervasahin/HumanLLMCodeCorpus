def fonk1(b1):
    while b1 not in ['Y', 'y', 'N', 'n']:
        b1 = input("Invalid input. Please try again. Are those numbers correct? (Y/N) ")
    return b1
def fonk2():
    while True:
        try:
            b2 = int(input("Please enter the first positive integer: "))
            if b2 < 0:
                raise ValueError
            b3 = int(input("Please enter the second positive integer: "))
            if b3 < 0:
                raise ValueError
            break
        except ValueError:
            print("Value error. Remember that this program will only take positive INTEGERS. Starting over.\n")
    print(f"Your first number is {b2} and your second number is {b3}")
    b4 = input("Are these correct? (Y/N) ")
    b4 = fonk1(b4)
    if b4 in ['N', 'n']:
        print("Please restart the program and enter the correct numbers.")
        return
    a1 = 1
    a2 = 1
    while a1 % 10 != 9:
        a1 = b3 * a2
        a2 += 1
    a1 = (a1
    print(f"Your X Factor is {a1}")
    b5 = b2 - 10 * (b2
    b5 *= a1
    b6 = (b2
    print(f"Is {b6} divisible by {b3}?")
    if b6 % b3 = = 0:
        print("Yes, it is divisible.")
    else:
        print("No, it is not divisible.")
if b7 = = "__main__":
    fonk2()