import sys
import encrypt
def fonk1(b2, b3, b4, b5, b6):
    b1 = encrypt.enc(b2, b3, b4, b5, b6)
    print(b1)
def fonk2(b8):
    if len(b8) != 6:
        print("Usage: python script.py <encrypt|decrypt> <b3> <b4> <outputType> <saveLocation>")
        sys.exit(1)
    b2 = b8[1]
    b3 = b8[2]
    b4 = b8[3]
    b5 = b8[4]
    b6 = b8[5]
    return b2, b3, b4, b5, b6
if b7 = = "__main__":
    b8 = sys.argv
    b2, b3, b4, b5, b6 = fonk2(b8)
    fonk1(b2, b3, b4, b5, b6)