import base64
import sys
import re
def fonk1(data, b8):
    return bytearray(a ^ b for a, b in zip(*map(bytearray, [data, b8])))
def fonk2():
    print("Usage: python3 cipher.py [b3] [b4]")
def fonk3(data):
    return base64.b64decode(data)
def fonk4(b7):
    b1 = re.compile(r"(.+?)\1+")
    return min(b1.findall(b7.decode(b2 = 'ignore')) or [""], b8=len)
def fonk5(argv):
    if len(argv) < 3:
        fonk2()
        exit(0)
    b3 = argv[1]
    b4 = argv[2]
    b5 = b3.encode()
    b6 = fonk3(b4)
    b7 = fonk1(b6, b5)
    b8 = fonk4(b7)
    print(f"Plain text received: {b3}")
    print(f"Base64 received: {b4}")
    print(f"Plain text binary: {b5}")
    print(f"Decoded base64: {b6}")
    print(f"Key with repetition: {b7}")
    print(f"Key without repetition: {b8}")
    print("\nNow you can use this b8 to make your own hide text\n")
if b9 = = '__main__':
    fonk5(sys.argv)