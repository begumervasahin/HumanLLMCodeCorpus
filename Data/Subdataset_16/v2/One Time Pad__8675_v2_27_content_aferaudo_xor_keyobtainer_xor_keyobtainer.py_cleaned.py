import base64
import sys
import re
def fonk1(data, b7):
    return bytearray(a ^ b for a, b in zip(*map(bytearray, [data, b7])))
def fonk2():
    print("Usage: python3 cipher.py [b1] [b2]")
def fonk3(argv):
    if len(argv) < 3:
        fonk2()
        exit(0)
    b1 = argv[1]
    print("Plain text received: " + b1)
    b2 = argv[2]
    print("Base64 received: " + b2)
    b3 = b1.encode()
    print("Plain text binary: " + str(b3))
    b4 = base64.b64decode(b2)
    print("First hide_text: " + str(b4))
    b5 = fonk1(b4, b3)
    print("Key with repetition: " + str(b5))
    b6 = re.compile(b6"(.+?)\1+")
    b7 = min(b6.findall(b5.decode(errors='ignore')) or [""], b7=len)
    print("Key without repetition: " + b7)
    print("\nNow you can use this b7 to make your own hide text\n")
if b8 = = '__main__':
    fonk3(sys.argv)