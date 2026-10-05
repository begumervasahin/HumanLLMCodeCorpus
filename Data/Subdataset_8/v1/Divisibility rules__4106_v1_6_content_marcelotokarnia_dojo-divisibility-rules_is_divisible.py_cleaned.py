def div_rule(m):
    current_index = 0
    while True:
        yield (-1) ** current_index
        current_index += 1
def is_divisible(n, m):
    divisibility_rule = div_rule(m)
    total_sum = 0
    n = str(n)[::-1]
    for digit in n:
        multiplier = next(divisibility_rule)
        total_sum += int(digit) * multiplier
        if abs(total_sum) > 3 * m:
            total_sum %= 3 * m
    return total_sum % m == 0
number = 123456
divisor = 7
result = is_divisible(number, divisor)
print(result)
