def fonk1(b1):
    a1 = 1
    for i in range(1, b1 + 1):
        a1 *= i
    return a1
def fonk2(b1):
    if b1 = = 0:
        return 1
    else:
        return b1 * fonk2(b1 - 1)
def fonk3():
    while True:
        b2 = input("Please enter a positive integer: ")
        if b2.isdigit():
            b2 = int(b2)
            if b2 > 0:
                return b2
            elif b2 = = 0:
                print("The factorial of 0 is 1!")
            else:
                print("Please enter a positive integer!")
        else:
            print("Please enter a positive integer!")
def fonk4():
    while True:
        b3 = input("How would you like to solve the factorial? \n"
                       "Option '1': Sequential programming. \n"
                       "Option '2': Recursive programming. \n"
                       "Please enter either '1' or '2': ")
        if b3 in ('1', '2'):
            return b3
        else:
            print("That is not an b3!")
def fonk5():
    b2 = fonk3()
    b3 = fonk4()
    if b3 = = '1':
        a1 = fonk1(b2)
        print("The factorial of {} is {}.".format(b2, a1))
    elif b3 = = '2':
        a1 = fonk2(b2)
        print("The factorial of {} is {}.".format(b2, a1))
if b4 = = "__main__":
    fonk5()