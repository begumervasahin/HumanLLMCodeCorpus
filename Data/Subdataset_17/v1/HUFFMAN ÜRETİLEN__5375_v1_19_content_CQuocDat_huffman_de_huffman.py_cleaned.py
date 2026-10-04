import numpy as np
import cv2
class Node:
    def __init__(self):
        self.grayvalue = None
        self.isleaf = None
        self.id = None
        self.left = None
        self.right = None
def tree_builder(root, bit_sequence, i, index):
    if i == len(bit_sequence) - 1:
        if bit_sequence[i] == 0:
            if root.left is None:
                new_node = Node()
                new_node.id = 0
                root.left = new_node
                new_node.grayvalue = index
                new_node.isleaf = True
                return
        if bit_sequence[i] == 1:
            if root.right is None:
                new_node = Node()
                new_node.id = 1
                root.right = new_node
                new_node.grayvalue = index
                new_node.isleaf = True
                return
    else:
        if bit_sequence[i] == 0:
            if root.left is None:
                new_node = Node()
                new_node.id = 0
                root.left = new_node
                new_node.isleaf = False
                tree_builder(new_node, bit_sequence, i + 1, index)
            else:
                tree_builder(root.left, bit_sequence, i + 1, index)
        if bit_sequence[i] == 1:
            if root.right is None:
                new_node = Node()
                new_node.id = 1
                root.right = new_node
                new_node.isleaf = False
                tree_builder(new_node, bit_sequence, i + 1, index)
            else:
                tree_builder(root.right, bit_sequence, i + 1, index)
def find(bit_string, node, chiso):
    if node.isleaf:
        e.append(node.grayvalue)
        idx.append(chiso)
        return
    else:
        if bit_string[chiso] == '0':
            find(bit_string, node.left, chiso + 1)
        if bit_string[chiso] == '1':
            find(bit_string, node.right, chiso + 1)
def main():
    with open('dictionary_meo.txt', 'r') as dict_file, open('imageinBit_meo.txt', 'r') as bit_file:
        tree_array = []
        for line in dict_file:
            temp = line.split(' ')
            bit_seq = list(temp[1].strip())
            bit_seq = [int(bit) for bit in bit_seq]
            tree_array.append(bit_seq)
        width = tree_array.pop()
        height = tree_array.pop()
        width = int(''.join(map(str, width)))
        height = int(''.join(map(str, height)))
        print(f"Image dimensions: {height}x{width}")
        root = Node()
        for index, bit_seq in enumerate(tree_array):
            tree_builder(root, bit_seq, 0, index)
        img = []
        for line in bit_file:
            code = list(line.strip())
            m = 0
            global e, idx
            e = []
            idx = []
            while m < len(code):
                find(code, root, m)
                m = idx[-1] + 1
            img.append(e)
        img = np.array(img, dtype=np.uint8).reshape((height, width))
        cv2.imshow('DECOMPRESS', img)
        cv2.imwrite('meo-decompress.png', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
if __name__ == "__main__":
    main()