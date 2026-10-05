import argparse
import base64
import bz2
import logging
import sys
__version__ = "2017.06.04"
def main(argv):
    configure_logging()
    args = parse_arguments(argv)
    data, key = read_files(args.datafile, args.keyfile)
    if args.cmd == "dec":
        data = unwrap(data)
    else:
        data = compress_data(data)
    check_key_length(data, key)
    result = xor_operation(data, key)
    if args.cmd == "enc":
        result = encode_data(result)
    else:
        result = decompress_data(result)
    print_result(result)
def configure_logging():
    logging.basicConfig(level=logging.WARNING, format="%(levelname)s: %(message)s")
def parse_arguments(argv):
    parser = argparse.ArgumentParser(description="Use a one time pad to encrypt or decrypt a file.")
    parser.add_argument("-v", "--version", action="version", version=__version__)
    parser.add_argument("cmd", type=str, choices=["enc", "dec"], help="action to perform")
    parser.add_argument("datafile", type=str, help="name of the data file.")
    parser.add_argument("keyfile", type=str, help="name of the key file.")
    return parser.parse_args(argv)
def read_files(datafile, keyfile):
    try:
        with open(datafile, "rb") as df:
            data = df.read()
        with open(keyfile, "rb") as kf:
            key = unwrap(kf.read())
    except IOError as e:
        logging.error("Reading input files failed: {}".format(e))
        sys.exit(1)
    return data, key
def unwrap(data):
    data = bytes([b for b in data if b not in b" \r\n"])
    return base64.b64decode(data)
def compress_data(data):
    return bz2.compress(data)[10:]
def check_key_length(data, key):
    if len(data) > len(key):
        logging.error("Message longer than the key.")
        sys.exit(2)
def xor_operation(data, key):
    return bytes([i ^ j for i, j in zip(data, key)])
def encode_data(data):
    return bytes(encode(data), "utf-8")
def decompress_data(data):
    return bz2.decompress(b"BZh91AY&SY" + data)
def print_result(result):
    print(result.decode("utf-8"))
def encode(data, chunklen=6, linelen=78):
    length = len(data)
    n = int(linelen
    chunks = [
        base64.b64encode(data[j : j + chunklen]).decode("ascii")
        for j in range(0, length, chunklen)
    ]
    lines = [" ".join(chunks[i : i + n]) for i in range(0, len(chunks), n)]
    return "\n".join(lines)
if __name__ == "__main__":
    main(sys.argv[1:])