import os
from collections import Counter
class Node:
    def __init__(self, content, frequency, binary='', left=None, right=None):
        self.content = content
        self.frequency = frequency
        self.binary = binary
        self.left = left
        self.right = right
    def __repr__(self):
        return repr((self.content, self.frequency, self.binary))
    def is_leaf(self):
        return self.left is None and self.right is None
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
                self.root = sorted(self.root, key=lambda x: x.frequency)
                return
        self.root.append(new_node)
        self.root = sorted(self.root, key=lambda x: x.frequency)
    def create_list(self):
        for char in self.text:
            if not self.root:
                self.insert_root(Node(char, 1, ''))
            else:
                self.insert_element(Node(char, 1, ''))
    def build_tree(self):
        self.create_list()
        while len(self.root) > 1:
            left_node = self.root.pop(0)
            right_node = self.root.pop(0)
            merged_node = Node("", left_node.frequency + right_node.frequency, '', left_node, right_node)
            self.root.append(merged_node)
            self.root = sorted(self.root, key=lambda x: x.frequency)
class HuffmanTree:
    def encode(self, node):
        if node is None:
            return
        if node.left:
            node.left.binary = node.binary + '1'
            self.encode(node.left)
        if node.right:
            node.right.binary = node.binary + '0'
            self.encode(node.right)
    def get_binary_code(self, tree, char):
        if tree.content == char:
            return tree.binary
        binary = ''
        if tree.left:
            binary = self.get_binary_code(tree.left, char)
        if binary == '' and tree.right:
            binary = self.get_binary_code(tree.right, char)
        return binary
    def text_to_binary(self, tree, text):
        return ''.join([self.get_binary_code(tree, char) for char in text])
    def decode(self, tree, binary_text):
        current_node = tree
        decoded_text = ''
        for bit in binary_text:
            if bit == '1':
                current_node = current_node.left
            else:
                current_node = current_node.right
            if current_node.is_leaf():
                decoded_text += current_node.content
                current_node = tree
        return decoded_text
    def display_table(self, node):
        if node is None:
            return
        if node.left:
            self.display_table(node.left)
        if node.is_leaf():
            print(node)
        if node.right:
            self.display_table(node.right)
def load_frequencies(text):
    return Counter(text)
def open_file(filename):
    if not os.path.isfile(filename):
        print("File not found!")
        exit()
    else:
        with open(filename, "r") as file:
            return file.read()
def create_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
    except IOError:
        print("Error creating the file!")
def main():
    print("TO START THE PROGRAM, ENTER THE NAME OF THE FILE CONTAINING THE TEXT TO BE COMPRESSED")
    filename = input("Filename: ")
    text = open_file(filename)
    char_list = list(text)
    huffman_tree = HuffmanTree()
    node_list = NodeList(char_list)
    node_list.build_tree()
    huffman_tree.encode(node_list.root[0])
    print("--------------------- HUFFMAN CODE EXECUTION ---------------------")
    print("Inserted text:", text)
    print("")
    frequencies = load_frequencies(char_list)
    print("Character frequencies:")
    print(frequencies)
    print("")
    print("Tree built successfully!")
    print("")
    print("Huffman table:")
    huffman_tree.display_table(node_list.root[0])
    print("")
    binary_code = huffman_tree.text_to_binary(node_list.root[0], node_list.text)
    print("Text compressed to binary:", binary_code)
    print("")
    decompressed_text = huffman_tree.decode(node_list.root[0], binary_code)
    print("Decompressed text:", decompressed_text)
    print("")
    create_file("result.txt", f"Inserted text: {text}\nCompressed binary: {binary_code}\nDecompressed text: {decompressed_text}\n")
    print("Output file generated successfully!")
if __name__ == '__main__':
    main()