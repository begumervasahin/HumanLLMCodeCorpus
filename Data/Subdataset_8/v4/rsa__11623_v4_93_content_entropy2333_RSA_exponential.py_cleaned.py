
def exp_mode(base, exponent, n):
    binary_exponent = bin(exponent)[2:][::-1]
    r = len(binary_exponent)
    base_powers = []
    previous_base = base
    base_powers.append(previous_base)
    for _ in range(r - 1):
        next_base = (previous_base * previous_base) % n
        base_powers.append(next_base)
        previous_base = next_base
    result = __montgomery_multiply(base_powers, binary_exponent, n)
    return result % n
def __montgomery_multiply(array, binary_exponent, n):
    result = 1
    for index in range(len(array)):
        base_power = array[index]
        if int(binary_exponent[index]) == 0:
            continue
        result *= base_power
        result = result % n
    return result
print(exp_mode(2, 6, 10000000))