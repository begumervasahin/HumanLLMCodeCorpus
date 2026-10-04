import textwrap
import conversion
import permutations
import misc
def fonk1(text, key):
    b1 = misc.text_to_bits(text)
    b2 = textwrap.wrap(b1, 64)
    b2[-1] = b2[-1].ljust(64, '0')
    b3 = conversion.primary_key_to_subkeys(key)
    b4 = []
    for b6 in b2:
        b5 = fonk2(b6, b3)
        b4.append(b5)
    return ''.join(b4)
def fonk2(b6, b3):
    b6 = permutations.permutation(b6, "initial")
    left_part, b7 = b6[:32], b6[32:]
    for round_index in range(16):
        left_part, b7 = b7, misc.binary_addition(left_part, fonk3(b7, b3[round_index]), 32)
    b5 = permutations.permutation(b7 + left_part, "inverse")
    return b5
def fonk3(b7, subkey):
    b8 = permutations.permutation(b7, "expansion")
    b9 = misc.XOR(b8, subkey)
    b10 = permutations.sBox_permutation(b9)
    b11 = permutations.permutation(b10, "pBox")
    return b11
def fonk4():
    b12 = "Your b12 here"
    b13 = "Your key here"
    b14 = fonk1(b12, b13)
    print("Encrypted text:", b14)
if b15 = = "__main__":
    fonk4()