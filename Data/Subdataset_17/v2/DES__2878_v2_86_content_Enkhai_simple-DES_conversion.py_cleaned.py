import misc
import permutations
def primary_key_to_subkeys(key):
    subkeys = []
    binary_prim_key = misc.hex_to_bits(key)
    binary_prim_key = ''.join([binary_prim_key[i:i + 7] for i in range(0, len(binary_prim_key), 8)])
    half_length = len(binary_prim_key)
    left_part = binary_prim_key[:half_length]
    right_part = binary_prim_key[half_length:]
    for i in range(16):
        shift_amount = 1 if i in {0, 1, 8, 15} else 2
        left_part = misc.left_shift(left_part, shift_amount)
        right_part = misc.left_shift(right_part, shift_amount)
        combined_key = left_part + right_part
        subkeys.append(permutations.permutation(combined_key, "compression"))
    return subkeys
def main():
    primary_key = "133457799BBCDFF1"
    subkeys = primary_key_to_subkeys(primary_key)
    print("Subkeys:")
    for idx, subkey in enumerate(subkeys, 1):
        print(f"Subkey {idx}: {subkey}")
if __name__ == "__main__":
    main()