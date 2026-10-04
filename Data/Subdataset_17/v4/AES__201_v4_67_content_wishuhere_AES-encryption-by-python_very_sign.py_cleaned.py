import sys
import getopt
import os
from Crypto.Hash import SHA256, MD5, SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
BLOCK_SIZE = 1024 * 1024
HASH_MODES = {
    "SHA256": SHA256,
    "MD5": MD5,
    "SHA": SHA,
    "SHA1": SHA,
    "SHA-1": SHA
}
def get_hash_mode(hash_mode_str):
    hash_obj = HASH_MODES.get(hash_mode_str.upper())
    if hash_obj is None:
        print("Available modes: SHA256, MD5, SHA.")
        sys.exit(2)
    return hash_obj
def verify_signature(hash_mode_str, input_file, signature_file, public_key_file):
    print(f"Hash mode: {hash_mode_str}")
    hash_mode = get_hash_mode(hash_mode_str)
    my_hash = hash_mode.new()
    with open(input_file, "rb") as f:
        while block := f.read(BLOCK_SIZE):
            my_hash.update(block)
    with open(signature_file, "rb") as f:
        signature = f.read()
    print(f"Signature retrieved: {signature}")
    if not os.path.isfile(public_key_file):
        print("Public key doesn't exist... Task failed.")
        return False
    with open(public_key_file, "r") as f:
        public_key = RSA.importKey(f.read())
    verifier = PKCS1_v1_5.new(public_key)
    result = verifier.verify(my_hash, signature)
    print(f"Verification result: {result}")
    return result
def parse_arguments(argv):
    try:
        opts, args = getopt.getopt(argv, "h:")
    except getopt.GetoptError:
        print_usage()
        sys.exit(2)
    hash_mode = None
    for opt, arg in opts:
        if opt == "-h":
            hash_mode = arg
    if not hash_mode or len(args) != 3:
        print_usage()
        sys.exit(2)
    return hash_mode, args[0], args[1], args[2]
def print_usage():
    print("Usage: very_sign.py -h <hash> <input_file> <signature_file> <public_key_file>")
def main(argv):
    hash_mode, input_file, signature_file, public_key_file = parse_arguments(argv)
    result = verify_signature(hash_mode, input_file, signature_file, public_key_file)
    print(f"Verify result: {result}")
    return result
if __name__ == "__main__":
    main(sys.argv[1:])