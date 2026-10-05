
def generate_divisibility_rule(m):
    index = 0
    while True:
        yield (-1) ** index
        index += 1
def is_divisible_by_rule(number, divisor):
    divisibility_rule = generate_divisibility_rule(divisor)
    running_total = 0
    number_str_reversed = str(number)[::-1]
    for digit in number_str_reversed:
        multiplier = next(divisibility_rule)
        running_total += int(digit) * multiplier
        if abs(running_total) > 3 * divisor:
            running_total %= 3 * divisor
    return running_total % divisor == 0
number_to_check = 123456
divisor_to_check = 7
result = is_divisible_by_rule(number_to_check, divisor_to_check)
print(result)
