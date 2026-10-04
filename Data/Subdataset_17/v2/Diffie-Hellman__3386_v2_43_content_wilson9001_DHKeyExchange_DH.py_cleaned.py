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
def main():
    p = int(input("Prime for modulus (p): "))
    a = int(input("Secret exponent (a): "))
    g = int(input("Generator (g): "))
    g_pow_a_mod_p = mod_exp(g, a, p)
    print("Generating value for key exchange...")
    print(f"g^a (mod p) = {g_pow_a_mod_p}")
    g_pow_b_mod_p = int(input("Shared key from server: "))
    shared_value = mod_exp(g_pow_b_mod_p, a, p)
    truncate_length = int(input("Number of digits to truncate from the shared value: "))
    truncated_shared_value = truncate_int(shared_value, truncate_length)
    print(f"Shared value is: {truncated_shared_value}")
if __name__ == '__main__':
    main()