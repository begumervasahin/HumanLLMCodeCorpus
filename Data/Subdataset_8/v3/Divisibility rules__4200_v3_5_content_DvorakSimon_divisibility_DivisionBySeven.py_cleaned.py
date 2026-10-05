def check_divisibility_by_seven(number):
    number_str = str(number)
    while len(number_str) != 2 and number != 0:
        print(f"Current number: {number_str}")
        prefix = number_str[:-1]
        last_digit = int(number_str[-1])
        number_str = str(int(prefix) - (2 * last_digit))
        number = int(number_str)
    if number % 7 == 0:
        print(f"Number {number_str} is divisible by 7!")
    else:
        print(f"Number {number_str} is not divisible by 7.")
number_to_check = 1946
check_divisibility_by_seven(number_to_check)