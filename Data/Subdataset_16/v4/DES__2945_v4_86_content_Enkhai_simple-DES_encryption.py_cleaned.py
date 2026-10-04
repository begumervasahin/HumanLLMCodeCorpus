import textwrap
import conversion
import permutations
import misc
def fonk1(text, key):
    b1 = misc.text_to_bits(text)
    b2 = textwrap.wrap(b1, 64)
    b2[-1] = b2[-1].ljust(64, '0')
    b3 = conversion.primary_key_to_subkeys(key)
    for i, b4 in enumerate(b2):
        b4 = permutations.permutation(b4, "initial")
        left_part, b5 = b4[:32], b4[32:]
        for round_index in range(16):
            left_part, b5 = b5, misc.binary_addition(left_part, fonk2(b5, b3[round_index]), 32)
        b2[i] = permutations.permutation(b5 + left_part, "inverse")
    return ''.join(b2)
def fonk2(b5, subkey):
    b6 = permutations.permutation(b5, "expansion")
    b7 = misc.XOR(b6, subkey)
    b8 = permutations.sBox_permutation(b7)
    b9 = permutations.permutation(b8, "pBox")
    return b9
def fonk3():
    b10 = "Your b10 here"
    b11 = "Your key here"
    b12 = fonk1(b10, b11)
    print("Encrypted text:", b12)
if b13 = = "__main__":
    fonk3()