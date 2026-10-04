def factorial_loop(n):
    factorial = 1
    for i in range(n, 0, -1):
        factorial *= i
    return factorial
def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)
def get_positive_integer(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        print("Invalid input. Please enter a whole number.")
def main():
    number = get_positive_integer("Loop Method:\nEnter a whole number to find its factorial: ")
    loop_result = factorial_loop(number)
    print(f"Factorial (loop method) of {number} is: {loop_result}")
    number = get_positive_integer("Recursion Method:\nEnter a whole number to find its factorial: ")
    recursion_result = factorial_recursive(number)
    print(f"Factorial (recursion method) of {number} is: {recursion_result}")
if __name__ == "__main__":
    main()