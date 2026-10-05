import permutationMappings
import textwrap
def permutation(data, permutation_type):
    mapping = None
    if permutation_type == "initial":
        mapping = permutationMappings.initial_perm_map
    elif permutation_type == "compression":
        mapping = permutationMappings.compression_perm_map
    elif permutation_type == "expansion":
        mapping = permutationMappings.expansion_perm_map
    elif permutation_type == "pBox":
        mapping = permutationMappings.pBox_perm_map
    elif permutation_type == "inverse":
        mapping = permutationMappings.inverseInitial_perm_map
    try:
        return ''.join([data[i - 1] for i in mapping])
    except IndexError:
        print("Wrong permutation type!")
def sBox_permutation(data):
    blocks = textwrap.wrap(data, 6)
    for block_num, block in enumerate(blocks):
        mapping = permutationMappings.sBox_perm_map[block_num]
        i = int(block[0] + block[5], 2)
        j = int(''.join([block[x] for x in range(1, 5)]), 2)
        block = "{0:b}".format(mapping[i][j]).zfill(4)
        blocks[block_num] = block
    return ''.join(blocks)
data = "110011000011001100001111"
permutation_type = "initial"
permuted_data = permutation(data, permutation_type)
print(f"{permutation_type} permutation result:", permuted_data)
s_box_data = "101010"
s_box_permuted_data = sBox_permutation(s_box_data)
print("S-box permutation result:", s_box_permuted_data)