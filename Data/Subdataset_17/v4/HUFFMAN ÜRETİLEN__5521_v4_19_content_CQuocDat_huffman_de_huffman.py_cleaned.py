import numpy as np
import cv2
class Node:
    def __init__(self):
        self.grayvalue = None
        self.isleaf = None
        self.id = None
        self.left = None
        self.right = None
def build_tree(root, code, index, grayvalue):
    if index == len(code) - 1:
        if code[index] == 0:
            if root.left is None:
                root.left = Node()
                root.left.id = 0
                root.left.grayvalue = grayvalue
                root.left.isleaf = True
        elif code[index] == 1:
            if root.right is None:
                root.right = Node()
                root.right.id = 1
                root.right.grayvalue = grayvalue
                root.right.isleaf = True
    else:
        if code[index] == 0:
            if root.left is None:
                root.left = Node()
                root.left.id = 0
                root.left.isleaf = False
            build_tree(root.left, code, index + 1, grayvalue)
        elif code[index] == 1:
            if root.right is None:
                root.right = Node()
                root.right.id = 1
                root.right.isleaf = False
            build_tree(root.right, code, index + 1, grayvalue)
def find_leaf(node, code, index):
    if node.isleaf:
        return node.grayvalue, index
    else:
        if code[index] == '0':
            return find_leaf(node.left, code, index + 1)
        elif code[index] == '1':
            return find_leaf(node.right, code, index + 1)
def decompress_image(dictionary_file, image_file):
    with open(dictionary_file, 'r') as dict_file:
        tree_data = [line.split() for line in dict_file]
    width = int(''.join(tree_data.pop(-1)))
    height = int(''.join(tree_data.pop(-1)))
    root = Node()
    for index, (_, code) in enumerate(tree_data):
        binary_code = [int(bit) for bit in code.strip()]
        build_tree(root, binary_code, 0, index)
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
    cv2.imshow('DECOMPRESS', img)
    cv2.imwrite('meo-decompress.png', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == "__main__":
    decompress_image('dictionary_meo.txt', 'imageinBit_meo.txt')