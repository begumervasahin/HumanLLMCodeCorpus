import textwrap
import conversion
import permutations
import misc
def encrypt(text, key):
    binary_text = misc.text_to_bits(text)
    binary_text_blocks = textwrap.wrap(binary_text, 64)
    binary_text_blocks = _pad_blocks(binary_text_blocks)
    subkeys = conversion.primary_key_to_subkeys(key)
    encrypted_blocks = []
    for block in binary_text_blocks:
        left_half, right_half = block[:32], block[32:]
        for i in range(16):
            left_half, right_half = _feistel_round(right_half, left_half, subkeys[i])
        encrypted_block = permutations.permutation(right_half + left_half, "inverse")
        encrypted_blocks.append(encrypted_block)
    return ''.join(encrypted_blocks)
def _pad_blocks(blocks):
    last_block_len = len(blocks[-1])
    if last_block_len < 64:
        blocks[-1] += '0' * (64 - last_block_len)
    return blocks
def _feistel_round(right_half, left_half, subkey):
    expanded_right_half = permutations.permutation(right_half, "expansion")
    xored_right_half = misc.XOR(expanded_right_half, subkey)
    sboxed_right_half = permutations.sBox_permutation(xored_right_half)
    permuted_right_half = permutations.permutation(sboxed_right_half, "pBox")
    return right_half, misc.binary_addition(left_half, permuted_right_half, 32)
text = "Hello, World!"
key = "123456789ABCDEF0"
encrypted_text = encrypt(text, key)
print("Encrypted text:", encrypted_text)