import numpy as np
import cv2
class Node:
    def __init__(self):
        self.grayvalue = None
        self.isleaf = None
        self.id = None
        self.left = None
        self.right = None
def build_tree(node, array, index):
    if index == len(array) - 1:
        if array[index] == 0:
            add_leaf_node(node, 0, index)
        if array[index] == 1:
            add_leaf_node(node, 1, index)
    else:
        if array[index] == 0:
            build_child_tree(node, 0, array, index + 1)
        if array[index] == 1:
            build_child_tree(node, 1, array, index + 1)
def add_leaf_node(node, node_id, index):
    child = Node()
    child.id = node_id
    node.left if node_id == 0 else node.right = child
    child.grayvalue = index
    child.isleaf = True
def build_child_tree(node, node_id, array, index):
    if getattr(node, 'left' if node_id == 0 else 'right') is None:
        child = Node()
        child.id = node_id
        setattr(node, 'left' if node_id == 0 else 'right', child)
        child.isleaf = False
        build_tree(child, array, index)
    else:
        build_tree(getattr(node, 'left' if node_id == 0 else 'right'), array, index)
def binary_tree_paths(root):
    if root is None:
        return []
    if root.left is None and root.right is None:
        return [str(root.id)]
    left_subtree = binary_tree_paths(root.left)
    right_subtree = binary_tree_paths(root.right)
    full_subtree = left_subtree + right_subtree
    paths = [str(root.id) + '-' + leaf for leaf in full_subtree]
    return paths
def find_leaf(code, node, index):
    if node.isleaf:
        e.append(node.grayvalue)
        idx.append(index)
        return
    else:
        child_node = node.left if code[index] == '0' else node.right
        find_leaf(code, child_node, index + 1)
dict_file = open('dictionary_meo.txt', 'r')
image_file = open('imageinBit_meo.txt', 'r')
tree_array = []
for line in dict_file:
    temp = line.split(' ')
    tree_array.append([int(bit) for bit in temp[1].strip()])
width, height = map(int, tree_array.pop())
print("Image dimensions:", height, "x", width)
root = Node()
for index, tree_bits in enumerate(tree_array):
    build_tree(root, tree_bits, index)
img = []
for code_line in image_file:
    code = list(code_line[0])
    e, idx = [], []
    find_leaf(code, root, 0)
    img.append(e)
img = np.array(img, dtype=np.uint8)
cv2.imshow('DECOMPRESS', img)
cv2.imwrite('meo-decompress.png', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
dict_file.close()
image_file.close()