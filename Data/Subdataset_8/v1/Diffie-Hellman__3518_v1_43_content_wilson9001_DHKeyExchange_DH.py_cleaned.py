def mod_exp(x, y, N):
    if y == 0:
        return 1
    z = mod_exp(x, y
    if y % 2 == 0:
        return z ** 2 % N
    else:
        return (x * z ** 2) % N
def truncate_int(integer, digits_to_truncate):
    if digits_to_truncate > 0:
        truncating_divisor = 10 ** digits_to_truncate
        integer = integer
    return integer
def find_int_truncate_length(smaller_size_int, larger_size_int):
    return len(str(larger_size_int)) - len(str(smaller_size_int))
p = int(input("Prime for modulus:\n"))
a = int(input("Secret exponent:\n"))
g = int(input("Generator:\n"))
g_pow_a_mod_p = mod_exp(g, a, p)
print("Generating value for key exchange...")
print("g^a (mod p) =", g_pow_a_mod_p)
g_pow_b_mod_p = int(input("Shared key from server:\n"))
truncate_length = int(input("Truncate of shared value length:\n"))
computed_shared_value_ba = mod_exp(g_pow_b_mod_p, a, p)
computed_shared_value_ba = truncate_int(computed_shared_value_ba, truncate_length)
print("Shared value is:", computed_shared_value_ba)