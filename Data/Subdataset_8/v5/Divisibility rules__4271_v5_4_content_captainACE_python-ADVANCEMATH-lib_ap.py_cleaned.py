def validate_input(choice):
    valid_choices = {'Y', 'y', 'N', 'n'}
    while choice not in valid_choices:
        choice = input("Invalid input. Please try again. Are those numbers correct? (Y/N) ")
def calculate_x_factor(second_num):
    multiplier = 1
    x_factor = 1
    while x_factor % 10 != 9:
        x_factor = second_num * multiplier
        multiplier += 1
    return (x_factor / 10) + 1
def main():
    first_num = 0
    second_num = 0
    while True:
        try:
            first_num = int(input("Please enter the first positive integer: "))
            if first_num < 0:
                raise ValueError
            second_num = int(input("Please enter the second positive integer: "))
            if second_num < 0:
                raise ValueError
            break
        except ValueError:
            print("Value error. Remember that this program will only take positive INTEGERS. Starting over.\n")
    print("Your first number is", first_num, "and your second number is", second_num)
    choice = input("Are these correct? ")
    validate_input(choice)
    x_factor = calculate_x_factor(second_num)
    print("Your X Factor is", x_factor)
    ones_digit = first_num % 10
    ones_digit *= x_factor
    pen_ult = first_num
    print("Is", pen_ult, "divisible by", second_num, "?")
if __name__ == "__main__":
    main()