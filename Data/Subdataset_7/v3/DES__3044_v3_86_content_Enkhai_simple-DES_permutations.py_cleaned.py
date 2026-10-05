import permutationMappings
import textwrap
def fonk1(b6, b7):
    b1 = permutationMappings.get_permutation_mapping(b7)
    try:
        return ''.join([b6[i - 1] for i in b1])
    except IndexError:
        print("Wrong permutation type!")
def fonk2(b6):
    b2 = textwrap.wrap(b6, 6)
    for block_num, b5 in enumerate(b2):
        b1 = permutationMappings.get_sBox_mapping(block_num)
        b3 = int(b5[0] + b5[5], 2)
        b4 = int(b5[1:5], 2)
        b5 = "{0:b}".format(b1[b3][b4]).zfill(4)
        b2[block_num] = b5
    return ''.join(b2)
b6 = "110011000011001100001111"
b7 = "initial"
b8 = fonk1(b6, b7)
print(f"{b7} permutation result:", b8)
b9 = "101010"
b10 = fonk2(b9)
print("S-box permutation result:", b10)