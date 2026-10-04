import sys
import os
from collections import defaultdict
import operator
PROBABILITIES_FILE = "result.txt"
CODES_FILE = "codigos.txt"
COMPRESSED_FILE = "comprimido.dat"
INPUT_FILE = sys.argv[2]
def huffman_compressor():
    probabilities = load_probabilities(PROBABILITIES_FILE)
    huffman_codes = generate_huffman_codes(probabilities)
    save_huffman_codes(huffman_codes, CODES_FILE)
    with open(INPUT_FILE, 'r') as infile, open(COMPRESSED_FILE, 'wb') as outfile:
        text_content = infile.read().rstrip().lower()
        encoded_text = encode_text(huffman_codes, text_content)
        padded_encoded_text = pad_encoded_text(encoded_text)
        binary_data = convert_to_binary_array(padded_encoded_text)
        outfile.write(bytes(binary_data))
    display_compression_statistics(INPUT_FILE, COMPRESSED_FILE)
def load_probabilities(filename):
    probabilities = {}
    with open(filename, 'r') as file:
        for line in file:
            symbol, probability = line.split("\t")
            probability = float(probability.strip())
            if symbol not in ["space", "salto"]:
                probabilities[symbol] = probability
    return probabilities
def generate_huffman_codes(probabilities):
    if len(probabilities) == 2:
        return dict(zip(probabilities.keys(), ['0', '1']))
    sorted_probabilities = dict(sorted(probabilities.items(), key=operator.itemgetter(1)))
    key1, key2 = list(sorted_probabilities.keys())[:2]
    p1, p2 = sorted_probabilities.pop(key1), sorted_probabilities.pop(key2)
    sorted_probabilities[key1 + key2] = p1 + p2
    codes = generate_huffman_codes(sorted_probabilities)
    combined_code = codes.pop(key1 + key2)
    codes[key1], codes[key2] = combined_code + '0', combined_code + '1'
    return codes
def save_huffman_codes(huffman_codes, filename):
    with open(filename, "w") as file:
        for symbol, code in huffman_codes.items():
            symbol_display = "salto" if symbol == '\n' else symbol
            file.write(f"{symbol_display}\t{code}\n")
def encode_text(huffman_codes, text):
    return ''.join(huffman_codes[ch] for ch in text if ch in huffman_codes)
def pad_encoded_text(encoded_text):
    padding_size = 8 - len(encoded_text) % 8
    padding_info = f"{padding_size:08b}"
    return padding_info + encoded_text + '0' * padding_size
def convert_to_binary_array(padded_encoded_text):
    return bytearray(int(padded_encoded_text[i:i+8], 2) for i in range(0, len(padded_encoded_text), 8))
def display_compression_statistics(input_file, output_file):
    original_size = os.path.getsize(input_file) / (1024 * 1024.0)
    compressed_size = os.path.getsize(output_file) / (1024 * 1024.0)
    compression_ratio = (compressed_size / original_size) * 100
    print(f"\n\nOriginal Text: {input_file} Size: {original_size:.2f} MB")
    print(f"Compressed File: {output_file} Size: {compressed_size:.2f} MB")
    print(f"File {input_file} compressed by {round(compression_ratio)}%")
    print("Text successfully compressed!\n\n")
if __name__ == "__main__":
    huffman_compressor()