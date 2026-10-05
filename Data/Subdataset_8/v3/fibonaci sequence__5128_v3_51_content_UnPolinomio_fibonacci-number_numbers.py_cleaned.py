def calculate_fibonacci_sequence(length):
    fibonacci_sequence = [1, 1]
    for i in range(length - 2):
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    for index, number in enumerate(fibonacci_sequence):
        print(f"{index + 1}.- {number}")
def get_positive_integer(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            number = int(user_input)
            if number >= 2:
                return number
            else:
                print("\nError: Please insert a positive number greater than or equal to 2.")
        else:
            print("\nError: Please insert an integer number.")
quantity = get_positive_integer("\nHow many Fibonacci numbers do you want to calculate?\n>> ")
calculate_fibonacci_sequence(quantity)