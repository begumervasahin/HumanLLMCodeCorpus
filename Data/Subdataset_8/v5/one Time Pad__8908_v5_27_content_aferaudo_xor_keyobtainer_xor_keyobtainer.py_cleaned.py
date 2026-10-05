import base64
import sys
import re
def xor_bytes(data1, data2):
    return bytearray(a ^ b for a, b in zip(data1, data2))
def print_help():
    print("Usage: python3 cipher.py [plain_text] [hide_text_base64]")
def main(argv):
    if len(argv) < 3:
        print_help()
        sys.exit(1)
    plain_text = argv[1]
    print("Plain text received:", plain_text)
    hide_text_base64 = argv[2]
    print("Base64 received:", hide_text_base64)
    plain_text_bin = plain_text.encode()
    print("Plain text binary:", plain_text_bin)
    base64_ciphertext = base64.b64decode(hide_text_base64)
    print("First hide text:", base64_ciphertext)
    key_repeated = xor_bytes(base64_ciphertext, plain_text_bin)
    print("Key with repetition:", key_repeated)
    repeating_pattern = min(re.findall(r"(.+?)\1+", key_repeated.decode()) or [""], key=len)
    print("Key without repetition:", repeating_pattern)
    print("\nNow you can use this key to make your own hide text\n")
if __name__ == '__main__':
    main(sys.argv)