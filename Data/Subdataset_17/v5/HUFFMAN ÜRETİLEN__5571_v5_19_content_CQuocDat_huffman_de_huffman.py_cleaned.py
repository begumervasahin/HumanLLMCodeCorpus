import numpy as np
import cv2
class Node:
    def __init__(self):
        self.grayvalue = None
        self.isleaf = False
        self.id = None
        self.left = None
        self.right = None
def build_tree(root, code, grayvalue, index=0):
    if index == len(code):
        root.grayvalue = grayvalue
        root.isleaf = True
        return
    bit = code[index]
    if bit == 0:
        if root.left is None:
            root.left = Node()
        build_tree(root.left, code, grayvalue, index + 1)
    elif bit == 1:
        if root.right is None:
            root.right = Node()
        build_tree(root.right, code, grayvalue, index + 1)
def find_leaf(node, code, index):
    if node.isleaf:
        return node.grayvalue, index
    bit = code[index]
    if bit == '0':
        return find_leaf(node.left, code, index + 1)
    elif bit == '1':
        return find_leaf(node.right, code, index + 1)
def decompress_image(dictionary_file, image_file):
    root = Node()
    with open(dictionary_file, 'r') as dict_file:
        tree_data = [line.split() for line in dict_file]
    width = int(tree_data.pop(-1)[0])
    height = int(tree_data.pop(-1)[0])
    for grayvalue, code in enumerate(tree_data):
        binary_code = [int(bit) for bit in code[0]]
        build_tree(root, binary_code, grayvalue)
    image_data = []
    with open(image_file, 'r') as file:
        for line in file:
            code = list(line.strip())
            idx = 0
            row = []
            while idx < len(code):
                grayvalue, idx = find_leaf(root, code, idx)
                row.append(grayvalue)
            image_data.append(row)
    img = np.array(image_data, dtype=np.uint8)
    cv2.imshow('Decompressed Image', img)
    cv2.imwrite('decompressed_image.png', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == "__main__":
    decompress_image('dictionary_meo.txt', 'imageinBit_meo.txt')