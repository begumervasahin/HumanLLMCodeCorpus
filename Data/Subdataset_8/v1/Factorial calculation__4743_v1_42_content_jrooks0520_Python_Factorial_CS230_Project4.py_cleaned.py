def factorial_sequential(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    print("The factorial of %s is %s." % (num, result))
def factorial_recursive(num):
    if num == 0:
        return 1
    else:
        return num * factorial_recursive(num - 1)
def main():
    while True:
        pos_int = input("Please enter a positive integer: ")
        if pos_int.isdigit():
            pos_int = int(pos_int)
            if pos_int > 0:
                option = input("How would you like to solve the factorial? \n"
                               "Option '1': Sequential programming. \n"
                               "Option '2': Recursive programming. \n"
                               "Please enter either '1' or '2': ")
                if option == '1':
                    factorial_sequential(pos_int)
                    break
                elif option == '2':
                    result = factorial_recursive(pos_int)
                    print("The factorial of %s is %s." % (pos_int, result))
                    break
                else:
                    print("That is not an option!")
            elif pos_int == 0:
                print("The factorial of 0 is 1!")
            else:
                print("Please enter a positive integer!")
        else:
            print("Please enter a positive integer!")
if __name__ == "__main__":
    main()