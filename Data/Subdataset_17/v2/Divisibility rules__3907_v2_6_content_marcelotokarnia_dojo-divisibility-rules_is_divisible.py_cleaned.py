from divisibility_rule import div_rule
def is_divisible(number, divisor):
    divisibility_rule = div_rule(divisor)
    total = 0
    reversed_number = number[::-1]
    for digit in reversed_number:
        param = next(divisibility_rule)
        total += int(digit) * param
        print(total)
        if abs(total) > 3 * divisor:
            if total > 0:
                total -= 3 * divisor
            else:
                total += 3 * divisor
    return total % divisor == 0
if __name__ == "__main__":
    number = "1946"
    divisor = 7
    result = is_divisible(number, divisor)
    if result:
        print(f"The number {number} is divisible by {divisor}.")
    else:
        print(f"The number {number} is not divisible by {divisor}.")