import os
from collections import Counter
class Node:
    def __init__(self, content, frequency, binary_code='', left=None, right=None):
        self.content = content
        self.frequency = frequency
        self.binary_code = binary_code
        self.left = left
        self.right = right
    def __repr__(self):
        return repr((self.content, self.frequency, self.binary_code))
    def is_leaf(self):
        return self.left is None and self.right is None
class HuffmanTree:
    def encode(self, node):
        if node is None:
            return
        if node.left is not None:
            node.left.binary_code = node.binary_code + '1'
            self.encode(node.left)
        if node.right is not None:
            node.right.binary_code = node.binary_code + '0'
            self.encode(node.right)
    def get_binary_code(self, node, character):
        if node.content == character:
            return node.binary_code
        if node.left:
            code = self.get_binary_code(node.left, character)
            if code:
                return code
        if node.right:
            code = self.get_binary_code(node.right, character)
        return code
    def text_to_binary(self, node, text):
        return ''.join(self.get_binary_code(node, char) for char in text)
    def decode(self, root, binary_text):
        node = root
        decoded_text = ''
        for bit in binary_text:
            node = node.left if bit == '1' else node.right
            if node.is_leaf():
                decoded_text += node.content
                node = root
        return decoded_text
    def print_huffman_table(self, node):
        if node is None:
            return
        if node.left:
            self.print_huffman_table(node.left)
        if node.is_leaf():
            print(node)
        if node.right:
            self.print_huffman_table(node.right)
class NodeList:
    def __init__(self, text):
        self.text = text
        self.root = None
    def insert_root(self, new_node):
        self.root = [new_node]
    def insert_element(self, new_node):
        for node in self.root:
            if node.content == new_node.content:
                node.frequency += 1
                self.root.sort(key=lambda node: node.frequency)
                return
        self.root.append(new_node)
        self.root.sort(key=lambda node: node.frequency)
    def create_node_list(self):
        for char in self.text:
            if self.root is None:
                self.insert_root(Node(char, 1))
            else:
                self.insert_element(Node(char, 1))
    def build_tree(self):
        self.create_node_list()
        while len(self.root) > 1:
            left = self.root.pop(0)
            right = self.root.pop(0)
            new_node = Node('', left.frequency + right.frequency, left=left, right=right)
            self.root.append(new_node)
            self.root.sort(key=lambda node: node.frequency)
def load_frequencies(text):
    return Counter(text)
def read_file(file_name):
    if not os.path.isfile(file_name):
        print("File not found!")
        exit()
    with open(file_name, "r") as file:
        return file.read()
def write_file(file_name, content):
    try:
        with open(file_name, 'w') as file:
            file.write(content)
    except IOError:
        print("Error creating the file!")
def main():
    print("Please enter the file name containing the text to be compressed:")
    file_name = input("File Name: ")
    text = read_file(file_name)
    char_list = list(text)
    huffman_tree = HuffmanTree()
    node_list = NodeList(char_list)
    node_list.build_tree()
    huffman_tree.encode(node_list.root[0])
    print("------------------- HUFFMAN CODING EXECUTION -------------------")
    print("Original Text:", text)
    print("")
    print("Character Frequencies:")
    frequencies = load_frequencies(char_list)
    print(frequencies)
    print("")
    print("Huffman Tree created successfully!")
    print("")
    print("Huffman Table:")
    huffman_tree.print_huffman_table(node_list.root[0])
    print("")
    binary_code = huffman_tree.text_to_binary(node_list.root[0], text)
    print("Text compressed to binary:", binary_code)
    print("")
    decoded_text = huffman_tree.decode(node_list.root[0], binary_code)
    print("Decompressed Text:", decoded_text)
    print("")
    output_content = (f"Original Text: {text}\n"
                      f"Compressed Binary: {binary_code}\n"
                      f"Decompressed Text: {decoded_text}\n")
    write_file("result.txt", output_content)
    print("Output file generated successfully!")
if __name__ == '__main__':
    main()