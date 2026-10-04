import os
from collections import Counter
class Node:
    def __init__(self, frequency, char=None):
        self.left = None
        self.right = None
        self.frequency = frequency
        self.char = char
    def is_leaf(self):
        return self.left is None and self.right is None
class BinaryTree:
    def __init__(self, frequency_list):
        self.frequency_list = frequency_list
        self.code_dict = {}
        self.reverse_dict = {}
    def create_tree(self):
        nodes = [Node(freq, char) for char, freq in self.frequency_list.items()]
        while len(nodes) > 1:
            nodes.sort(key=lambda node: node.frequency)
            left = nodes.pop(0)
            right = nodes.pop(0)
            new_node = Node(left.frequency + right.frequency)
            new_node.left = left
            new_node.right = right
            nodes.append(new_node)
        return nodes[0]
    def generate_codes(self, node, encoded=""):
        if node is None:
            return
        if node.is_leaf():
            self.code_dict[node.char] = encoded
            self.reverse_dict[encoded] = node.char
            print(f'Character: {node.char}, Code: {encoded}')
            return
        self.generate_codes(node.left, encoded + "1")
        self.generate_codes(node.right, encoded + "0")
    def encode_message(self, input_file, output_file):
        with open(input_file, 'r') as input_f, open(output_file, 'w') as output_f:
            for char, code in self.code_dict.items():
                output_f.write(f'{char if char != "\n" else "\\n"} -> {code}\n')
            output_f.write('```\n')
            total_bits = 0
            for char in input_f.read():
                encoded_char = self.code_dict[char]
                output_f.write(encoded_char)
                total_bits += len(encoded_char)
        print(f'Number of bits: {total_bits / 8:.2f} bytes')
    def decode_message(self, encoded_file, root):
        with open(encoded_file, 'r') as file:
            encoded_message = file.read().split('```')[-1].strip()
        decoded_message = ''
        node = root
        for bit in encoded_message:
            node = node.left if bit == '1' else node.right
            if node.is_leaf():
                decoded_message += node.char
                node = root
        print("Decoded Message:", decoded_message)
def count_chars(file_location):
    with open(file_location, 'r') as file:
        return Counter(file.read())
def main():
    input_file = '/path/to/your/input.txt'
    output_file = '/path/to/your/output.txt'
    frequency_list = count_chars(input_file)
    tree = BinaryTree(frequency_list)
    root_node = tree.create_tree()
    tree.generate_codes(root_node)
    tree.encode_message(input_file, output_file)
    tree.decode_message(output_file, root_node)
if __name__ == '__main__':
    main()