import binascii
import argparse
SPACE = ord(' ')
def main():
    parser = argparse.ArgumentParser(description="Many-time Pad Cracker")
    parser.add_argument("--filename", type=str,
                        help="Name of the file containing the ciphertexts (default: ciphertexts.txt)",
                        default="ciphertexts.txt")
    args = parser.parse_args()
    try:
        with open(args.filename) as file:
            ciphertexts = [binascii.unhexlify(line.rstrip()) for line in file]
            cleartexts = [bytearray(b'?' * len(ciphertext)) for ciphertext in ciphertexts]
    except Exception as e:
        print(f"Failed to read {args.filename}: {e}")
        raise SystemExit(-1)
    max_length = max(len(ciphertext) for ciphertext in ciphertexts)
    columns = [[] for _ in range(max_length)]
    for ciphertext in ciphertexts:
        for index, byte in enumerate(ciphertext):
            columns[index].append(byte)
    spaces = []
    pad = []
    for column in columns:
        frequencies = {}
        for byte1 in column:
            for byte2 in column:
                xor_result = byte1 ^ byte2
                if xor_result >= 65:
                    frequencies[byte1] = frequencies.get(byte1, 0) + 1
                    frequencies[byte2] = frequencies.get(byte2, 0) + 1
        most_frequent_byte = max(frequencies, key=frequencies.get)
        spaces.append(most_frequent_byte)
    for space in spaces:
        pad.append(space ^ SPACE)
    for index_row, ciphertext in enumerate(ciphertexts):
        for index_column, byte in enumerate(ciphertext):
            cleartexts[index_row][index_column] = ciphertext[index_column] ^ pad[index_column]
    print("\n".join(cleartext.decode('ascii') for cleartext in cleartexts))
if __name__ == "__main__":
    main()