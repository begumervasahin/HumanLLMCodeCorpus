import textwrap
import conversion
import permutations
import misc
def fonk1(b12, b13):
    b1 = misc.text_to_bits(b12)
    b2 = textwrap.wrap(b1, 64)
    b2 = fonk2(b2)
    b3 = conversion.primary_key_to_subkeys(b13)
    b4 = []
    for block in b2:
        left_half, b5 = block[:32], block[32:]
        for i in range(16):
            left_half, b5 = fonk3(b5, left_half, b3[i])
        b6 = permutations.permutation(b5 + left_half, "inverse")
        b4.append(b6)
    return ''.join(b4)
def fonk2(blocks):
    b7 = len(blocks[-1])
    if b7 < 64:
        blocks[-1] += '0' * (64 - b7)
    return blocks
def fonk3(b5, left_half, subkey):
    b8 = permutations.permutation(b5, "expansion")
    b9 = misc.XOR(b8, subkey)
    b10 = permutations.sBox_permutation(b9)
    b11 = permutations.permutation(b10, "pBox")
    return b5, misc.binary_addition(left_half, b11, 32)
b12 = "Hello, World!"
b13 = "123456789ABCDEF0"
b14 = fonk1(b12, b13)
print("Encrypted b12:", b14)