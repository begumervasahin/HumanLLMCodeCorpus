import textwrap
import conversion
import permutations
import misc
def fonk1(b12, b13):
    b1 = misc.text_to_bits(b12)
    b2 = textwrap.wrap(b1, 64)
    b3 = len(b2[-1])
    if b3 < 64:
        b2[-1] += '0' * (64 - b3)
    b4 = conversion.primary_key_to_subkeys(b13)
    b5 = []
    for block in b2:
        left_half, b6 = block[:32], block[32:]
        for i in range(16):
            left_half, b6 = b6, misc.binary_addition(left_half, fonk2(b6, b4[i]), 32)
        b7 = permutations.permutation(b6 + left_half, "inverse")
        b5.append(b7)
    return ''.join(b5)
def fonk2(b6, subkey):
    b8 = permutations.permutation(b6, "expansion")
    b9 = misc.XOR(b8, subkey)
    b10 = permutations.sBox_permutation(b9)
    b11 = permutations.permutation(b10, "pBox")
    return b11
b12 = "Hello, World!"
b13 = "123456789ABCDEF0"
b14 = fonk1(b12, b13)
print("Encrypted b12:", b14)