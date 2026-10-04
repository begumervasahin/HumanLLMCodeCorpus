import misc
import permutations
def fonk1(key):
    b1 = []
    b2 = misc.hex_to_bits(key)
    b2 = ''.join([b2[i:i + 7] for i in range(0, len(b2), 8)])
    b3 = len(b2)
    b4 = b2[:b3]
    b5 = b2[b3:]
    for round_index in range(16):
        b6 = 1 if round_index in {0, 1, 8, 15} else 2
        b4 = misc.left_shift(b4, b6)
        b5 = misc.left_shift(b5, b6)
        b7 = b4 + b5
        b8 = permutations.permutation(b7, "compression")
        b1.append(b8)
    return b1
def fonk2():
    b9 = "133457799BBCDFF1"
    b1 = fonk1(b9)
    print("Subkeys:")
    for idx, b8 in enumerate(b1, 1):
        print(f"Subkey {idx}: {b8}")
if b10 = = "__main__":
    fonk2()