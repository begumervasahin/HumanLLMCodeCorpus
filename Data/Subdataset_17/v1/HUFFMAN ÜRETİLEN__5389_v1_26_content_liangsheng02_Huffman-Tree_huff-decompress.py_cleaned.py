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
        self.file = os.path.splitext(file)[0]
        self.text_code, self.text_string = self._readfile()
        self.root = self._to_tree()
        self.final_text = self._decompress()
        print('Decompression complete:', len(self.final_text), 'characters')
    def _readfile(self):
        text_code = pickle.load(open(self.file + '-symbol-model.pkl', 'rb'))
        padding = text_code.pop('padding_length')
        text_bin = open(self.file + '.bin', 'rb').read()
        text_string = (''.join([bin(byte)[2:].zfill(8) for byte in text_bin]))[:-padding]
        return text_code, text_string
    def _to_tree(self):
        root = Node()
        for char, code in self.text_code.items():
            node = root
            for bit in code:
                if bit == '0':
                    if not node.left:
                        node.left = Node()
                    node = node.left
                else:
                    if not node.right:
                        node.right = Node()
                    node = node.right
            node.char = char
        return root
    def _decompress(self):
        final_text = []
        node = self.root
        for bit in self.text_string:
            node = node.left if bit == "0" else node.right
            if node.char:
                final_text.append(node.char)
                node = self.root
        decompressed_text = ''.join(final_text)
        with open(self.file + "-decompressed.txt", 'w', encoding='utf-8', newline='\n') as output_file:
            output_file.write(decompressed_text)
        return decompressed_text
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Huffman Decompression")
    parser.add_argument('infile', type=str, help="Input file for Huffman decompression (without extension)")
    args = parser.parse_args()
    start = time.time()
    HuffmanDecoder(args.infile)
    end = time.time()
    print(f"Time taken to decode the compressed file: {end - start:.2f} seconds")