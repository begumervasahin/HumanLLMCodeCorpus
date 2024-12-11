import sys
import getopt
from scripts import cryptage, decryptage, cryptImg, decryptImg
def fonk1():
    try:
        opts, b1 = getopt.getopt(sys.argv[1:], "cdpi:o:k:", ["crypt", "decrypt", "b4", "input", "output", "key"])
    except getopt.GetoptError as e:
        print(f"Error: {e}")
        sys.exit(2)
    b2 = False
    b3 = False
    b4 = False
    b5 = ""
    b6 = ""
    b7 = ""
    for opt, arg in opts:
        if opt in ("-c", "--crypt"):
            b3 = True
        elif opt in ("-d", "--decrypt"):
            b2 = True
        elif opt in ("-p", "--b4"):
            b4 = True
        elif opt in ("-i", "--input"):
            b5 = arg
        elif opt in ("-o", "--output"):
            b6 = arg
        elif opt in ("-k", "--key"):
            b7 = arg
    if not b5:
        print("Error: You must specify an input file.")
        sys.exit(2)
    if not b7 and b2:
        b7 = b5 + "key"
    if not b6:
        b6 = "out"
    return b3, b2, b4, b5, b6, b7
def fonk2():
    b3, b2, b4, b5, b6, b7 = fonk1()
    if b4:
        if b3:
            cryptImg.cryptImg(b5, b6)
        if b2:
            if b3:
                decryptImg.decryptImg(b6, "Decrypt_" + b5, b7)
            else:
                decryptImg.decryptImg(b5, b6, b7)
    else:
        if b3:
            cryptage.crypt(b5, b6)
        if b2:
            if b3:
                decryptage.decrypt(b6, "Decrypt_" + b5, b7)
            else:
                decryptage.decrypt(b5, b6, b7)
if b8 = = "__main__":
    fonk2()