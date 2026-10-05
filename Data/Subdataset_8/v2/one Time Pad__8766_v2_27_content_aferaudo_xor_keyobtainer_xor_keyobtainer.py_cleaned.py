import base64
import sys
import re
def xor(data, key):
    return bytearray(a ^ b for a, b in zip(data, key))
def print_help():
    print("Usage: python3 cipher.py [plain_text] [hide_text_base64]")
def main(argv):
    if len(sys.argv) < 3:
        print_help()
        exit(0)
    plain_text = sys.argv[1]
    hide_text_base64 = sys.argv[2]
    print("Plain text received:", plain_text)
    print("Base64 received:", hide_text_base64)
    plain_text_bin = plain_text.encode()
    print("Plain text binary:", plain_text_bin)
    base64_ciph = base64.b64decode(hide_text_base64)
    print("Decoded hide text:", base64_ciph)
    key_repeated = xor(base64_ciph, plain_text_bin)
    print("Key with repetition:", key_repeated)
    pattern = re.compile(r"(.+?)\1+")
    key = min(pattern.findall(key_repeated.decode()) or [""], key=len)
    print("Key without repetition:", key)
    print("\n\nYou can now use this key to encrypt your own message.\n\n")
if __name__ == '__main__':
    main(sys.argv)