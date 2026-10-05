def calculate_factorial_sequential(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result
def calculate_factorial_recursive(num):
    if num == 0:
        return 1
    else:
        return num * calculate_factorial_recursive(num - 1)
def prompt_for_integer():
    while True:
        pos_int = input("Please enter a positive integer: ")
        if pos_int.isdigit():
            pos_int = int(pos_int)
            if pos_int > 0:
                return pos_int
            elif pos_int == 0:
                print("The factorial of 0 is 1!")
            else:
                print("Please enter a positive integer!")
        else:
            print("Please enter a positive integer!")
def choose_factorial_method():
    while True:
        option = input("How would you like to solve the factorial? \n"
                       "Option '1': Sequential programming. \n"
                       "Option '2': Recursive programming. \n"
                       "Please enter either '1' or '2': ")
        if option in ('1', '2'):
            return option
        else:
            print("That is not an option!")
def main():
    pos_int = prompt_for_integer()
    option = choose_factorial_method()
    if option == '1':
        result = calculate_factorial_sequential(pos_int)
        print("The factorial of {} is {}.".format(pos_int, result))
    elif option == '2':
        result = calculate_factorial_recursive(pos_int)
        print("The factorial of {} is {}.".format(pos_int, result))
if __name__ == "__main__":
    main()