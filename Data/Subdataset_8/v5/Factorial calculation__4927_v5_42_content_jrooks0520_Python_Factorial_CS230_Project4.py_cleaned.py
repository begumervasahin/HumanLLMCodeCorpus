def calculate_factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
        print("The factorial of {} is {}. ".format(i, factorial))
def prompt_for_positive_integer():
    while True:
        user_input = input("Please enter a positive integer: ")
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Invalid input. Please enter a positive integer.")
def prompt_for_factorial_method():
    while True:
        option = input("How would you like to solve the factorial? \n"
                       "Option '1': Sequential programming. \n"
                       "Option '2': Recursive programming. \n"
                       "Please enter either '1' or '2': ")
        if option in ('1', '2'):
            return option
        else:
            print("Invalid option. Please enter either '1' or '2'.")
def main():
    while True:
        num = prompt_for_positive_integer()
        method = prompt_for_factorial_method()
        if num == 0:
            print("The factorial of 0 is 1.")
        elif num > 0:
            if method == '1':
                calculate_factorial(num)
            else:
                factorial_recursive(num)
            break
        else:
            print("Invalid input. Please enter a positive integer.")
if __name__ == "__main__":
    main()