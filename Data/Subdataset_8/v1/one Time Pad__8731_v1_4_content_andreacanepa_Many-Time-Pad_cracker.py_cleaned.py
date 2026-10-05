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
        with open(args.filename) as f:
            ciphertexts = [binascii.unhexlify(line.rstrip()) for line in f]
        cleartexts = [bytearray(b'?' * len(c)) for c in ciphertexts]
    except Exception as e:
        print(f"Cannot crack {args.filename} --- {e}")
        raise SystemExit(-1)
    for k in range(max(len(c) for c in ciphertexts)):
        cts = [c for c in ciphertexts if len(c) > k]
    max_line_length = max(len(line) for line in ciphertexts)
    list_of_columns = [[] for _ in range(max_line_length)]
    for line_of_ciphertexts in ciphertexts:
        for index, item in enumerate(line_of_ciphertexts):
            list_of_columns[index].append(item)
    spaces = []
    pad = []
    for column in list_of_columns:
        mydict = {}
        for i in column:
            for j in column:
                result = i ^ j
                if result >= 65:
                    mydict[i] = mydict.get(i, 0) + 1
                    mydict[j] = mydict.get(j, 0) + 1
        maximum = max(mydict, key=mydict.get)
        spaces.append(maximum)
    for space in spaces:
        pad.append(space ^ SPACE)
    for index_row, row in enumerate(ciphertexts):
        for index_column, column in enumerate(row):
            cleartexts[index_row][index_column] = ciphertexts[index_row][index_column] ^ pad[index_column]
    print("\n".join(c.decode('ascii') for c in cleartexts))
if __name__ == "__main__":
    main()