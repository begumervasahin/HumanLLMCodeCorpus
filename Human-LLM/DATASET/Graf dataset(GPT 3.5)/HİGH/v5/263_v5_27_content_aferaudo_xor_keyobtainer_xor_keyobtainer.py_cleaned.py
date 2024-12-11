import base64
import sys
import re
def fonk1(data1, data2):
    return bytearray(a ^ b for a, b in zip(data1, data2))
def fonk2():
    print("Usage: python3 cipher.py [b1] [b2]")
def fonk3(argv):
    if len(argv) < 3:
        fonk2()
        sys.exit(1)
    b1 = argv[1]
    print("Plain text received:", b1)
    b2 = argv[2]
    print("Base64 received:", b2)
    b3 = b1.encode()
    print("Plain text binary:", b3)
    b4 = base64.b64decode(b2)
    print("First hide text:", b4)
    b5 = fonk1(b4, b3)
    print("Key with repetition:", b5)
    b6 = min(re.findall(r"(.+?)\1+", b5.decode()) or [""], key=len)
    print("Key without repetition:", b6)
    print("\nNow you can use this key to make your own hide text\n")
if b7 = = '__main__':
    fonk3(sys.argv)