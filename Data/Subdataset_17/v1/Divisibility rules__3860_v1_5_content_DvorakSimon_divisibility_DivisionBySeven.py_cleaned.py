def check_divisibility_by_7(number):
    s_number_to_check = str(number)
    while len(s_number_to_check) > 2 and number > 0:
        print(s_number_to_check)
        prefix = s_number_to_check[:-1]
        last_digit = int(s_number_to_check[-1])
        s_number_to_check = str(int(prefix) - (2 * last_digit))
        number = int(s_number_to_check)
    if number % 7 == 0:
        return f"Number {s_number_to_check} is divisible by 7!"
    else:
        return f"Number {s_number_to_check} is not divisible by 7."
i_number_to_check = 1946
result = check_divisibility_by_7(i_number_to_check)
print(result)