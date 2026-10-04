def check_divisibility_by_7(number):
    current_number_str = str(number)
    while len(current_number_str) > 2 and number > 0:
        print(current_number_str)
        prefix = current_number_str[:-1]
        last_digit = int(current_number_str[-1])
        transformed_number = int(prefix) - (2 * last_digit)
        current_number_str = str(transformed_number)
        number = transformed_number
    if number % 7 == 0:
        return f"Number {current_number_str} is divisible by 7!"
    else:
        return f"Number {current_number_str} is not divisible by 7."
if __name__ == "__main__":
    initial_number = 1946
    result = check_divisibility_by_7(initial_number)
    print(result)