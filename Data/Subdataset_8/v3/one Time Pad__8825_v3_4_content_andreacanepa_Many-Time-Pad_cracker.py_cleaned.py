import binascii
import argparse
SPACE = ord(' ')
def read_ciphertexts(filename):
    try:
        with open(filename) as file:
            ciphertexts = [binascii.unhexlify(line.rstrip()) for line in file]
            cleartexts = [bytearray(b'?' * len(ciphertext)) for ciphertext in ciphertexts]
        return ciphertexts, cleartexts
    except Exception as e:
        print(f"Failed to read {filename}: {e}")
        raise SystemExit(-1)
def transpose_ciphertexts(ciphertexts):
    max_length = max(len(ciphertext) for ciphertext in ciphertexts)
    columns = [[] for _ in range(max_length)]
    for ciphertext in ciphertexts:
        for index, byte in enumerate(ciphertext):
            columns[index].append(byte)
    return columns
def find_spaces(columns):
    spaces = []
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
    return spaces
def calculate_pad(spaces):
    return [space ^ SPACE for space in spaces]
def decrypt_ciphertexts(ciphertexts, pad):
    cleartexts = []
    for ciphertext in ciphertexts:
        cleartext = bytearray(len(ciphertext))
        for index, byte in enumerate(ciphertext):
            cleartext[index] = byte ^ pad[index]
        cleartexts.append(cleartext)
    return cleartexts
def main():
    parser = argparse.ArgumentParser(description="Many-time Pad Cracker")
    parser.add_argument("--filename", type=str,
                        help="Name of the file containing the ciphertexts (default: ciphertexts.txt)",
                        default="ciphertexts.txt")
    args = parser.parse_args()
    ciphertexts, cleartexts = read_ciphertexts(args.filename)
    columns = transpose_ciphertexts(ciphertexts)
    spaces = find_spaces(columns)
    pad = calculate_pad(spaces)
    cleartexts = decrypt_ciphertexts(ciphertexts, pad)
    print("\n".join(cleartext.decode('ascii') for cleartext in cleartexts))
if __name__ == "__main__":
    main()