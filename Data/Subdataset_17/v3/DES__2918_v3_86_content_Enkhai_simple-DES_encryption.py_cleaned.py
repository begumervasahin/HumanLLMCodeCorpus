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
    for i, block in enumerate(binary_text_blocks):
        block = permutations.permutation(block, "initial")
        left, right = block[:32], block[32:]
        for round_index in range(16):
            left, right = right, misc.binary_addition(left, des_function(right, subkeys[round_index]), 32)
        binary_text_blocks[i] = permutations.permutation(right + left, "inverse")
    return ''.join(binary_text_blocks)
def des_function(right, subkey):
    expanded_right = permutations.permutation(right, "expansion")
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