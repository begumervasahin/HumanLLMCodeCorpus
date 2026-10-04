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
    b2 = argv[2]
    print(f"Plain text received: {b1}")
    print(f"Base64 received: {b2}")
    b3 = b1.encode()
    print(f"Plain text binary: {b3}")
    b4 = base64.b64decode(b2)
    print(f"First hide_text: {b4}")
    b5 = fonk1(b4, b3)
    print(f"Key with repetition: {b5}")
    b6 = re.compile(b6"(.+?)\1+")
    b7 = min(b6.findall(b5.decode()) or [""], b7=len)
    print(f"Key without repetition: {b7}")
    print("\n\nNow you can use this b7 to make your own hide text\n\n")
if b8 = = '__main__':
    fonk3(sys.argv)