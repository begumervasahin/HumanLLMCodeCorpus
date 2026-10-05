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
            if node.left is None:
                new_node = Node()
                new_node.id = 0
                node.left = new_node
                new_node.grayvalue = index
                new_node.isleaf = True
                return
        if array[index] == 1:
            if node.right is None:
                new_node = Node()
                new_node.id = 1
                node.right = new_node
                new_node.grayvalue = index
                new_node.isleaf = True
                return
    else:
        if array[index] == 0:
            if node.left is None:
                new_node = Node()
                new_node.id = 0
                node.left = new_node
                new_node.isleaf = False
                build_tree(new_node, array, index + 1)
            else:
                build_tree(node.left, array, index + 1)
        if array[index] == 1:
            if node.right is None:
                new_node = Node()
                new_node.id = 1
                node.right = new_node
                new_node.isleaf = False
                build_tree(new_node, array, index + 1)
            else:
                build_tree(node.right, array, index + 1)
def binary_tree_paths(root):
    if root is None:
        return []
    if root.left is None and root.right is None:
        return [str(root.id)]
    left_subtree = binary_tree_paths(root.left)
    right_subtree = binary_tree_paths(root.right)
    full_subtree = left_subtree + right_subtree
    paths = []
    for leaf in full_subtree:
        paths.append(str(root.id) + '-' + leaf)
    return paths
def find_leaf(mang, node, chiso):
    if node.isleaf:
        e.append(node.grayvalue)
        idx.append(chiso)
        return
    else:
        if mang[chiso] == '0':
            find_leaf(mang, node.left, chiso + 1)
        if mang[chiso] == '1':
            find_leaf(mang, node.right, chiso + 1)
dict_file = open('dictionary_meo.txt', 'r')
image_file = open('imageinBit_meo.txt', 'r')
tree_array = []
for line in dict_file:
    temp = line.split(' ')
    j = list(temp[1].strip())
    for i in range(len(j)):
        j[i] = int(j[i])
    tree_array.append(j)
width = int(''.join(str(e) for e in tree_array.pop()))
height = int(''.join(str(e) for e in tree_array.pop()))
print("Image dimensions:", height, "x", width)
root = Node()
for index in range(len(tree_array)):
    i = 0
    build_tree(root, tree_array[index], index)
image_array = []
for line in image_file:
    image_array.append(line.split())
img = []
for code in image_array:
    code = code[0]
    code = list(code)
    m = 0
    e = []
    idx = []
    while m < len(code) - 1:
        find_leaf(code, root, m)
        m = idx[-1]
    img.append(e)
img = np.array(img, dtype=np.uint8)
cv2.imshow('DECOMPRESS', img)
cv2.imwrite('meo-decompress.png', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
dict_file.close()
image_file.close()