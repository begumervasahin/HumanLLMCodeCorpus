import textwrap
import permutationMappings
def fonk1(data, type):
    b1 = {
        "initial": permutationMappings.initial_perm_map,
        "compression": permutationMappings.compression_perm_map,
        "expansion": permutationMappings.expansion_perm_map,
        "pBox": permutationMappings.pBox_perm_map,
        "inverse": permutationMappings.inverseInitial_perm_map
    }
    if type not in b1:
        raise ValueError("Wrong permutation type!")
    b2 = b1[type]
    return ''.join([data[b4 - 1] for b4 in b2])
def fonk2(data):
    b3 = textwrap.wrap(data, 6)
    for block_num, block in enumerate(b3):
        b2 = permutationMappings.sBox_perm_map[block_num]
        b4 = int(block[0] + block[5], 2)
        b5 = int(''.join(block[1:5]), 2)
        b3[block_num] = f"{b2[b4][b5]:04b}"
    return ''.join(b3)
def fonk3():
    b6 = "1100101010110010111010101010101001101010101010110010101010101010"
    b7 = "initial"
    b8 = fonk1(b6, b7)
    print(f"Permuted data ({b7}): {b8}")
    b9 = fonk2(b6)
    print(f"S-Box permuted data: {b9}")
if b10 = = "__main__":
    fonk3()