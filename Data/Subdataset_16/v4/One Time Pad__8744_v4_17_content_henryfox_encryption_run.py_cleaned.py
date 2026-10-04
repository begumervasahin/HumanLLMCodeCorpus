import sys
import encrypt
def fonk1(b3, b4, b5, b6, b7):
    b1 = encrypt.enc(b3, b4, b5, b6, b7)
    print(b1)
if b2 = = "__main__":
    if len(sys.argv) != 6:
        print("Usage: python script.py <encrypt|decrypt> <b4> <b5> <outputType> <saveLocation>")
        sys.exit(1)
    b3 = sys.argv[1]
    b4 = sys.argv[2][1:]
    b5 = sys.argv[3][1:]
    b6 = sys.argv[4]
    b7 = sys.argv[5][1:]
    fonk1(b3, b4, b5, b6, b7)