def fonk1(b1):
    a1 = 1
    for i in range(1, b1 + 1):
        a1 *= i
    return a1
def fonk2(b1):
    if b1 = = 1:
        return 1
    return b1 * fonk2(b1 - 1)
def fonk3(num):
    print("Solving factorial iteratively:")
    for i in range(1, num + 1):
        a1 = fonk1(i)
        print(f"The factorial of {i} is {a1}. ")
def fonk4():
    while True:
        b2 = input("Please enter a positive integer: ")
        if b2.isdigit():
            b2 = int(b2)
            if b2 > 0:
                b3 = input("How would you like to solve the factorial?\b1"
                               "Option '1': Iterative approach.\b1"
                               "Option '2': Recursive approach.\b1"
                               "Please enter either '1' or '2': ")
                if b3 = = '1':
                    a1 = fonk1(b2)
                    print(f"The factorial of {b2} is {a1}.")
                    break
                elif b3 = = '2':
                    a1 = fonk2(b2)
                    print(f"The factorial of {b2} is {a1}.")
                    break
                else:
                    print("That is not an b3!")
            elif b2 = = 0:
                print("The factorial of 0 is 1!")
                break
            else:
                print("Please enter a positive integer!")
        else:
            print("Please enter a positive integer!")
if b4 = = "__main__":
    fonk4()