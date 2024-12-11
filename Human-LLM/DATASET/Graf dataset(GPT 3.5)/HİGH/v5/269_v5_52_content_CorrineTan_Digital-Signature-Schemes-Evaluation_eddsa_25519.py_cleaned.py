import ed25519
import time
import sys
import hashlib
def fonk1(b13):
    a1 = 0
    a2 = 0
    a3 = 0
    with open(b13) as file:
        for line in file:
            b1 = str.encode(line)
            b2 = hashlib.sha256(b1).b2()
            b3 = time.time()
            signing_key, b4 = ed25519.create_keypair()
            b5 = time.time()
            a1 += b5 - b3
            b6 = time.time()
            b7 = signing_key.sign(b2, b10="base64")
            b8 = time.time()
            a2 += b8 - b6
            b9 = time.time()
            try:
                b4.verify(b7, b2, b10 = "base64")
            except ed25519.BadSignatureError:
                print("Invalid b7!")
            b11 = time.time()
            a3 += b11 - b9
    return a1, a2, a3
if b12 = = '__main__':
    b13 = "".join(sys.argv[1:])
    a1, a2, a3 = fonk1(b13)
    b14 = a1 + a2 + a3
    print("Time taken to generate key pairs:", a1)
    print("Time taken to sign messages:", a2)
    print("Time taken to verify messages:", a3)
    print("Total time:", b14)