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
        self.text_code, self.text_string = self._load_files()
        self.root = self._build_tree()
        self.final_text = self._decompress()
        print(f'Decompression complete: {len(self.final_text)} characters')
    def _load_files(self):
        with open(f"{self.file}-symbol-model.pkl", 'rb') as model_file:
            text_code = pickle.load(model_file)
        padding = text_code.pop('padding_length')
        with open(f"{self.file}.bin", 'rb') as binary_file:
            text_bin = binary_file.read()
        text_string = ''.join(f"{byte:08b}" for byte in text_bin)[:-padding]
        return text_code, text_string
    def _build_tree(self):
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
            node = node.left if bit == '0' else node.right
            if node.char:
                final_text.append(node.char)
                node = self.root
        decompressed_text = ''.join(final_text)
        output_path = f"{self.file}-decompressed.txt"
        with open(output_path, 'w', encoding='utf-8', newline='\n') as output_file:
            output_file.write(decompressed_text)
        return decompressed_text
def main():
    parser = argparse.ArgumentParser(description="Huffman Decompression")
    parser.add_argument('infile', type=str, help="Input file for Huffman decompression (without extension)")
    args = parser.parse_args()
    start_time = time.time()
    HuffmanDecoder(args.infile)
    elapsed_time = time.time() - start_time
    print(f"Time taken to decode the compressed file: {elapsed_time:.2f} seconds")
if __name__ == '__main__':
    main()