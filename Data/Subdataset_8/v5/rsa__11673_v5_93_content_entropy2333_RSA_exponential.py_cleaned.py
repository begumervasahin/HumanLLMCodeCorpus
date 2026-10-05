def exp_mod_montgomery(base, exponent, modulus):
    binary_exponent = bin(exponent)[2:][::-1]
    r = len(binary_exponent)
    base_powers = [base]
    previous_base = base
    for _ in range(r - 1):
        next_base = (previous_base * previous_base) % modulus
        base_powers.append(next_base)
        previous_base = next_base
    result = montgomery_multiply(base_powers, binary_exponent, modulus)
    return result % modulus
def montgomery_multiply(array, binary_exponent, modulus):
    result = 1
    for index, base_power in enumerate(array):
        if int(binary_exponent[index]) == 0:
            continue
        result *= base_power
        result = result % modulus
    return result
print(exp_mod_montgomery(2, 6, 10000000))