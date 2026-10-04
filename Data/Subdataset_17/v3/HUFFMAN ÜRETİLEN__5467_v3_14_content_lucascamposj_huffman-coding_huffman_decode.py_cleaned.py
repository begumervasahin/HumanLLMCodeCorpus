import sys
import os
import math
from bitstring import BitArray
def read_file_metadata(file_data):
    max_code_length = file_data[:8].uint
    max_code_bits = math.ceil(math.log(max_code_length + 1, 2))
    padding_size = file_data[8:11].uint
    return max_code_length, max_code_bits, padding_size
def parse_symbol_codes(symbols_data, max_code_bits):
    symbols = {}
    pos = 0
    for s in range(256):
        if symbols_data[pos]:
            pos += 1
            code_size = symbols_data[pos:pos + max_code_bits].uint
            code = symbols_data[pos + max_code_bits:pos + max_code_bits + code_size]
            pos += max_code_bits + code_size
            if code_size not in symbols:
                symbols[code_size] = {}
            symbols[code_size][code.bin] = BitArray(uint=s, length=8)
        else:
            pos += 1
    return symbols, pos
def decompress_data(data, symbols, max_code_length, output_file_name):
    with open(output_file_name, "wb") as output_file:
        i = 0
        while i < data.length:
            buffer = data[i:i + max_code_length]
            for size, codes in symbols.items():
                code = buffer[:size]
                if code.bin in codes:
                    codes[code.bin].tofile(output_file)
                    i += size
                    break
def main():
    if len(sys.argv) < 3:
        print("Usage: python decompress.py <input_file> <output_file>")
        return
    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]
    print(f"Input File: {input_file_name}")
    print(f"Input File Size: {os.path.getsize(input_file_name)} Bytes\n")
    print("Reading File...")
    with open(input_file_name, "rb") as input_file:
        file_data = BitArray(bytes=input_file.read())
    max_code_length, max_code_bits, padding_size = read_file_metadata(file_data)
    print("Reading Symbol Codes...")
    symbols_data = file_data[11:]
    symbols, pos = parse_symbol_codes(symbols_data, max_code_bits)
    pos += padding_size
    print("Decompressing Data...")
    data = symbols_data[pos:]
    decompress_data(data, symbols, max_code_length, output_file_name)
    print(f"\nOutput File: {output_file_name}")
    print(f"Output File Size: {os.path.getsize(output_file_name)} Bytes")
if __name__ == "__main__":
    main()