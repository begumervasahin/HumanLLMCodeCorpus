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
        return f"Node(content='{self.content}', frequency={self.frequency}, binary_code='{self.binary_code}')"
    def is_leaf(self):
        return self.left is None and self.right is None
class HuffmanTree:
    def encode(self, node):
        if node is None:
            return
        if node.left:
            node.left.binary_code = node.binary_code + '1'
            self.encode(node.left)
        if node.right:
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
            return self.get_binary_code(node.right, character)
        return None
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
            print(f"Character: '{node.content}', Code: {node.binary_code}")
        if node.right:
            self.print_huffman_table(node.right)
class NodeList:
    def __init__(self, text):
        self.text = text
        self.nodes = []
    def create_node_list(self):
        frequency = Counter(self.text)
        self.nodes = [Node(char, freq) for char, freq in frequency.items()]
        self.nodes.sort(key=lambda node: node.frequency)
    def build_tree(self):
        self.create_node_list()
        while len(self.nodes) > 1:
            left = self.nodes.pop(0)
            right = self.nodes.pop(0)
            new_node = Node('', left.frequency + right.frequency, left=left, right=right)
            self.nodes.append(new_node)
            self.nodes.sort(key=lambda node: node.frequency)
def load_text(file_name):
    if not os.path.isfile(file_name):
        raise FileNotFoundError(f"File not found: {file_name}")
    with open(file_name, 'r') as file:
        return file.read()
def save_output(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)
def main():
    file_name = input("Please enter the file name containing the text to be compressed: ")
    text = load_text(file_name)
    huffman_tree = HuffmanTree()
    node_list = NodeList(text)
    node_list.build_tree()
    huffman_tree.encode(node_list.nodes[0])
    print("\n------------------- HUFFMAN CODING EXECUTION -------------------")
    print("Original Text:", text)
    print("\nCharacter Frequencies:", Counter(text))
    print("\nHuffman Tree created successfully!")
    print("\nHuffman Table:")
    huffman_tree.print_huffman_table(node_list.nodes[0])
    binary_code = huffman_tree.text_to_binary(node_list.nodes[0], text)
    print("\nText compressed to binary:", binary_code)
    decoded_text = huffman_tree.decode(node_list.nodes[0], binary_code)
    print("\nDecompressed Text:", decoded_text)
    output_content = (f"Original Text: {text}\n"
                      f"Compressed Binary: {binary_code}\n"
                      f"Decompressed Text: {decoded_text}\n")
    save_output("result.txt", output_content)
    print("\nOutput file generated successfully!")
if __name__ == '__main__':
    main()