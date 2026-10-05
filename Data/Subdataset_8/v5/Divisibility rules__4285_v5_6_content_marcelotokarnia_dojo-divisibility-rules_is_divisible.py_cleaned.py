
from divisibility_rule import div_rule
def is_divisible_by_rule(number, divisor):
    divisibility_rule = div_rule(divisor)
    total_sum = 0
    number_str_reversed = str(number)[::-1]
    for digit in number_str_reversed:
        multiplier = next(divisibility_rule)
        total_sum += int(digit) * multiplier
        if abs(total_sum) > 3 * divisor:
            total_sum %= 3 * divisor
    return total_sum % divisor == 0
number_to_check = 123456
divisor_to_check = 7
result = is_divisible_by_rule(number_to_check, divisor_to_check)
print(result)
