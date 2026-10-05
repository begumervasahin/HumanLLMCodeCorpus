import textwrap
import conversion
import permutations
import misc
def fonk1(b6, b7):
    b1 = misc.text_to_bits(b6)
    b1 = textwrap.wrap(b1, 64)
    b2 = b1[-1]
    b1[-1] = b2 + '0' * (64 - len(b2))
    b3 = conversion.primary_key_to_subkeys(b7)
    for part_num, b4 in enumerate(b1):
        b4 = permutations.permutation(b4, "initial")
        lpt, b5 = b4[:32], b4[32:]
        for i in range(16):
            lpt, b5 = b5, misc.binary_addition(lpt, fonk2(b5, b3[i]), 32)
        b1[part_num] = permutations.permutation(b5 + lpt, "inverse")
    return ''.join(b1)
def fonk2(b5, subkey):
    b5 = permutations.permutation(b5, "expansion")
    b5 = misc.XOR(b5, subkey)
    b5 = permutations.sBox_permutation(b5)
    b5 = permutations.permutation(b5, "pBox")
    return b5
b6 = "Hello, World!"
b7 = "123456789ABCDEF0"
b8 = fonk1(b6, b7)
print("Encrypted b6:", b8)