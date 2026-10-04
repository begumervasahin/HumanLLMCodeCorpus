import numpy as np
import cv2
class Node:
    def __init__(self):
        self.grayvalue = None
        self.isleaf = False
        self.left = None
        self.right = None
def build_tree(root, bit_sequence, grayscale_value):
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
    root.grayvalue = grayscale_value
def decode_bitstring(bit_string, node):
    if node.isleaf:
        return node.grayvalue, 0
    next_node = node.left if bit_string[0] == '0' else node.right
    return decode_bitstring(bit_string[1:], next_node)
def load_image_dimensions(tree_array):
    height = int(''.join(map(str, tree_array.pop())))
    width = int(''.join(map(str, tree_array.pop())))
    return height, width
def main():
    with open('dictionary_meo.txt', 'r') as dict_file, open('imageinBit_meo.txt', 'r') as bit_file:
        tree_array = [list(map(int, line.split()[1].strip())) for line in dict_file]
        height, width = load_image_dimensions(tree_array)
        print(f"Image dimensions: {height}x{width}")
        root = Node()
        for grayscale_value, bit_sequence in enumerate(tree_array):
            build_tree(root, bit_sequence, grayscale_value)
        image = []
        for line in bit_file:
            bit_string = line.strip()
            decoded_row = []
            i = 0
            while i < len(bit_string):
                gray_value, length = decode_bitstring(bit_string[i:], root)
                decoded_row.append(gray_value)
                i += length + 1
            image.append(decoded_row)
        image = np.array(image, dtype=np.uint8).reshape((height, width))
        cv2.imshow('Decompressed Image', image)
        cv2.imwrite('meo-decompress.png', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
if __name__ == "__main__":
    main()