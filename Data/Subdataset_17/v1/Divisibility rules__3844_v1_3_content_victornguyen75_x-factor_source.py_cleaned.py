def validate(char):
    while char not in ['Y', 'y', 'N', 'n']:
        char = input("Invalid input. Please try again. Are those numbers correct? (Y/N) ")
    return char
def main():
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
    print(f"Your first number is {first_num} and your second number is {second_num}")
    choice = input("Are these correct? (Y/N) ")
    choice = validate(choice)
    if choice in ['N', 'n']:
        print("Please restart the program and enter the correct numbers.")
        return
    x_factor = 1
    multiplier = 1
    while x_factor % 10 != 9:
        x_factor = second_num * multiplier
        multiplier += 1
    x_factor = (x_factor
    print(f"Your X Factor is {x_factor}")
    ones_digit = first_num - 10 * (first_num
    ones_digit *= x_factor
    pen_ult = (first_num
    print(f"Is {pen_ult} divisible by {second_num}?")
    if pen_ult % second_num == 0:
        print("Yes, it is divisible.")
    else:
        print("No, it is not divisible.")
if __name__ == "__main__":
    main()