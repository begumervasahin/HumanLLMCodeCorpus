import textwrap
import conversion
import permutations
import misc
def fonk1(b8, b9):
    b1 = misc.text_to_bits(b8)
    b2 = textwrap.wrap(b1, 64)
    b3 = len(b2[-1])
    if b3 < 64:
        b2[-1] += '0' * (64 - b3)
    b4 = conversion.primary_key_to_subkeys(b9)
    b5 = []
    for block in b2:
        lpt, b6 = permutations.permutation(block, "initial")[:32], permutations.permutation(block, "initial")[32:]
        for subkey in b4:
            lpt, b6 = b6, misc.binary_addition(lpt, fonk2(b6, subkey), 32)
        b7 = permutations.permutation(b6 + lpt, "inverse")
        b5.append(b7)
    return ''.join(b5)
def fonk2(b6, subkey):
    b6 = permutations.permutation(b6, "expansion")
    b6 = misc.XOR(b6, subkey)
    b6 = permutations.sBox_permutation(b6)
    b6 = permutations.permutation(b6, "pBox")
    return b6
b8 = "Hello, World!"
b9 = "123456789ABCDEF0"
b10 = fonk1(b8, b9)
print("Encrypted b8:", b10)