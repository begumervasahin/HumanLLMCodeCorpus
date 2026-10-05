
from divisibility_rule import div_rule
def is_divisible_by_rule(n, m):
    divisibility_rule = div_rule(m)
    total_sum = 0
    n = n[::-1]
    for digit in n:
        multiplier = next(divisibility_rule)
        total_sum += int(digit) * multiplier
        if abs(total_sum) > 3 * m:
            total_sum %= 3 * m
    return total_sum % m == 0
number_to_check = 123456
divisor_to_check = 7
result = is_divisible_by_rule(number_to_check, divisor_to_check)
print(result)
