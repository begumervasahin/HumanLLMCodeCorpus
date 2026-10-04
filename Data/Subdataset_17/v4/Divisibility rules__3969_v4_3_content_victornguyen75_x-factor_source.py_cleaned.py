
def validate(char):
    while char.lower() not in ['y', 'n']:
        char = input("Invalid input. Please try again. Are those numbers correct? (Y/N) ")
    return char
def get_positive_integer(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num < 0:
                raise ValueError
            return num
        except ValueError:
            print("Value error. Remember that this program will only take positive INTEGERS. Starting over.\n")
def calculate_x_factor(second_num):
    x_factor = 1
    multiplier = 1
    while x_factor % 10 != 9:
        x_factor = second_num * multiplier
        multiplier += 1
    return (x_factor
def check_divisibility(first_num, second_num, x_factor):
    ones_digit = first_num % 10
    ones_digit *= x_factor
    penultimate = (first_num
    print(f"Is {penultimate} divisible by {second_num}?")
    if penultimate % second_num == 0:
        return "Yes, it is divisible."
    else:
        return "No, it is not divisible."
def main():
    first_num = get_positive_integer("Please enter the first positive integer: ")
    second_num = get_positive_integer("Please enter the second positive integer: ")
    print(f"Your first number is {first_num} and your second number is {second_num}")
    choice = input("Are these correct? (Y/N) ")
    choice = validate(choice)
    if choice.lower() == 'n':
        print("Please restart the program and enter the correct numbers.")
        return
    x_factor = calculate_x_factor(second_num)
    print(f"Your X Factor is {x_factor}")
    result = check_divisibility(first_num, second_num, x_factor)
    print(result)
if __name__ == "__main__":
    main()