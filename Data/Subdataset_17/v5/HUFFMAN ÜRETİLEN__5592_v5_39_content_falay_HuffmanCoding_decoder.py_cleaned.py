import os
import sys
import json
class HuffmanDecoder:
    class TreeNode:
        def __init__(self, char=None):
            self.char = char
            self.left = None
            self.right = None
    def __init__(self, source, target):
        self._validate_file(source)
        self.source = source
        self.target = target
        self.huffman_tree_root = self.TreeNode()
        self.code_map = {}
        self.encoded_text = ""
        self.padding_len = 0
    def _validate_file(self, file_path):
        if not os.path.exists(file_path) or not os.path.isfile(file_path):
            self._error_message(f"Error: {file_path} does not exist.")
    def parse_encoded_file(self):
        with open(self.source, 'r') as encoded_file:
            serialized_map, self.encoded_text, padding_len_str = encoded_file.read().split('\n')
            self.code_map = json.loads(serialized_map)
            self.padding_len = int(padding_len_str)
    def build_huffman_tree(self):
        for char, code in self.code_map.items():
            current_node = self.huffman_tree_root
            for bit in code:
                if bit == '0':
                    if current_node.left is None:
                        current_node.left = self.TreeNode()
                    current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = self.TreeNode()
                    current_node = current_node.right
            current_node.char = char
    def decode_text(self):
        byte_stream = ''.join(f"{bin(ord(char))[2:]:0>8}" for char in self.encoded_text)
        byte_stream = byte_stream[:-self.padding_len]
        decoded_text = []
        current_node = self.huffman_tree_root
        for bit in byte_stream:
            current_node = current_node.left if bit == '0' else current_node.right
            if current_node.char:
                decoded_text.append(current_node.char)
                current_node = self.huffman_tree_root
        self._write_decoded_file(decoded_text)
        print("Huffman decoding completed successfully.")
    def _write_decoded_file(self, decoded_text):
        with open(self.target, 'w') as decoded_file:
            decoded_file.write(''.join(decoded_text))
    @staticmethod
    def _error_message(message):
        print(message)
        sys.exit(1)
def main():
    if len(sys.argv) != 3:
        HuffmanDecoder._error_message(f"Usage: python {sys.argv[0]} [encoded text path] [decoded text path]")
    source = sys.argv[1]
    target = sys.argv[2]
    decoder = HuffmanDecoder(source, target)
    decoder.parse_encoded_file()
    decoder.build_huffman_tree()
    decoder.decode_text()
if __name__ == '__main__':
    main()