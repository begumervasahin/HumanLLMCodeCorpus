def fonk1(a1):
    a1 = 1
    for i in range(1, b2 + 1):
        a1 *= i
        print("The factorial of %s is %s. " % (i, a1))
b1 = True
while b1 = = True:
    b2 = input("Please enter a positive integer: ")
    if b2.isdigit():
        b2 = int(b2)
        if b2 > 0:
            b3 = input("How would you like to solve the factorial?  \n"
                           "Option '1': Sequential programming.  \n"
                           "Option '2': Recursive programming.  \n"
                           "Please enter either '1' or '2': ")
            if b3 = = '1':
                a1 = 1
                for i in range(1, b2 + 1):
                    a1 *= i
                print("The factorial of %s is %s. " % (i, a1))
                b1 = False
            elif b3 = = '2':
                fonk1(b2)
                b1 = False
            else:
                print("That is not an b3! ")
        elif b2 = = 0:
            print("The factorial of 0 is 1! ")
        else:
            print("Please enter a positive integer! ")
    else:
        print("Please enter a positive integer! ")