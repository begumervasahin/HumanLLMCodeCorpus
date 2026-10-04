def fonk1(b1):
    a1 = 1
    for i in range(1, b1 + 1):
        a1 *= i
    return a1
def fonk2(b1):
    if b1 = = 1:
        return 1
    return b1 * fonk2(b1 - 1)
def fonk3(prompt):
    while True:
        b2 = input(prompt)
        if b2.isdigit():
            b2 = int(b2)
            if b2 > 0:
                return b2
            elif b2 = = 0:
                print("The factorial of 0 is 1!")
                exit()
        print("Invalid input. Please enter a positive integer.")
def fonk4():
    while True:
        b3 = input("How would you like to solve the factorial?\b1"
                       "Option '1': Iterative approach.\b1"
                       "Option '2': Recursive approach.\b1"
                       "Please enter either '1' or '2': ")
        if b3 in ('1', '2'):
            return b3
        print("That is not an b3! Please enter '1' or '2'.")
def fonk5():
    b4 = fonk3("Please enter a positive integer: ")
    b3 = fonk4()
    if b3 = = '1':
        a1 = fonk1(b4)
    else:
        a1 = fonk2(b4)
    print(f"The factorial of {b4} is {a1}.")
if b5 = = "__main__":
    fonk5()