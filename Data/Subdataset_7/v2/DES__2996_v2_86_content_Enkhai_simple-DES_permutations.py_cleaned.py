import permutationMappings
import textwrap
def fonk1(b7, b2):
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
    try:
        return ''.join([b7[b4 - 1] for b4 in b1])
    except IndexError:
        print("Wrong permutation type!")
def fonk2(b7):
    b3 = textwrap.wrap(b7, 6)
    for block_num, b6 in enumerate(b3):
        b1 = permutationMappings.sBox_perm_map[block_num]
        b4 = int(b6[0] + b6[5], 2)
        b5 = int(''.join([b6[x] for x in range(1, 5)]), 2)
        b6 = "{0:b}".format(b1[b4][b5]).zfill(4)
        b3[block_num] = b6
    return ''.join(b3)
b7 = "110011000011001100001111"
b2 = "initial"
b8 = fonk1(b7, b2)
print(f"{b2} permutation result:", b8)
b9 = "101010"
b10 = fonk2(b9)
print("S-box permutation result:", b10)