import os
class Node:
    def __init__(self, frequency, char=None):
        self.frequency = frequency
        self.char = char
        self.left = None
        self.right = None
    def is_leaf(self):
        return self.left is None and self.right is None
class HuffmanTree:
    def __init__(self, frequency_dict):
        self.frequency_dict = frequency_dict
        self.code_dict = {}
        self.reverse_dict = {}
        self.root = self.build_tree()
    def build_tree(self):
        nodes = [Node(freq, char) for char, freq in self.frequency_dict.items()]
        while len(nodes) > 1:
            nodes.sort(key=lambda node: node.frequency)
            left = nodes.pop(0)
            right = nodes.pop(0)
            merged_node = Node(left.frequency + right.frequency)
            merged_node.left = left
            merged_node.right = right
            nodes.append(merged_node)
        return nodes[0] if nodes else None
    def assign_codes(self, node=None, code=""):
        if node is None:
            node = self.root
        if node.is_leaf():
            self.code_dict[node.char] = code
            self.reverse_dict[code] = node.char
            print(f"Character: {repr(node.char)}, Code: {code}")
        else:
            self.assign_codes(node.left, code + "0")
            self.assign_codes(node.right, code + "1")
    def decode_message(self, encoded_message):
        current_node = self.root
        decoded_text = []
        for bit in encoded_message:
            current_node = current_node.left if bit == '0' else current_node.right
            if current_node.is_leaf():
                decoded_text.append(current_node.char)
                current_node = self.root
        return ''.join(decoded_text)
    def encode_file(self, input_path, output_path):
        with open(input_path, 'r') as infile, open(output_path, 'w') as outfile:
            for code, char in self.reverse_dict.items():
                outfile.write(f"{code}.-.{repr(char)}\n")
            outfile.write("```\n")
            while (char := infile.read(1)):
                outfile.write(self.code_dict[char])
    def decode_file(self, encoded_path):
        with open(encoded_path, 'r') as file:
            for line in file:
                if line.strip() == "```":
                    break
            encoded_message = file.read()
            decoded_message = self.decode_message(encoded_message)
            print("\nDecoded Message:", decoded_message)
            return decoded_message
def count_characters(file_path):
    frequency_dict = {}
    with open(file_path, 'r') as file:
        while (char := file.read(1)):
            frequency_dict[char] = frequency_dict.get(char, 0) + 1
    return frequency_dict
def main():
    input_path = 'path/to/your/input.txt'
    output_path = 'path/to/your/output.txt'
    char_frequencies = count_characters(input_path)
    huffman_tree = HuffmanTree(char_frequencies)
    huffman_tree.assign_codes()
    huffman_tree.encode_file(input_path, output_path)
    print("\nReverse Dictionary:", huffman_tree.reverse_dict)
    huffman_tree.decode_file(output_path)
if __name__ == "__main__":
    main()