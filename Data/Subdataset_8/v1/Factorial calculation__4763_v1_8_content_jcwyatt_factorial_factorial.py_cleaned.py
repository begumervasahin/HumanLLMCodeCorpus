def factorial_with_loop():
    start_num = input("Loop Method:\nWhat number would you like to find the factorial for? \nEnter a whole number: ")
    while not start_num.isdigit():
        start_num = input("Invalid input. Please enter a valid whole number: ")
    start_num = int(start_num)
    factorial = 1
    if start_num != 0:
        for i in range(start_num, 0, -1):
            factorial *= i
    print("Factorial:", factorial)
def factorial_with_recursion():
    start_num = input("\nRecursion Method:\nWhat number would you like to find the factorial for? \nEnter a whole number: ")
    while not start_num.isdigit():
        start_num = input("Invalid input. Please enter a valid whole number: ")
    start_num = int(start_num)
    def recur_factorial(n):
        if n == 1:
            return n
        else:
            return n * recur_factorial(n - 1)
    factorial = recur_factorial(start_num)
    print("Factorial:", factorial)
if __name__ == "__main__":
    factorial_with_loop()
    factorial_with_recursion()