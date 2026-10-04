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
    for i, b5 in enumerate(b2):
        b5 = permutations.permutation(b5, "initial")
        left, b6 = b5[:32], b5[32:]
        for round_index in range(16):
            left, b6 = b6, misc.binary_addition(left, fonk2(b6, b4[round_index]), 32)
        b2[i] = permutations.permutation(b6 + left, "inverse")
    return ''.join(b2)
def fonk2(b6, subkey):
    b7 = permutations.permutation(b6, "expansion")
    b8 = misc.XOR(b7, subkey)
    b9 = permutations.sBox_permutation(b8)
    b10 = permutations.permutation(b9, "pBox")
    return b10
def fonk3():
    b11 = "Your b11 here"
    b12 = "Your key here"
    b13 = fonk1(b11, b12)
    print("Encrypted text:", b13)
if b14 = = "__main__":
    fonk3()