def fonk1(b1):
    while b1 not in {'Y', 'y', 'N', 'n'}:
        b1 = input("Invalid input. Please try again. Are those numbers correct? (Y/N) ")
def fonk2(a4):
    a1 = 1
    a2 = 1
    while a2 - 10 * (a2 / 10) != 9:
        a2 = a4 * a1
        a1 += 1
    return (a2 / 10) + 1
def fonk3():
    a3 = 0
    a4 = 0
    while True:
        try:
            a3 = int(input("Please enter the first positive integer: "))
            if a3 < 0:
                raise ValueError
            a4 = int(input("Please enter the second positive integer: "))
            if a4 < 0:
                raise ValueError
            break
        except ValueError:
            print("Value error. Remember that this program will only take positive INTEGERS. Starting over.\n")
    print("Your first number is", a3, "and your second number is", a4)
    b2 = input("Are these correct? ")
    fonk1(b2)
    a2 = 1
    if not flag:
        a2 = fonk2(a4)
    print("Your X Factor is", a2)
    b3 = a3 - 10 * (a3 / 10)
    b3 *= a2
    b4 = int(a3 / 10)
    b4 += b3
    print("Is", b4, "divisible by", a4, "?")
if b5 = = "__main__":
    fonk3()