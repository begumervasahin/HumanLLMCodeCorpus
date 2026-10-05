import sys
import os
import math
from bitstring import BitArray
def read_file(input_file_name):
    with open(input_file_name, "rb") as input_file:
        return BitArray(bytes=input_file.read())
def read_symbol_codes(data, max_code_length):
    symbols = {}
    pos = 0
    while pos < len(data):
        symbol_bit = data[pos]
        pos += 1
        if symbol_bit:
            code_size = int(data[pos:pos + max_code_length].uint)
            pos += max_code_length
            code = data[pos:pos + code_size]
            pos += code_size
            if code_size not in symbols:
                symbols[code_size] = {}
            symbols[code_size][code.bin] = BitArray(uint=(pos - code_size - max_code_length - 1), length=8)
        else:
            pos += 1
    return symbols, pos
def write_compressed_data(data, symbols, max_code_length, output_file_name):
    i = 0
    with open(output_file_name, "wb") as output_file:
        while i < len(data):
            buffer = BitArray(data[i:i + max_code_length])
            for size in symbols:
                code = buffer[:size]
                if code.bin in symbols[size]:
                    symbols[size][code.bin].tofile(output_file)
                    break
            i += size
def main():
    if len(sys.argv) <= 2:
        print("Usage: python compress.py <input_file> <output_file>")
        return
    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]
    print("Input File Name:", input_file_name)
    input_file_length_in_bytes = os.path.getsize(input_file_name)
    print("Input File Size:", input_file_length_in_bytes, "Bytes")
    print("\nReading Input File...")
    file_data = read_file(input_file_name)
    max_code_length = int(file_data[:8].uint)
    max_code_bits = int(math.ceil(math.log(max_code_length + 1, 2)))
    padding_size = int(file_data[8:11].uint)
    print("Reading Symbol Codes...")
    symbols_data = file_data[11:]
    symbols, pos = read_symbol_codes(symbols_data, max_code_bits)
    pos += padding_size
    print("Reading and Writing Compressed Data...")
    data = symbols_data[pos:]
    write_compressed_data(data, symbols, max_code_length, output_file_name)
    output_file_length_in_bytes = os.path.getsize(output_file_name)
    print("\nOutput File Name:           ", output_file_name)
    print("Compressed File Size:", output_file_length_in_bytes, "Bytes")
if __name__ == "__main__":
    main()