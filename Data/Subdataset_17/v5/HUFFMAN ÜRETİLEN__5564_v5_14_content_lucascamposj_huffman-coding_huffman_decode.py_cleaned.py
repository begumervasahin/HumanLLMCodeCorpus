import sys
import os
import math
from bitstring import BitArray
def read_file_data(input_file_name):
    with open(input_file_name, "rb") as file:
        return BitArray(bytes=file.read())
def parse_symbols(symbols_data, max_code_bits):
    symbols = {}
    pos = 0
    for s in range(256):
        if symbols_data[pos]:
            pos += 1
            code_length_bits = symbols_data[pos:pos + max_code_bits].uint
            code = symbols_data[pos + max_code_bits:pos + max_code_bits + code_length_bits]
            pos += max_code_bits + code_length_bits
            if code_length_bits not in symbols:
                symbols[code_length_bits] = {}
            symbols[code_length_bits][code.bin] = BitArray(uint=s, length=8)
        else:
            pos += 1
    return symbols, pos
def decompress_data(data, symbols, max_code_length, output_file_name):
    with open(output_file_name, "wb") as output_file:
        i = 0
        while i < data.length:
            buffer = BitArray(data[i:i + max_code_length])
            for size in symbols:
                code = buffer[:size]
                if code.bin in symbols[size]:
                    symbols[size][code.bin].tofile(output_file)
                    i += size
                    break
def main():
    if len(sys.argv) < 3:
        print("Usage: python decompress.py <input_file> <output_file>")
        return
    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]
    print(f"Input File: {input_file_name}")
    input_file_length = os.path.getsize(input_file_name)
    print(f"File Size: {input_file_length} Bytes")
    print("\nReading File...")
    file_data = read_file_data(input_file_name)
    max_code_length = file_data[:8].uint
    max_code_bits = math.ceil(math.log2(max_code_length + 1))
    padding_size = file_data[8:11].uint
    print("Parsing Symbol Codes...")
    symbols_data = file_data[11:]
    symbols, pos = parse_symbols(symbols_data, max_code_bits)
    pos += padding_size
    print("Decompressing Data...")
    data = symbols_data[pos:]
    decompress_data(data, symbols, max_code_length, output_file_name)
    output_file_length = os.path.getsize(output_file_name)
    print(f"\nOutput File: {output_file_name}")
    print(f"Decompressed File Size: {output_file_length} Bytes")
if __name__ == "__main__":
    main()