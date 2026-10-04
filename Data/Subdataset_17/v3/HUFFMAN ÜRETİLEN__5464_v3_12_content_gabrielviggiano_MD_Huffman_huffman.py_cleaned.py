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
        return f"Node(content={self.content}, frequency={self.frequency}, binary={self.binary})"
    def is_leaf(self):
        return self.left is None and self.right is None
class NodeList:
    def __init__(self, text):
        self.text = text
        self.nodes = []
    def create_list(self):
        frequency_map = Counter(self.text)
        self.nodes = [Node(char, freq) for char, freq in frequency_map.items()]
        self.nodes.sort(key=lambda n: n.frequency)
    def build_tree(self):
        self.create_list()
        while len(self.nodes) > 1:
            left = self.nodes.pop(0)
            right = self.nodes.pop(0)
            merged_node = Node(None, left.frequency + right.frequency, left=left, right=right)
            self.nodes.append(merged_node)
            self.nodes.sort(key=lambda n: n.frequency)
class HuffmanTree:
    def encode(self, node):
        if node is None:
            return
        if node.left:
            node.left.binary = node.binary + '0'
            self.encode(node.left)
        if node.right:
            node.right.binary = node.binary + '1'
            self.encode(node.right)
    def get_binary_code(self, node, char):
        if node.is_leaf():
            return node.binary if node.content == char else None
        left_code = self.get_binary_code(node.left, char) if node.left else None
        right_code = self.get_binary_code(node.right, char) if node.right else None
        return left_code or right_code
    def text_to_binary(self, node, text):
        return ''.join(self.get_binary_code(node, char) for char in text)
    def decode(self, node, binary_text):
        current_node = node
        decoded_text = []
        for bit in binary_text:
            current_node = current_node.left if bit == '0' else current_node.right
            if current_node.is_leaf():
                decoded_text.append(current_node.content)
                current_node = node
        return ''.join(decoded_text)
    def display_table(self, node):
        if node is None:
            return
        if node.is_leaf():
            print(node)
        else:
            self.display_table(node.left)
            self.display_table(node.right)
def load_frequencies(text):
    return Counter(text)
def open_file(filename):
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"File not found: {filename}")
    with open(filename, "r") as file:
        return file.read()
def create_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
def main():
    filename = input("Enter the filename containing the text to be compressed: ")
    try:
        text = open_file(filename)
    except FileNotFoundError as e:
        print(e)
        return
    node_list = NodeList(text)
    node_list.build_tree()
    huffman_tree = HuffmanTree()
    huffman_tree.encode(node_list.nodes[0])
    print("\n--- Huffman Code Execution ---")
    print("Original Text:", text)
    frequencies = load_frequencies(text)
    print("\nCharacter Frequencies:")
    print(frequencies)
    print("\nHuffman Tree Table:")
    huffman_tree.display_table(node_list.nodes[0])
    binary_code = huffman_tree.text_to_binary(node_list.nodes[0], text)
    print("\nCompressed Binary:", binary_code)
    decompressed_text = huffman_tree.decode(node_list.nodes[0], binary_code)
    print("\nDecompressed Text:", decompressed_text)
    output_content = (f"Original Text: {text}\n"
                      f"Compressed Binary: {binary_code}\n"
                      f"Decompressed Text: {decompressed_text}\n")
    create_file("result.txt", output_content)
    print("\nOutput file generated successfully!")
if __name__ == '__main__':
    main()