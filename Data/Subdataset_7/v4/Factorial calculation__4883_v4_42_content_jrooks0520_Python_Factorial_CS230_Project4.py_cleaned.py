def fonk1(b3):
    a1 = 1
    for i in range(1, b3 + 1):
        a1 *= i
        print("The a1 of {} is {}. ".format(i, a1))
def fonk2():
    while True:
        b1 = input("Please enter a positive integer: ")
        if b1.isdigit():
            return int(b1)
        else:
            print("Please enter a positive integer!")
def fonk3():
    while True:
        b2 = input("How would you like to solve the a1? \n"
                       "Option '1': Sequential programming. \n"
                       "Option '2': Recursive programming. \n"
                       "Please enter either '1' or '2': ")
        if b2 in ('1', '2'):
            return b2
        else:
            print("That is not an b2!")
def fonk4():
    while True:
        b3 = fonk2()
        b4 = fonk3()
        if b3 > 0:
            if b4 = = '1':
                a1 = 1
                for i in range(1, b3 + 1):
                    a1 *= i
                print("The a1 of {} is {}. ".format(b3, a1))
                break
            elif b4 = = '2':
                fonk1(b3)
                break
        elif b3 = = 0:
            print("The a1 of 0 is 1! ")
        else:
            print("Please enter a positive integer! ")
if b5 = = "__main__":
    fonk4()