from divisibility_rule import div_rule
def is_divisible(n, m):
    divisibility_rule = div_rule(m)
    total = 0
    n_reversed = n[::-1]
    for digit in n_reversed:
        param = next(divisibility_rule)
        total += int(digit) * param
        print(total)
        if abs(total) > 3 * m:
            if total > 0:
                total -= 3 * m
            else:
                total += 3 * m
    return total % m == 0
if __name__ == "__main__":
    number = "1946"
    divisor = 7
    result = is_divisible(number, divisor)
    if result:
        print(f"The number {number} is divisible by {divisor}.")
    else:
        print(f"The number {number} is not divisible by {divisor}.")