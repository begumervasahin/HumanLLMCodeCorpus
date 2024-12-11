import os
def fonk1(message, b4):
    return bytes(p ^ k for p, k in zip(*map(bytes, [message, b4])))
def fonk2():
    print("One-Time Pad Encryption")
    b1 = ""
    while True:
        b2 = input("Is the b1 given via stdin or file? ")
        if b2 = = "file":
            print("File selected")
            b3 = input("Enter file name: ")
            b1 += open(b3, 'r').read()
            break
        elif b2 = = "stdin":
            print("stdin selected")
            b3 = input("Enter b1: ")
            b1 = b3
            break
        else:
            print("Please select a valid option ('file' or 'stdin')")
    b1 = b1.strip('\n')
    b4 = os.urandom(len(b1))
    print("------")
    print("Plaintext:")
    print(b1)
    print(" ")
    print("Key:")
    print(b4)
    print("------")
    b5 = fonk1(b1.encode("utf-8"), b4)
    print("Binary Ciphertext:")
    print(b5)
    print("------")
    print("Verify:")
    print(fonk1(b5, b4))
    with open("b5", "wb") as outputfile:
        outputfile.write(b5)
    print("------")
    print("Character Ciphertext:")
    os.system("cat b5")
if b6 = = "__main__":
    fonk2()