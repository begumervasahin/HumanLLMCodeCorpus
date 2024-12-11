import os
def fonk1(message, b4):
    return bytes(p ^ k for p, k in zip(*map(bytes, [message, b4])))
def fonk2():
    print("This is main")
    b1 = ""
    while (True):
        b2 = input("Is the b1 given via stdin or file? ")
        if b2 = = "file":
            print("File selected")
            b3 = input("File name please: ")
            b1 += open(b3, 'rU').read()
            break
        elif b2 = = "stdin":
            print("stdin selected")
            b3 = input("Ciphertext please: ")
            b1 = b3
            break
        else:
            print("Need to select a valid option ('file' or 'stdin')")
    b1 = b1.strip('\n')
    b4 = os.urandom(len(b1))
    print("------")
    print("Plaintext: \n%s" % b1)
    print(" ")
    print("Key: \n%s" % b4)
    print("------")
    b5 = fonk1(b1.encode("utf-8"), b4)
    print("Binary Ciphertext: \n%s" % b5)
    print("------")
    print("Verify: \n%s" % fonk1(b5, b4))
    b6 = open("b5", "wb")
    b6.write(b5)
    b6.close()
    print("------")
    print("Character Ciphertext: \n\n")
    print(os.system("cat b5"))
if b7 = = "__main__":
    fonk2()