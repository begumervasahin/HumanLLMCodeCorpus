import textwrap
import permutationMappings
def permutation(data, type):
    mappings = {
        "initial": permutationMappings.initial_perm_map,
        "compression": permutationMappings.compression_perm_map,
        "expansion": permutationMappings.expansion_perm_map,
        "pBox": permutationMappings.pBox_perm_map,
        "inverse": permutationMappings.inverseInitial_perm_map
    }
    if type not in mappings:
        raise ValueError("Wrong permutation type!")
    mapping = mappings[type]
    return ''.join([data[i - 1] for i in mapping])
def sBox_permutation(data):
    blocks = textwrap.wrap(data, 6)
    for block_num, block in enumerate(blocks):
        mapping = permutationMappings.sBox_perm_map[block_num]
        i = int(block[0] + block[5], 2)
        j = int(''.join(block[1:5]), 2)
        blocks[block_num] = f"{mapping[i][j]:04b}"
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