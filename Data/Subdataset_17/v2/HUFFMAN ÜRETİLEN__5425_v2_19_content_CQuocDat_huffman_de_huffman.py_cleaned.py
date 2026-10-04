import numpy as np
import cv2
class Node:
    def __init__(self):
        self.grayvalue = None
        self.isleaf = False
        self.left = None
        self.right = None
def tree_builder(root, bit_sequence, index):
    for bit in bit_sequence:
        if bit == 0:
            if root.left is None:
                root.left = Node()
            root = root.left
        else:
            if root.right is None:
                root.right = Node()
            root = root.right
    root.isleaf = True
    root.grayvalue = index
def find(bit_string, node):
    if node.isleaf:
        return node.grayvalue, 0
    if bit_string[0] == '0':
        return find(bit_string[1:], node.left)
    else:
        return find(bit_string[1:], node.right)
def main():
    with open('dictionary_meo.txt', 'r') as dict_file, open('imageinBit_meo.txt', 'r') as bit_file:
        tree_array = []
        for line in dict_file:
            bit_sequence = list(map(int, line.split()[1].strip()))
            tree_array.append(bit_sequence)
        height = int(''.join(map(str, tree_array.pop())))
        width = int(''.join(map(str, tree_array.pop())))
        print(f"Image dimensions: {height}x{width}")
        root = Node()
        for index, bit_sequence in enumerate(tree_array):
            tree_builder(root, bit_sequence, index)
        img = []
        for line in bit_file:
            bit_string = line.strip()
            decoded_row = []
            i = 0
            while i < len(bit_string):
                gray_value, length = find(bit_string[i:], root)
                decoded_row.append(gray_value)
                i += length + 1
            img.append(decoded_row)
        img = np.array(img, dtype=np.uint8).reshape((height, width))
        cv2.imshow('Decompressed Image', img)
        cv2.imwrite('meo-decompress.png', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
if __name__ == "__main__":
    main()