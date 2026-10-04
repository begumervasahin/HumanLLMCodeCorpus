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
        if not (os.path.exists(source) and os.path.isfile(source)):
            self.error_message(f"Error: {source} does not exist.")
        self.HuffmanTreeRoot = self.TreeNode()
        self.source = source
        self.target = target
        self.code_map = {}
        self.encoded_text = ""
        self.padding_len = 0
    def parse_encoded_file(self):
        with open(self.source, 'r') as encoded_file:
            serialized_map, self.encoded_text, self.padding_len = encoded_file.read().split('\n')
            self.code_map = json.loads(serialized_map)
    def build_huffman_tree(self):
        for char, code in self.code_map.items():
            current_node = self.HuffmanTreeRoot
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
        byte_stream = ''.join(f"{ord(char):08b}" for char in self.encoded_text)
        byte_stream = byte_stream[:-int(self.padding_len)]
        decoded_text = []
        current_node = self.HuffmanTreeRoot
        for bit in byte_stream:
            current_node = current_node.left if bit == '0' else current_node.right
            if current_node.char is not None:
                decoded_text.append(current_node.char)
                current_node = self.HuffmanTreeRoot
        with open(self.target, 'w') as decoded_file:
            decoded_file.write(''.join(decoded_text))
        print('Huffman decoding completed successfully.')
    def error_message(self, message):
        print(message)
        sys.exit(1)
def decode_huffman_file(source, target):
    decoder = HuffmanDecoder(source, target)
    decoder.parse_encoded_file()
    decoder.build_huffman_tree()
    decoder.decode_text()
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f"Usage: python {sys.argv[0]} [encoded text path] [decoded text path]")
        sys.exit(1)
    decode_huffman_file(source=sys.argv[1], target=sys.argv[2])