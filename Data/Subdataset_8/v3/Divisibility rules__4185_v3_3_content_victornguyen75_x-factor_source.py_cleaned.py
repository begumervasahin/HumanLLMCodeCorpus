def validate_input(user_input):
    while user_input not in {'Y', 'y', 'N', 'n'}:
        user_input = input("Invalid input. Please try again. Are those numbers correct? (Y/N) ")
first_number = 0
second_number = 0
x_factor = 1
ones_digit = 0
penultimate = 0
flag = False
while True:
    try:
        first_number = int(input("Please enter the first positive integer: "))
        if first_number < 0:
            raise ValueError
        second_number = int(input("Please enter the second positive integer: "))
        if second_number < 0:
            raise ValueError
        break
    except ValueError:
        print("Value error. Remember that this program will only take positive INTEGERS. Starting over.\n")
print("Your first number is", first_number, "and your second number is", second_number)
user_choice = input("Are these correct? ")
validate_input(user_choice)
if not flag:
    multiplier = 1
    while x_factor - 10 * (x_factor / 10) != 9:
        x_factor = second_number * multiplier
        multiplier += 1
    x_factor = (x_factor / 10) + 1
print("Your X Factor is", x_factor)
ones_digit = first_number - 10 * (first_number / 10)
ones_digit *= x_factor
penultimate = int(first_number / 10)
penultimate += ones_digit
print("Is", penultimate, "divisible by", second_number, "?")