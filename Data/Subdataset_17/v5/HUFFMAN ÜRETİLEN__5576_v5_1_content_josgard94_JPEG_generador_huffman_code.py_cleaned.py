
import sys
import os
import operator
from collections import defaultdict
PROBABILITIES_FILE = "result.txt"
COMPRESSED_FILE = "comprimido.dat"
CODES_FILE = "codigos.txt"
def huffman_compression(input_file):
    probabilities = load_probabilities(PROBABILITIES_FILE)
    huffman_codes = generate_huffman_codes(probabilities)
    save_codes(huffman_codes, CODES_FILE)
    with open(input_file, 'r') as txt, open(COMPRESSED_FILE, 'wb') as output:
        text = txt.read().rstrip().lower()
        encoded_text = encode_text(huffman_codes, text)
        padded_encoded_text = pad_encoded_text(encoded_text)
        bit_array = generate_bit_array(padded_encoded_text)
        output.write(bytes(bit_array))
def load_probabilities(filename):
    probabilities = {}
    with open(filename, 'r') as file:
        for line in file:
            symbol, probability = line.split("\t")
            if symbol not in {"space", "salto"}:
                probabilities[symbol] = float(probability.strip())
    return probabilities
def generate_huffman_codes(probabilities):
    if len(probabilities) == 2:
        return dict(zip(probabilities.keys(), ['0', '1']))
    probabilities_copy = probabilities.copy()
    sym1, sym2 = get_lowest_probability_symbols(probabilities_copy)
    combined_prob = probabilities_copy.pop(sym1) + probabilities_copy.pop(sym2)
    probabilities_copy[sym1 + sym2] = combined_prob
    codes = generate_huffman_codes(probabilities_copy)
    combined_code = codes.pop(sym1 + sym2)
    codes[sym1] = combined_code + '0'
    codes[sym2] = combined_code + '1'
    return codes
def get_lowest_probability_symbols(probabilities):
    sorted_symbols = sorted(probabilities.items(), key=operator.itemgetter(1))
    return sorted_symbols[0][0], sorted_symbols[1][0]
def save_codes(codes, filename):
    with open(filename, 'w') as file:
        for symbol, code in codes.items():
            symbol_name = "salto" if symbol == '\n' else symbol
            file.write(f"{symbol_name}\t{code}\n")
def encode_text(codes, text):
    return ''.join(codes.get(char, '') for char in text)
def pad_encoded_text(encoded_text):
    padding_size = 8 - len(encoded_text) % 8
    padded_encoded_text = encoded_text + '0' * padding_size
    padding_info = f"{padding_size:08b}"
    return padding_info + padded_encoded_text
def generate_bit_array(binary_string):
    if len(binary_string) % 8 != 0:
        raise ValueError("Binary string length must be a multiple of 8")
    return bytearray(int(binary_string[i:i+8], 2) for i in range(0, len(binary_string), 8))
def display_compression_results(original_file, compressed_file):
    original_size_mb = os.path.getsize(original_file) / (1024 * 1024.0)
    compressed_size_mb = os.path.getsize(compressed_file) / (1024 * 1024.0)
    compression_ratio = (compressed_size_mb / original_size_mb) * 100
    print(f"\n\n------------ Compression Results ------------\n")
    print(f"Original Text: {original_file} | Size: {original_size_mb:.2f} MB")
    print(f"Compressed File: {compressed_file} | Size: {compressed_size_mb:.2f} MB")
    print(f"Compression Ratio: {round(compression_ratio)}%")
    print("Text file compressed successfully!\n\n")
def main():
    if len(sys.argv) < 3 or sys.argv[1] != '-f':
        print("Usage: python generardor_huffman_code.py -f <FILE_TO_COMPRESS>")
        sys.exit(1)
    input_file = sys.argv[2]
    huffman_compression(input_file)
    display_compression_results(input_file, COMPRESSED_FILE)
if __name__ == "__main__":
    main()