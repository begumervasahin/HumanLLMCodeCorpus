import sys
b1 = [chr(n) for n in range(32, 127) if chr(n) not in ['$']]
def fonk1(cipher_char, key_char):
    return b1[(b1.index(cipher_char) - b1.index(key_char)) % len(b1)]
def fonk2(cipher_char, plaintext_char):
    return fonk4(cipher_char, plaintext_char)
def fonk3(b5, b4):
    b2 = ""
    for i in range(len(b5)):
        b2 += fonk4(b4[i], b5[i])
    return b2
b3 = sys.argv[1]
if b3 = = "d":
    print("Decryption Mode, to exit press: ctrl + c")
    b4 = input("Enter the b4: ")
    b5 = input("Now enter the b5: ")
    print("Plaintext: " + fonk6(b5, b4))
elif b3 = = "e":
    print("Encryption Mode, to exit press: ctrl + c")
    b2 = input("Enter the b2: ")
    b4 = input("Now enter the b4: ")
    if len(b2) <= len(b4):
        b5 = "".join([fonk5(b4[i], b2[i]) for i in range(len(b2))])
        print("KEY: " + b5)
    else:
        print("The length of b4 must be >= b2 to encrypt all of it")
else:
    print("Please enter either 'e' for encryption or 'd' for decryption.")
    sys.exit(-1)
import sys
b1 = [chr(n) for n in range(32, 127) if chr(n) not in ['$']]
def fonk4(cipher_char, key_char):
    return b1[(b1.index(cipher_char) - b1.index(key_char)) % len(b1)]
def fonk5(cipher_char, plaintext_char):
    return fonk4(cipher_char, plaintext_char)
def fonk6(b5, b4):
    b2 = ""
    for i in range(len(b5)):
        b2 += fonk4(b4[i], b5[i])
    return b2
b3 = sys.argv[1]
if b3 = = "d":
    print("Decryption Mode, to exit press: ctrl + c")
    b4 = input("Enter the b4: ")
    b5 = input("Now enter the b5: ")
    print("Plaintext: " + fonk6(b5, b4))
elif b3 = = "e":
    print("Encryption Mode, to exit press: ctrl + c")
    b2 = input("Enter the b2: ")
    b4 = input("Now enter the b4: ")
    if len(b2) <= len(b4):
        b5 = "".join([fonk5(b4[i], b2[i]) for i in range(len(b2))])
        print("KEY: " + b5)
    else:
        print("The length of b4 must be >= b2 to encrypt all of it")
else:
    print("Please enter either 'e' for encryption or 'd' for decryption.")
    sys.exit(-1)