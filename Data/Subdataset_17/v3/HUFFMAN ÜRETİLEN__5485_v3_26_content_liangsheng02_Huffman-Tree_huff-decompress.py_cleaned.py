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
    def __init__(self, file_path):
        self.file_path = os.path.splitext(file_path)[0]
        self.symbol_code, self.encoded_string = self._load_files()
        self.root = self._build_tree()
        self.decompressed_text = self._decompress()
        print(f'Decompression complete: {len(self.decompressed_text)} characters')
    def _load_files(self):
        with open(f"{self.file_path}-symbol-model.pkl", 'rb') as model_file:
            symbol_code = pickle.load(model_file)
        padding_length = symbol_code.pop('padding_length')
        with open(f"{self.file_path}.bin", 'rb') as binary_file:
            binary_data = binary_file.read()
        bit_string = ''.join(f"{byte:08b}" for byte in binary_data)[:-padding_length]
        return symbol_code, bit_string
    def _build_tree(self):
        root = Node()
        for char, code in self.symbol_code.items():
            current_node = root
            for bit in code:
                if bit == '0':
                    if not current_node.left:
                        current_node.left = Node()
                    current_node = current_node.left
                else:
                    if not current_node.right:
                        current_node.right = Node()
                    current_node = current_node.right
            current_node.char = char
        return root
    def _decompress(self):
        decoded_text = []
        current_node = self.root
        for bit in self.encoded_string:
            current_node = current_node.left if bit == '0' else current_node.right
            if current_node.char:
                decoded_text.append(current_node.char)
                current_node = self.root
        decompressed_text = ''.join(decoded_text)
        output_file_path = f"{self.file_path}-decompressed.txt"
        self._save_decompressed_text(output_file_path, decompressed_text)
        return decompressed_text
    def _save_decompressed_text(self, file_path, text):
        with open(file_path, 'w', encoding='utf-8', newline='\n') as output_file:
            output_file.write(text)
def main():
    parser = argparse.ArgumentParser(description="Huffman Decompression Tool")
    parser.add_argument('infile', type=str, help="Input file for Huffman decompression (without extension)")
    args = parser.parse_args()
    start_time = time.time()
    HuffmanDecoder(args.infile)
    elapsed_time = time.time() - start_time
    print(f"Time taken to decode the compressed file: {elapsed_time:.2f} seconds")
if __name__ == '__main__':
    main()