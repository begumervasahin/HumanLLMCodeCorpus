def fonk1(b1):
    a1 = 1
    for i in range(1, b1 + 1):
        a1 *= i
    print("The factorial of {} is {}.".format(b1, a1))
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
                b3 = input("How would you like to solve the factorial? \n"
                               "Option '1': Sequential programming. \n"
                               "Option '2': Recursive programming. \n"
                               "Please enter either '1' or '2': ")
                if b3 = = '1':
                    fonk1(b2)
                    break
                elif b3 = = '2':
                    a1 = fonk2(b2)
                    print("The factorial of {} is {}.".format(b2, a1))
                    break
                else:
                    print("That is not an b3!")
            elif b2 = = 0:
                print("The factorial of 0 is 1!")
            else:
                print("Please enter a positive integer!")
        else:
            print("Please enter a positive integer!")
if b4 = = "__main__":
    fonk3()