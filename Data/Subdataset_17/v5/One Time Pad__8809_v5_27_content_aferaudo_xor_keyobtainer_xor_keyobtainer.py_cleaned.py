import base64
import sys
import re
def xor(data, key):
    return bytearray(a ^ b for a, b in zip(*map(bytearray, [data, key])))
def print_help():
    print("Usage: python3 cipher.py [plain_text] [hide_text_base64]")
def main(argv):
    if len(argv) < 3:
        print_help()
        sys.exit(0)
    plain_text = argv[1]
    hide_text_base64 = argv[2]
    print(f"Plain text received: {plain_text}")
    print(f"Base64 received: {hide_text_base64}")
    plain_text_bin = plain_text.encode()
    print(f"Plain text binary: {plain_text_bin}")
    hidden_text_bin = base64.b64decode(hide_text_base64)
    print(f"Decoded hidden text: {hidden_text_bin}")
    key_repeated = xor(hidden_text_bin, plain_text_bin)
    print(f"Key with repetition: {key_repeated}")
    repeating_pattern = re.compile(r"(.+?)\1+")
    key = min(repeating_pattern.findall(key_repeated.decode()) or [""], key=len)
    print(f"Key without repetition: {key}")
    print("\nNow you can use this key to make your own hidden text.\n")
if __name__ == '__main__':
    main(sys.argv)