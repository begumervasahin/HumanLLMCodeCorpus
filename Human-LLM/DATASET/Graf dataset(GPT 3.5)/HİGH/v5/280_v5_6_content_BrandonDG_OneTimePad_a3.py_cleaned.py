import os
def fonk1(message: bytes, b4: bytes) -> bytes:
    return bytes(p ^ k for p, k in zip(message, b4))
def fonk2():
    while True:
        b1 = input("Is the b3 provided via stdin or file? ").strip().lower()
        if b1 = = "file":
            b2 = input("Please enter the file name: ").strip()
            try:
                with open(b2, 'r') as file:
                    return file.read().encode('utf-8')
            except FileNotFoundError:
                print("File not found. Please enter a valid b2.")
        elif b1 = = "stdin":
            return input("Please enter the b3: ").encode('utf-8')
        else:
            print("Please select a valid option ('file' or 'stdin')")
def fonk3():
    print("Welcome to the One-Time Pad encryption tool.")
    b3 = fonk2()
    b4 = os.urandom(len(b3))
    print("------")
    print("Plaintext:\n%s" % b3.decode('utf-8'))
    print("\nKey:\n%s" % b4)
    print("------")
    b5 = fonk1(b3, b4)
    print("Binary Ciphertext:\n%s" % b5)
    print("------")
    b6 = fonk1(b5, b4)
    print("Verify:\n%s" % b6.decode('utf-8'))
    with open("b5", "wb") as outputfile:
        outputfile.write(b5)
    print("------")
    print("Character Ciphertext:\n")
    os.system("cat b5")
if b7 = = "__main__":
    fonk3()