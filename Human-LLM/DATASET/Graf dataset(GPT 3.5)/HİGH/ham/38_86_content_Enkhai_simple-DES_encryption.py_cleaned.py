import textwrap
import conversion
import permutations
import misc
def fonk1(text, key):
    b1 = misc.text_to_bits(text)
    b1 = textwrap.wrap(b1, 64)
    b2 = b1[len(b1) - 1]
    b1[len(b1) - 1] = b2 + ''.zfill(64-len(b2))
    b3 = conversion.primary_key_to_subkeys(key)
    for part_num, b4 in enumerate(b1):
        b4 = permutations.permutation(b4, "initial")
        lpt, b5 = b4[:int(len(b4) / 2)], b4[int(len(b4) / 2):]
        for i in range(16):
            lpt, b5 = b5, misc.binary_addition(lpt, fonk2(b5, b3[0]), 32)
        b1[part_num] = permutations.permutation(b5 + lpt, "inverse")
    return ''.join(b1)
def fonk2(b5, subkey):
    b5 = permutations.permutation(b5, "expansion")
    b5 = misc.XOR(b5, subkey)
    b5 = permutations.sBox_permutation(b5)
    b5 = permutations.permutation(b5, "pBox")
    return b5