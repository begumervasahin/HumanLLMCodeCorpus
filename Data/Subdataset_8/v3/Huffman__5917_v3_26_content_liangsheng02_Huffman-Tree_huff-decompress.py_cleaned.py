import os
import pickle
import argparse
import time
class Node:
    def __init__(self, char=None):
        self.char = char
        self.left = None
        self.right = None
class HuffmanDecoder:
    def __init__(self, file):
        self.file_name = os.path.splitext(file)[0]
        self.text_code, self.text_string = self._read_compressed_file()
        self.root = self._build_huffman_tree()
        self.final_text = self._decompress_text()
        print('Decompression completed:', len(self.final_text), 'characters')
    def _read_compressed_file(self):
        with open(self.file_name + '-symbol-model.pkl', 'rb') as f:
            text_code = pickle.load(f)
        with open(self.file_name + '.bin', 'rb') as f:
            padding = text_code.pop('padding_length')
            text_bin = f.read()
        text_string = ''.join(format(byte, '08b') for byte in text_bin)[:-padding]
        return text_code, text_string
    def _build_huffman_tree(self):
        root = Node()
        for char, code in self.text_code.items():
            node = root
            for bit in code:
                if bit == '0':
                    if node.left is None:
                        node.left = Node()
                    node = node.left
                else:
                    if node.right is None:
                        node.right = Node()
                    node = node.right
            node.char = char
        return root
    def _decompress_text(self):
        final_text = ''
        current_node = self.root
        for bit in self.text_string:
            current_node = current_node.left if bit == '0' else current_node.right
            if current_node.char:
                final_text += current_node.char
                current_node = self.root
        output_file = self.file_name + "-decompressed.txt"
        with open(output_file, 'w', encoding='utf-8', newline='\n') as f:
            f.write(final_text)
        return final_text
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', type=str, help="Input file to decompress (with or without extension)")
    args = parser.parse_args()
    start_time = time.time()
    decompress = HuffmanDecoder(args.infile)
    end_time = time.time()
    print("Decoding time:", end_time - start_time)