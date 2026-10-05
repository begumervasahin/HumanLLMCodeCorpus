import sys
b1 = [chr(n) for n in range(32, 127) if chr(n) != '$']
def fonk1(char1, char2):
    return b1[(b1.index(char1) - b1.index(char2)) % len(b1)]
def fonk2(cipher_char, plain_char):
    return fonk1(cipher_char, plain_char)
def fonk3(b5, b4):
    b2 = ""
    for i in range(len(b5)):
        b2 += fonk1(b4[i], b5[i])
    return b2
def fonk4():
    b3 = sys.argv[1].lower()
    if b3 = = "d":
        print("Decryption Mode, press ctrl + c to exit.")
        b4 = input("Enter the ciphertext: ")
        b5 = input("Enter the b5: ")
        print("Plaintext:", fonk3(b5, b4))
    elif b3 = = "e":
        print("Encryption Mode, press ctrl + c to exit.")
        b2 = input("Enter the plaintext: ")
        b4 = input("Enter the ciphertext: ")
        if len(b2) <= len(b4):
            b5 = "".join(fonk2(b4[i], b2[i]) for i in range(len(b2)))
            print("Generated Key:")
            print(f"START_KEY_END\n{b5}\nSTART_KEY_END")
        else:
            print("The length of the ciphertext must be greater than or equal to the plaintext.")
    else:
        print("Please enter either 'e' for encryption or 'd' for decryption.")
if b6 = = "__main__":
    fonk4()