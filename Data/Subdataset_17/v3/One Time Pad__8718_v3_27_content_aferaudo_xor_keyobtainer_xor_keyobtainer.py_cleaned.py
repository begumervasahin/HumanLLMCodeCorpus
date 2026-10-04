import base64
import sys
import re
def xor(data, key):
    return bytearray(a ^ b for a, b in zip(*map(bytearray, [data, key])))
def print_help():
    print("Usage: python3 cipher.py [plain_text] [hide_text_base64]")
def decode_base64(data):
    return base64.b64decode(data)
def find_repeating_key(key_repeated):
    pattern = re.compile(r"(.+?)\1+")
    return min(pattern.findall(key_repeated.decode(errors='ignore')) or [""], key=len)
def main(argv):
    if len(argv) < 3:
        print_help()
        exit(0)
    plain_text = argv[1]
    hide_text_base64 = argv[2]
    plain_text_bytes = plain_text.encode()
    base64_decoded = decode_base64(hide_text_base64)
    key_repeated = xor(base64_decoded, plain_text_bytes)
    key = find_repeating_key(key_repeated)
    print(f"Plain text received: {plain_text}")
    print(f"Base64 received: {hide_text_base64}")
    print(f"Plain text binary: {plain_text_bytes}")
    print(f"Decoded base64: {base64_decoded}")
    print(f"Key with repetition: {key_repeated}")
    print(f"Key without repetition: {key}")
    print("\nNow you can use this key to make your own hide text\n")
if __name__ == '__main__':
    main(sys.argv)