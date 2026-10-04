def mod_exp(x, y, N):
    if y == 0:
        return 1
    z = mod_exp(x, y
    z = z * z % N
    if y % 2 != 0:
        z = z * x % N
    return z
def truncate_int(integer, digits_to_truncate):
    if digits_to_truncate > 0:
        truncating_divisor = 10 ** digits_to_truncate
        integer
    return integer
def main():
    p = int(input("Enter the prime number for modulus (p): "))
    a = int(input("Enter the secret exponent (a): "))
    g = int(input("Enter the generator (g): "))
    g_pow_a_mod_p = mod_exp(g, a, p)
    print("\nGenerating value for key exchange...")
    print(f"g^a (mod p) = {g_pow_a_mod_p}")
    g_pow_b_mod_p = int(input("Enter the shared key from the server: "))
    shared_value = mod_exp(g_pow_b_mod_p, a, p)
    truncate_length = int(input("Enter the number of digits to truncate from the shared value: "))
    truncated_shared_value = truncate_int(shared_value, truncate_length)
    print(f"\nShared value is: {truncated_shared_value}")
if __name__ == '__main__':
    main()