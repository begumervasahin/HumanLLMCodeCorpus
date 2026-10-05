from decimal import Decimal
import sys
import os
import operator
RESULT_PROBABILITIES_FILE = "result.txt"
COMPRESSED_FILE = "compressed.dat"
CODES_FILE = "codes.txt"
def huffman_compressor():
    probabilities = read_probabilities()
    codes_table = generate_huffman_codes(probabilities)
    save_codes(codes_table)
    compress_text(codes_table)
def read_probabilities():
    probabilities = {}
    with open(RESULT_PROBABILITIES_FILE, 'r') as file:
        for line in file:
            key, value = line.strip().split("\t")
            if key not in ["space", "salto"]:
                probabilities[key] = float(value)
    return probabilities
def generate_huffman_codes(probabilities):
    if len(probabilities) == 2:
        return dict(zip(probabilities.keys(), ['0', '1']))
    sorted_probabilities = sorted(probabilities.items(), key=operator.itemgetter(1))
    key1, key2 = sorted_probabilities[0][0], sorted_probabilities[1][0]
    prob1, prob2 = probabilities.pop(key1), probabilities.pop(key2)
    probabilities[key1 + key2] = prob1 + prob2
    codes = generate_huffman_codes(probabilities)
    combined_code = codes.pop(key1 + key2)
    codes[key1], codes[key2] = combined_code + '0', combined_code + '1'
    return codes
def save_codes(codes):
    with open(CODES_FILE, "w") as file:
        for key, value in codes.items():
            key_name = "salto" if key == '\n' else key
            file.write(f"{value}\t{key_name}\n")
def compress_text(codes):
    with open(sys.argv[2], 'r') as text_file, open(COMPRESSED_FILE, 'wb') as output:
        text = text_file.read().rstrip().lower()
        encoded_text = encode_text(codes, text)
        padded_encoded_text = pad_encoded_text(encoded_text)
        bit_array = generate_bit_array(padded_encoded_text)
        output.write(bit_array)
def encode_text(codes, text):
    return ''.join(codes[char] for char in text.split() if char in codes)
def pad_encoded_text(encoded_text):
    padding = 8 - len(encoded_text) % 8
    return f"{padding:08b}" + encoded_text + "0" * padding
def generate_bit_array(binary_string):
    if len(binary_string) % 8 != 0:
        sys.exit(0)
    return bytearray(int(binary_string[i:i+8], 2) for i in range(0, len(binary_string), 8))
if __name__ == "__main__":
    huffman_compressor()
    display_compression_statistics(sys.argv[2])
def display_compression_statistics(input_file):
    original_size = os.path.getsize(input_file) / (1024 * 1024.0)
    compressed_size = os.path.getsize(COMPRESSED_FILE) / (1024 * 1024.0)
    compression_ratio = (compressed_size / original_size) * 100
    print("\nOriginal Text: {} Size: {:.2f} MB".format(input_file, original_size))
    print("Compressed File: {} Size: {:.2f} MB".format(COMPRESSED_FILE, compressed_size))
    print("File {} compressed by {:.2f}%".format(input_file, compression_ratio))
    print("Text file compressed successfully!\n")