import os
def fonk1(message: bytes, b4: bytes) -> bytes:
    return bytes(p ^ k for p, k in zip(message, b4))
def fonk2() -> str:
    while True:
        b1 = input("Is the b3 given via stdin or file? ")
        if b1 = = "file":
            b2 = input("Enter file name: ")
            with open(b2, 'r') as file:
                return file.read().strip()
        elif b1 = = "stdin":
            return input("Enter b3: ").strip()
        else:
            print("Please select a valid option ('file' or 'stdin')")
def fonk3():
    print("One-Time Pad Encryption")
    b3 = fonk2()
    b4 = os.urandom(len(b3))
    print("------")
    print("Plaintext:")
    print(b3)
    print(" ")
    print("Key:")
    print(b4)
    print("------")
    b5 = fonk1(b3.encode("utf-8"), b4)
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
    fonk3()