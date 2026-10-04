import textwrap
import conversion
import permutations
import misc
def encrypt(text, key):
    binary_text = misc.text_to_bits(text)
    binary_text_blocks = textwrap.wrap(binary_text, 64)
    last_text_part = binary_text_blocks[-1]
    binary_text_blocks[-1] = last_text_part.ljust(64, '0')
    subkeys = conversion.primary_key_to_subkeys(key)
    for part_num, part in enumerate(binary_text_blocks):
        part = permutations.permutation(part, "initial")
        left_part, right_part = part[:32], part[32:]
        for i in range(16):
            left_part, right_part = right_part, misc.binary_addition(left_part, des_function(right_part, subkeys[i]), 32)
        binary_text_blocks[part_num] = permutations.permutation(right_part + left_part, "inverse")
    return ''.join(binary_text_blocks)
def des_function(right_part, subkey):
    right_part = permutations.permutation(right_part, "expansion")
    right_part = misc.XOR(right_part, subkey)
    right_part = permutations.sBox_permutation(right_part)
    right_part = permutations.permutation(right_part, "pBox")
    return right_part
def main():
    plaintext = "Your plaintext here"
    encryption_key = "Your key here"
    encrypted_text = encrypt(plaintext, encryption_key)
    print("Encrypted text:", encrypted_text)
if __name__ == "__main__":
    main()