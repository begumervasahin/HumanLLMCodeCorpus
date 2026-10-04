import textwrap
import conversion
import permutations
import misc
def encrypt(text, key):
    binary_text = misc.text_to_bits(text)
    binary_text_blocks = textwrap.wrap(binary_text, 64)
    binary_text_blocks[-1] = binary_text_blocks[-1].ljust(64, '0')
    subkeys = conversion.primary_key_to_subkeys(key)
    for i, block in enumerate(binary_text_blocks):
        block = permutations.permutation(block, "initial")
        left_part, right_part = block[:32], block[32:]
        for round_index in range(16):
            left_part, right_part = right_part, misc.binary_addition(left_part, des_function(right_part, subkeys[round_index]), 32)
        binary_text_blocks[i] = permutations.permutation(right_part + left_part, "inverse")
    return ''.join(binary_text_blocks)
def des_function(right_part, subkey):
    expanded_right = permutations.permutation(right_part, "expansion")
    xored_right = misc.XOR(expanded_right, subkey)
    substituted_right = permutations.sBox_permutation(xored_right)
    final_right = permutations.permutation(substituted_right, "pBox")
    return final_right
def main():
    plaintext = "Your plaintext here"
    encryption_key = "Your key here"
    encrypted_text = encrypt(plaintext, encryption_key)
    print("Encrypted text:", encrypted_text)
if __name__ == "__main__":
    main()