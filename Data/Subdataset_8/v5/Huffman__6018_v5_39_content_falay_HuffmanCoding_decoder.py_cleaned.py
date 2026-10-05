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
        if not os.path.exists(source) or not os.path.isfile(source):
            self.error_message(f"{source} does not exist or is not a file.")
        self.HuffmanTreeRoot = self.TreeNode()
        self.source = source
        self.target = target
        self.code_map = {}
        self.encoded_text = ""
        self.padding_len = 0
    def parse_encoded_file(self):
        with open(self.source) as encoded_file:
            serialized_map, self.encoded_text, self.padding_len = encoded_file.read().split('\n')
            self.code_map = json.loads(serialized_map)
    def build_code_tree(self):
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
    def traverse_tree(self):
        byte_stream = ""
        for char in self.encoded_text:
            byte = bin(ord(char))[2:]
            byte = '0' * (8 - len(byte)) + byte if len(byte) < 8 else byte
            byte_stream += byte
        byte_stream = byte_stream[:-int(self.padding_len)]
        decoded_text = ""
        current_node = self.HuffmanTreeRoot
        for bit in byte_stream:
            if bit == '0':
                current_node = current_node.left
            else:
                current_node = current_node.right
            if current_node.char is not None:
                decoded_text += current_node.char
                current_node = self.HuffmanTreeRoot
        with open(self.target, 'w') as decoded_file:
            decoded_file.write(decoded_text)
        print('Huffman decoding successful.')
    @staticmethod
    def error_message(message):
        print(message)
        sys.exit(0)
def decode(source, target):
    decoder = HuffmanDecoder(source, target)
    decoder.parse_encoded_file()
    decoder.build_code_tree()
    decoder.traverse_tree()
if __name__ == '__main__':
    if len(sys.argv) != 3:
        HuffmanDecoder.error_message('Usage: python ' + sys.argv[0] + ' [encoded text path] [decoded text path]')
    decode(source=sys.argv[1], target=sys.argv[2])