import base64
import sys
import re
def xor(data, key):
    return bytearray(a ^ b for a, b in zip(*map(bytearray, [data, key])))
def print_help():
    print("Usage: python3 cipher.py [plain_text] [hide_text_base64]")
def main(argv):
    if len(sys.argv) < 3:
        print_help()
        sys.exit(0)
    plain_text = sys.argv[1]
    print("Plain text received: " + plain_text)
    hide_text_base64 = sys.argv[2]
    print("Base64 received: " +  hide_text_base64)
    plain_text_bin = plain_text.encode()
    print("Plain text binary: " + plain_text_bin.decode())
    base64_ciph = base64.b64decode(hide_text_base64)
    print("First hide_text: " + str(base64_ciph))
    key_repeated = xor(base64_ciph, plain_text_bin)
    print("Key with repetition: " + str(key_repeated))
    r = re.compile(r"(.+?)\1+")
    key = min(r.findall(key_repeated.decode()) or [""], key=len)
    print("Key without repetition: " + str(key))
    print("\nNow you can use this key to make your own hide text\n")
if __name__ == '__main__':
    main(sys.argv)