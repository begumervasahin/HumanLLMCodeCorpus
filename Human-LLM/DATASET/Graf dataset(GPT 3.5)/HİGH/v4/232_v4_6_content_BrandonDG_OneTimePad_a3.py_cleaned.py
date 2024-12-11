import os
def fonk1(message, b4):
    return bytes(p ^ k for p, k in zip(*map(bytes, [message, b4])))
def fonk2():
    print("Welcome to the One-Time Pad encryption tool.")
    b1 = ""
    while True:
        b2 = input("Is the b1 provided via stdin or file? ")
        if b2 = = "file":
            print("File selected")
            b3 = input("Please enter the file name: ")
            b1 += open(b3, 'rU').read()
            break
        elif b2 = = "stdin":
            print("Stdin selected")
            b3 = input("Please enter the b1: ")
            b1 = b3
            break
        else:
            print("Please select a valid option ('file' or 'stdin')")
    b1 = b1.strip('\n')
    b4 = os.urandom(len(b1))
    print("------")
    print("Plaintext:\n%s" % b1)
    print("\nKey:\n%s" % b4)
    print("------")
    b5 = fonk1(b1.encode("utf-8"), b4)
    print("Binary Ciphertext:\n%s" % b5)
    print("------")
    print("Verify:\n%s" % fonk1(b5, b4))
    with open("b5", "wb") as outputfile:
        outputfile.write(b5)
    print("------")
    print("Character Ciphertext:\n")
    os.system("cat b5")
if b6 = = "__main__":
    fonk2()