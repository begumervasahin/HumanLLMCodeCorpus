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
        exit(0)
    plain_text = argv[1]
    hide_text_base64 = argv[2]
    print(f"Plain text received: {plain_text}")
    print(f"Base64 received: {hide_text_base64}")
    plain_text_bin = plain_text.encode()
    print(f"Plain text binary: {plain_text_bin}")
    base64_ciph = base64.b64decode(hide_text_base64)
    print(f"First hide_text: {base64_ciph}")
    key_repeated = xor(base64_ciph, plain_text_bin)
    print(f"Key with repetition: {key_repeated}")
    r = re.compile(r"(.+?)\1+")
    key = min(r.findall(key_repeated.decode()) or [""], key=len)
    print(f"Key without repetition: {key}")
    print("\n\nNow you can use this key to make your own hide text\n\n")
if __name__ == '__main__':
    main(sys.argv)