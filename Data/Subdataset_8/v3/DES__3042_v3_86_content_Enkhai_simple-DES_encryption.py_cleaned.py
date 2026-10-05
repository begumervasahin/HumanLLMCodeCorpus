import textwrap
import conversion
import permutations
import misc
def encrypt(text, key):
    binary_text = misc.text_to_bits(text)
    binary_text_blocks = textwrap.wrap(binary_text, 64)
    last_block_len = len(binary_text_blocks[-1])
    if last_block_len < 64:
        binary_text_blocks[-1] += '0' * (64 - last_block_len)
    subkeys = conversion.primary_key_to_subkeys(key)
    encrypted_blocks = []
    for block in binary_text_blocks:
        lpt, rpt = permutations.permutation(block, "initial")[:32], permutations.permutation(block, "initial")[32:]
        for subkey in subkeys:
            lpt, rpt = rpt, misc.binary_addition(lpt, function(rpt, subkey), 32)
        encrypted_block = permutations.permutation(rpt + lpt, "inverse")
        encrypted_blocks.append(encrypted_block)
    return ''.join(encrypted_blocks)
def function(rpt, subkey):
    rpt = permutations.permutation(rpt, "expansion")
    rpt = misc.XOR(rpt, subkey)
    rpt = permutations.sBox_permutation(rpt)
    rpt = permutations.permutation(rpt, "pBox")
    return rpt
text = "Hello, World!"
key = "123456789ABCDEF0"
encrypted_text = encrypt(text, key)
print("Encrypted text:", encrypted_text)