import numpy as np
import cv2
class Node:
    def __init__(self):
        self.gray_value = None
        self.is_leaf = None
        self.node_id = None
        self.left = None
        self.right = None
def build_tree(parent_node, bit_array, bit_index, index):
    if bit_index == len(bit_array) - 1:
        if bit_array[bit_index] == 0:
            if parent_node.left is None:
                new_node = Node()
                new_node.node_id = 0
                parent_node.left = new_node
                new_node.gray_value = index
                new_node.is_leaf = True
                return
        elif bit_array[bit_index] == 1:
            if parent_node.right is None:
                new_node = Node()
                new_node.node_id = 1
                parent_node.right = new_node
                new_node.gray_value = index
                new_node.is_leaf = True
                return
    else:
        if bit_array[bit_index] == 0:
            if parent_node.left is None:
                new_node = Node()
                new_node.node_id = 0
                parent_node.left = new_node
                new_node.is_leaf = False
                build_tree(new_node, bit_array, bit_index + 1, index)
            else:
                build_tree(parent_node.left, bit_array, bit_index + 1, index)
        elif bit_array[bit_index] == 1:
            if parent_node.right is None:
                new_node = Node()
                new_node.node_id = 1
                parent_node.right = new_node
                new_node.is_leaf = False
                build_tree(new_node, bit_array, bit_index + 1, index)
            else:
                build_tree(parent_node.right, bit_array, bit_index + 1, index)
def find_leaf_nodes(code, node, index):
    if node.is_leaf:
        leaf_values.append(node.gray_value)
        leaf_indices.append(index)
        return
    else:
        if code[index] == '0':
            find_leaf_nodes(code, node.left, index + 1)
        elif code[index] == '1':
            find_leaf_nodes(code, node.right, index + 1)
dictionary_file = open('dictionary_meo.txt', 'r')
image_file = open('imageinBit_meo.txt', 'r')
tree_array = []
for line in dictionary_file:
    temp = line.split(' ')
    code_list = list(temp[1].rstrip())
    for i in range(len(code_list)):
        code_list[i] = int(code_list[i])
    tree_array.append(code_list)
width = int(''.join(str(e) for e in tree_array.pop()))
height = int(''.join(str(e) for e in tree_array.pop()))
print("Image Dimensions:", height, width)
root_node = Node()
for i in range(len(tree_array)):
    build_tree(root_node, tree_array[i], 0, i)
image_array = []
for line in image_file:
    code = line.split()[0]
    code_list = list(code)
    current_index = 0
    leaf_values = []
    leaf_indices = []
    while current_index < len(code_list) - 1:
        find_leaf_nodes(code_list, root_node, current_index)
        current_index = leaf_indices[-1]
    image_array.append(leaf_values)
image_array = np.array(image_array, dtype=np.uint8)
cv2.imshow('DECOMPRESS', image_array)
cv2.imwrite('meo-decompress.png', image_array)
cv2.waitKey(0)
cv2.destroyAllWindows()