def iterative_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
def recursive_factorial(n):
    if n == 1:
        return 1
    return n * recursive_factorial(n - 1)
def main():
    while True:
        pos_int = input("Please enter a positive integer: ")
        if pos_int.isdigit():
            pos_int = int(pos_int)
            if pos_int > 0:
                option = input("How would you like to solve the factorial?\n"
                               "Option '1': Iterative approach.\n"
                               "Option '2': Recursive approach.\n"
                               "Please enter either '1' or '2': ")
                if option == '1':
                    result = iterative_factorial(pos_int)
                    print(f"The factorial of {pos_int} is {result}.")
                    break
                elif option == '2':
                    result = recursive_factorial(pos_int)
                    print(f"The factorial of {pos_int} is {result}.")
                    break
                else:
                    print("That is not an option! Please enter '1' or '2'.")
            elif pos_int == 0:
                print("The factorial of 0 is 1!")
                break
            else:
                print("Please enter a positive integer!")
        else:
            print("Invalid input. Please enter a positive integer.")
if __name__ == "__main__":
    main()