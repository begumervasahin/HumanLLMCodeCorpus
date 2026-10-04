import sys
import os
import math
from bitstring import BitArray
def read_file_data(input_file_name):
    with open(input_file_name, "rb") as f:
        return BitArray(bytes=f.read())
def parse_symbols(symbols_data, max_code_bits):
    symbols = {}
    pos = 0
    for s in range(256):
        if symbols_data[pos]:
            pos += 1
            posj = pos + max_code_bits
            code_size = int(symbols_data[pos:posj].uint)
            code = symbols_data[posj:(posj + code_size)]
            pos = posj + code_size
            if code_size not in symbols:
                symbols[code_size] = {}
            symbols[code_size][code.bin] = BitArray(uint=s, length=8)
        else:
            pos += 1
    return symbols, pos
def decompress_data(data, symbols, max_code_length, output_file_name):
    final_data = BitArray()
    i = 0
    with open(output_file_name, "wb") as w:
        while i < data.length:
            buffer = BitArray(data[i:(i + max_code_length)])
            for size in symbols:
                code = buffer[:size] if size > 1 else BitArray(uint=buffer[0], length=1)
                if code.bin in symbols[size]:
                    symbols[size][code.bin].tofile(w)
                    break
            i += size
def main():
    if len(sys.argv) > 2:
        input_file_name = sys.argv[1]
        output_file_name = sys.argv[2]
        print(f"File Name: {input_file_name}")
        input_file_length = os.path.getsize(input_file_name)
        print(f"File Size: {input_file_length} Bytes")
        print("\nReading File...")
        file_data = read_file_data(input_file_name)
        max_code_length = int(file_data[:8].uint)
        max_code_bits = int(math.ceil(math.log(max_code_length + 1, 2)))
        padding_size = int(file_data[8:11].uint)
        print("Reading Symbol Codes...")
        symbols_data = file_data[11:]
        symbols, pos = parse_symbols(symbols_data, max_code_bits)
        pos += padding_size
        print("Reading and Writing Compressed Data...")
        data = symbols_data[pos:]
        decompress_data(data, symbols, max_code_length, output_file_name)
        output_file_length = os.path.getsize(output_file_name)
        print(f"\nFile Name:           {output_file_name}")
        print(f"Compressed file size: {output_file_length} Bytes")
if __name__ == "__main__":
    main()