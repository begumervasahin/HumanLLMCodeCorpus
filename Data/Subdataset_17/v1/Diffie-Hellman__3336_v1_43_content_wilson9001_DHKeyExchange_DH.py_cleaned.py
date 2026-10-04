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
    p = int(input("Prime for modulus:\n"))
    a = int(input("Secret exponent:\n"))
    g = int(input("Generator:\n"))
    gPOWaMODp = mod_exp(g, a, p)
    print("Generating value for key exchange...")
    print("g^a (mod p) =", gPOWaMODp)
    gPOWbMODp = int(input("Shared key from server:\n"))
    computed_shared_value = mod_exp(gPOWbMODp, a, p)
    truncate_length = int(input("Truncate of shared value length:\n"))
    truncated_shared_value = truncate_int(computed_shared_value, truncate_length)
    print("Shared value is:", truncated_shared_value)
if __name__ == '__main__':
    main()