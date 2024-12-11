import permutationMappings
import textwrap
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
    try:
        return ''.join([data[b4 - 1] for b4 in b1])
    except IndexError:
        print("Wrong permutation type!")
def fonk2(data):
    b3 = textwrap.wrap(data, 6)
    for block_num, b6 in enumerate(b3):
        b1 = permutationMappings.sBox_perm_map[block_num]
        b4 = int(b6[0] + b6[5], 2)
        b5 = int(''.join([b6[x] for x in range(1, 5)]), 2)
        b6 = format(b1[b4][b5], '04b')
        b3[block_num] = b6
    return ''.join(b3)