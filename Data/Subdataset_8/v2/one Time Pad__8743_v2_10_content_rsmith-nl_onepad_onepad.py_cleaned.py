import argparse
import base64
import bz2
import logging
import sys
__version__ = "2017.06.04"
def main(argv):
    logging.basicConfig(level=logging.WARNING, format="%(levelname)s: %(message)s")
    parser = argparse.ArgumentParser(description="Encrypt or decrypt data using a key file.")
    parser.add_argument("-v", "--version", action="version", version=__version__)
    parser.add_argument("cmd", type=str, choices=["enc", "dec"], help="Action to perform: 'enc' for encryption, 'dec' for decryption.")
    parser.add_argument("datafile", type=str, help="Name of the data file.")
    parser.add_argument("keyfile", type=str, help="Name of the key file.")
    args = parser.parse_args(argv)
    try:
        with open(args.datafile, "rb") as data_file:
            data = data_file.read()
        with open(args.keyfile, "rb") as key_file:
            key = unwrap(key_file.read())
    except IOError as e:
        logging.error("Failed to read input files: {}".format(e))
        sys.exit(1)
    if args.cmd == "dec":
        data = unwrap(data)
    else:
        data = bz2.compress(data)[10:]
    if len(data) > len(key):
        logging.error("Message is longer than the key.")
        sys.exit(2)
    result = bytes([i ^ j for i, j in zip(data, key)])
    if args.cmd == "enc":
        result = bytes(encode(result), "utf-8")
    else:
        result = bz2.decompress(b"BZh91AY&SY" + result)
    print(result.decode("utf-8"))
def unwrap(data):
    data = bytes([b for b in data if b not in b" \r\n"])
    return base64.b64decode(data)
def encode(data, chunk_len=6, line_len=78):
    length = len(data)
    n = int(line_len
    chunks = [
        base64.b64encode(data[j : j + chunk_len]).decode("ascii")
        for j in range(0, length, chunk_len)
    ]
    lines = [" ".join(chunks[i : i + n]) for i in range(0, len(chunks), n)]
    return "\n".join(lines)
if __name__ == "__main__":
    main(sys.argv[1:])