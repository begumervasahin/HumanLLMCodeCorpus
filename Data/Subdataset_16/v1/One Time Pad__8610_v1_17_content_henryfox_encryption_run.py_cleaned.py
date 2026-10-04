import sys
import encrypt
def fonk1():
    if len(sys.argv) != 6:
        print("Usage: python script.py <encrypt/decrypt> <b2> <b3> <b4> <b5>")
        return
    b1 = sys.argv[1]
    b2 = sys.argv[2][1:]
    b3 = sys.argv[3][1:]
    b4 = sys.argv[4]
    b5 = sys.argv[5][1:]
    b6 = encrypt.enc(b1, b2, b3, b4, b5)
    print(b6)
if b7 = = "__main__":
    fonk1()