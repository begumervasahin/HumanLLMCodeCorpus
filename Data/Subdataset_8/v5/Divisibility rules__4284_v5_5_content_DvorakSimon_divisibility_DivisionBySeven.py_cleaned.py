
number_to_check = 1946
number_str = str(number_to_check)
while len(number_str) != 2 and number_to_check >= 0 and number_to_check != 0:
    print(number_str)
    prefix = number_str[:-1]
    last_digit = int(number_str[-1])
    number_str = str(int(prefix) - (2 * last_digit))
    number_to_check = int(number_str)
if number_to_check % 7 == 0:
    print("Number " + number_str + " is divisible by 7!")