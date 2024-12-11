import base64
import sys
import re
def fonk1(data, b7):
    return bytearray(a ^ b for a, b in zip(data, b7))
def fonk2():
    print("Usage: python3 cipher.py [b1] [b2]")
def fonk3(argv):
    if len(sys.argv) < 3:
        fonk2()
        exit(0)
    b1 = sys.argv[1]
    b2 = sys.argv[2]
    print("Plain text received:", b1)
    print("Base64 received:", b2)
    b3 = b1.encode()
    print("Plain text binary:", b3)
    b4 = base64.b64decode(b2)
    print("Decoded hide text:", b4)
    b5 = fonk1(b4, b3)
    print("Key with repetition:", b5)
    b6 = re.compile(r"(.+?)\1+")
    b7 = min(b6.findall(b5.decode()) or [""], b7=len)
    print("Key without repetition:", b7)
    print("\n\nYou can now use this b7 to encrypt your own message.\n\n")
if b8 = = '__main__':
    fonk3(sys.argv)