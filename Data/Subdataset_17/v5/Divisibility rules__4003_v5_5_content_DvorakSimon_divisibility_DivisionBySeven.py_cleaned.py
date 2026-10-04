def check_divisibility_by_7(number):
    current_number = number
    while len(str(current_number)) > 2 and current_number > 0:
        print(current_number)
        prefix = str(current_number)[:-1]
        last_digit = int(str(current_number)[-1])
        current_number = int(prefix) - (2 * last_digit)
    if current_number % 7 == 0:
        return f"Number {current_number} is divisible by 7!"
    else:
        return f"Number {current_number} is not divisible by 7."
if __name__ == "__main__":
    initial_number = 1946
    result = check_divisibility_by_7(initial_number)
    print(result)