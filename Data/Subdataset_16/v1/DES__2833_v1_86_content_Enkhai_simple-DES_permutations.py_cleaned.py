import textwrap
import permutationMappings
def fonk1(data, b2):
    b1 = None
    if b2 = = "initial":
        b1 = permutationMappings.initial_perm_map
    elif b2 = = "compression":
        b1 = permutationMappings.compression_perm_map
    elif b2 = = "expansion":
        b1 = permutationMappings.expansion_perm_map
    elif b2 = = "pBox":
        b1 = permutationMappings.pBox_perm_map
    elif b2 = = "inverse":
        b1 = permutationMappings.inverseInitial_perm_map
    if b1 is None:
        raise ValueError("Wrong permutation b2!")
    return ''.join([data[b4 - 1] for b4 in b1])
def fonk2(data):
    b3 = textwrap.wrap(data, 6)
    for block_num, b6 in enumerate(b3):
        b1 = permutationMappings.sBox_perm_map[block_num]
        b4 = int(b6[0] + b6[5], 2)
        b5 = int(''.join(b6[1:5]), 2)
        b6 = ("{0:b}".format(b1[b4][b5])).zfill(4)
        b3[block_num] = b6
    return ''.join(b3)
def fonk3():
    b7 = "1100101010110010111010101010101001101010101010110010101010101010"
    b8 = "initial"
    b9 = fonk1(b7, b8)
    print(f"Permuted data ({b8}): {b9}")
    b10 = fonk2(b7)
    print(f"S-Box permuted data: {b10}")
if b11 = = "__main__":
    fonk3()