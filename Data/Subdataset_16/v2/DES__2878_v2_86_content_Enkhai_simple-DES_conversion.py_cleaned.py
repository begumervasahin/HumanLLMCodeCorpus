import misc
import permutations
def fonk1(key):
    b1 = []
    b2 = misc.hex_to_bits(key)
    b2 = ''.join([b2[i:i + 7] for i in range(0, len(b2), 8)])
    b3 = len(b2)
    b4 = b2[:b3]
    b5 = b2[b3:]
    for i in range(16):
        b6 = 1 if i in {0, 1, 8, 15} else 2
        b4 = misc.left_shift(b4, b6)
        b5 = misc.left_shift(b5, b6)
        b7 = b4 + b5
        b1.append(permutations.permutation(b7, "compression"))
    return b1
def fonk2():
    b8 = "133457799BBCDFF1"
    b1 = fonk1(b8)
    print("Subkeys:")
    for idx, subkey in enumerate(b1, 1):
        print(f"Subkey {idx}: {subkey}")
if b9 = = "__main__":
    fonk2()