import sys
import getopt
import scripts.cryptage as cryptage
import scripts.decryptage as decryptage
import scripts.cryptImg as cryptImg
import scripts.decryptImg as decryptImg
def fonk1():
    try:
        opts, b1 = getopt.getopt(sys.argv[1:], "cdpi:o:k:", ["crypt", "decrypt", "b4", "input", "output", "key"])
    except getopt.GetoptError as e:
        print(e.msg)
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
    if b5 = = "":
        print(opts)
        print("You must specify an input file")
        sys.exit(2)
    if b7 = = "" and b2:
        b7 = b5 + "key"
    if b6 = = "":
        b6 = "out"
    if b4:
        if b3:
            cryptImg.cryptImg(b5, b6)
        if b2:
            if b3:
                decryptImg.decryptImg(b6, "Decrypt_"+b5, b7)
            else:
                decryptImg.decryptImg(b5, b6, b7)
    else:
        if b3:
            cryptage.crypt(b5, b6)
        if b2:
            if b3:
                decryptage.decrypt(b6, "Decrypt_"+b5, b7)
            else:
                decryptage.decrypt(b5, b6, b7)
if b8 = = "__main__":
    fonk1()