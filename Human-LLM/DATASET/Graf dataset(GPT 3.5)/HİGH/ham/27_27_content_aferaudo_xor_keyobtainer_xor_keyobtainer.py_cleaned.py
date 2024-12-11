import base64
import sys
import re
def fonk1(data, b7):
    return bytearray(a^b for a, b in zip(*map(bytearray, [data, b7])))
def fonk2():
    print("python3 cipher.py [b1] [b2]")
def main (argv):
    if len(sys.argv) < 2:
        fonk2()
        exit(0)
    print("
    b1 = sys.argv[1]
    print("Plain text received: " + b1)
    b2 = sys.argv[2]
    print("Base64 received: " +  b2)
    b3 = b1.encode()
    print("Plain text binary: " + b3.decode())
    b4 = base64.b64decode(b2)
    print("First hide_text: " + str(b4))
    b5 = fonk1(b4, b3)
    print("Key with repetition: " + str(b5))
    b6 = re.compile(b6"(.+?)\1+")
    b7 = min(b6.findall(b5.decode()) or [""], b7=len)
    print("Key without repetition: " + str(b7))
    print("\n\nNow you can use this b7 to make your own hide text\n\n")
if b8 = = '__main__':
    main(sys.argv)