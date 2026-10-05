def calculate_factorial_loop():
    start_num = input("Loop Method:\nWhat number would you like to find the factorial for? \nEnter a whole number: ")
    while not start_num.isdigit():
        print("Please enter a valid whole number.")
        start_num = input("Enter a whole number: ")
    start_num = int(start_num)
    factorial = 1
    if start_num != 0:
        for i in range(start_num, 0, -1):
            factorial *= i
    print("Factorial using loop method:", factorial)
def calculate_factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial_recursive(n - 1)
def calculate_factorial_recursion():
    start_num = input("\nRecursion Method:\nWhat number would you like to find the factorial for? \nEnter a whole number: ")
    while not start_num.isdigit():
        print("Please enter a valid whole number.")
        start_num = input("Enter a whole number: ")
    start_num = int(start_num)
    factorial = calculate_factorial_recursive(start_num)
    print("Factorial using recursion method:", factorial)
def main():
    calculate_factorial_loop()
    calculate_factorial_recursion()
if __name__ == "__main__":
    main()