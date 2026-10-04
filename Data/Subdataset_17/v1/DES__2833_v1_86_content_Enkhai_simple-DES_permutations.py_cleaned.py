import textwrap
import permutationMappings
def permutation(data, type):
    mapping = None
    if type == "initial":
        mapping = permutationMappings.initial_perm_map
    elif type == "compression":
        mapping = permutationMappings.compression_perm_map
    elif type == "expansion":
        mapping = permutationMappings.expansion_perm_map
    elif type == "pBox":
        mapping = permutationMappings.pBox_perm_map
    elif type == "inverse":
        mapping = permutationMappings.inverseInitial_perm_map
    if mapping is None:
        raise ValueError("Wrong permutation type!")
    return ''.join([data[i - 1] for i in mapping])
def sBox_permutation(data):
    blocks = textwrap.wrap(data, 6)
    for block_num, block in enumerate(blocks):
        mapping = permutationMappings.sBox_perm_map[block_num]
        i = int(block[0] + block[5], 2)
        j = int(''.join(block[1:5]), 2)
        block = ("{0:b}".format(mapping[i][j])).zfill(4)
        blocks[block_num] = block
    return ''.join(blocks)
def main():
    sample_data = "1100101010110010111010101010101001101010101010110010101010101010"
    permutation_type = "initial"
    permuted_data = permutation(sample_data, permutation_type)
    print(f"Permuted data ({permutation_type}): {permuted_data}")
    sbox_permuted_data = sBox_permutation(sample_data)
    print(f"S-Box permuted data: {sbox_permuted_data}")
if __name__ == "__main__":
    main()