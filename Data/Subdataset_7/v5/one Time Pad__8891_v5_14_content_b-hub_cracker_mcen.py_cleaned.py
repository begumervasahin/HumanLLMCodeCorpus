import sys
b1 = [chr(n) for n in range(32, 127) if chr(n) != '$']
def fonk1(cipher_char, key_char):
    b2 = len(b1)
    b3 = b1.index(cipher_char)
    b4 = b1.index(key_char)
    b5 = (b3 - b4) % b2
    return b1[b5]
def fonk2(cipher_char, plaintext_char):
    return fonk1(cipher_char, plaintext_char)
def fonk3(b9, b8):
    b6 = ""
    for i in range(len(b9)):
        b6 += fonk1(b8[i], b9[i])
    return b6
def fonk4():
    b7 = sys.argv[1]
    if b7 = = "d":
        print("Decryption Mode, to exit press: ctrl + c")
        b8 = input("Enter the b8: ")
        b9 = input("Now enter the b9: ")
        print("Plaintext: " + fonk3(b9, b8))
    elif b7 = = "e":
        print("Encryption Mode, to exit press: ctrl + c")
        b6 = input("Enter the b6: ")
        b8 = input("Now enter the b8: ")
        if len(b6) <= len(b8):
            b9 = "".join([fonk2(b8[i], b6[i]) for i in range(len(b6))])
            print("KEY: " + b9)
        else:
            print("The length of b8 must be >= b6 to encrypt all of it")
    else:
        print("Please enter either 'e' for encryption or 'd' for decryption.")
if b10 = = "__main__":
    fonk4()