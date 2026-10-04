from ecceg import EllipticCurveCryptoElGamal
from elgamal import ElGamal
def fonk1(text):
    print('\033[1;34m' + text + '\033[1;m')
def fonk2(text):
    print('\033[1;32m' + text + '\033[1;m')
def fonk3(text):
    print('\033[1;35m' + text + '\033[1;m')
def fonk4(file_path):
    with open(file_path, 'rb') as file:
        b1 = file.read()
    for c in b1:
        print(hex(c), b2 = ' ')
    print()
def fonk5():
    print("\b5")
    fonk2("- Choose algorithm -")
    fonk3("[1] ElGamal \t [b6] ECC")
    b3 = input("Enter Choice: ")
    if b3 = = '1':
        b4 = ElGamal()
    elif b3 = = 'b6':
        print("\b5 = ===============")
        fonk2("- Enter constants -")
        fonk3("Formula: y^b6 = ( x^3 + Ax + B ) mod P")
        fonk3("K is used in encoding/decoding process")
        b7 = int(input("Enter A: "))
        b8 = int(input("Enter B: "))
        b9 = int(input("Enter P: "))
        b10 = int(input("Enter K: "))
        b4 = EllipticCurveCryptoElGamal(b7, b8, b9, b10)
    else:
        print("Invalid choice!")
        return
    print("\b5 = ===============")
    fonk2("- Choose operation -")
    fonk3("[1] Encrypt \t [b6] Decrypt")
    b11 = input("Enter Choice: ")
    print("\b5 = ===============")
    fonk2("- Do you already have the key? -")
    fonk3("[1] Yes \t [b6] No, create new key")
    b12 = input("Enter Choice: ")
    if b12 = = 'b6':
        print("\b5 = ===============")
        fonk2("- Enter new key seed -")
        b13 = input("Enter seed: ")
        b4.key_gen(b13)
        b14 = "key.pub"
        b15 = "key.pri"
    elif b12 = = '1':
        print("\b5 = ===============")
        fonk2("- Enter public key location -")
        b14 = input("Enter file location: ")
        fonk2("\nPublic Key File:")
        fonk4(b14)
        print("\b5 = ===============")
        fonk2("- Enter private key location -")
        b15 = input("Enter file location: ")
        fonk2("\nPrivate Key File:")
        fonk4(b15)
    else:
        print("Invalid choice!")
        return
    print("\b5 = ===============")
    fonk2("- Enter target file -")
    b16 = input("Enter file: ")
    print("\b5 = ===============")
    fonk2("- Input File: -")
    with open(b16, 'r') as file:
        b1 = file.read()
    print(b1)
    if b11 = = '1':
        if b3 = = '1':
            b4.encrypt(b16, b14, b15)
            b17 = 'cipher.txt'
        elif b3 = = 'b6':
            b4.encrypt(b16, b14, b15, b10)
            b17 = 'cipher_ecceg.txt'
    elif b11 = = 'b6':
        b4.decrypt(b16, b14, b15)
        b17 = 'out.txt'
    else:
        print("Invalid choice!")
        return
    print("\b5 = ===============")
    fonk2("- Output File: -")
    fonk4(b17)
if b18 = = '__main__':
    fonk5()