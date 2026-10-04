import textwrap
import conversion
import permutations
import misc
def fonk1(text, key):
    b1 = misc.text_to_bits(text)
    b2 = textwrap.wrap(b1, 64)
    b3 = b2[-1]
    b2[-1] = b3.ljust(64, '0')
    b4 = conversion.primary_key_to_subkeys(key)
    for part_num, b5 in enumerate(b2):
        b5 = permutations.permutation(b5, "initial")
        left_part, b6 = b5[:32], b5[32:]
        for i in range(16):
            left_part, b6 = b6, misc.binary_addition(left_part, fonk2(b6, b4[i]), 32)
        b2[part_num] = permutations.permutation(b6 + left_part, "inverse")
    return ''.join(b2)
def fonk2(b6, subkey):
    b6 = permutations.permutation(b6, "expansion")
    b6 = misc.XOR(b6, subkey)
    b6 = permutations.sBox_permutation(b6)
    b6 = permutations.permutation(b6, "pBox")
    return b6
def fonk3():
    b7 = "Your b7 here"
    b8 = "Your key here"
    b9 = fonk1(b7, b8)
    print("Encrypted text:", b9)
if b10 = = "__main__":
    fonk3()