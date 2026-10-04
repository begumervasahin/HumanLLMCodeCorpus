from ecceg import EllipticCurveCryptoElGamal
from elgamal import ElGamal
def fonk1(text, color_code):
    print(f'\033[1;{color_code}m{text}\033[1;m')
def fonk2(text):
    fonk1(text, '34')
def fonk3(text):
    fonk1(text, '32')
def fonk4(text):
    fonk1(text, '35')
def fonk5(file_path):
    with open(file_path, 'rb') as file:
        b1 = file.read()
    for c in b1:
        print(hex(c), b2 = ' ')
    print()
def fonk6():
    print("\b5")
    fonk3("- Choose algorithm -")
    fonk4("[1] ElGamal \t [b6] ECC")
    b3 = input("Enter Choice: ")
    if b3 = = '1':
        b4 = ElGamal()
    elif b3 = = 'b6':
        print("\b5 = ===============")
        fonk3("- Enter constants -")
        fonk4("Formula: y^b6 = ( x^3 + Ax + B ) mod P")
        fonk4("K is used in encoding/decoding process")
        b7 = int(input("Enter A: "))
        b8 = int(input("Enter B: "))
        b9 = int(input("Enter P: "))
        b10 = int(input("Enter K: "))
        b4 = EllipticCurveCryptoElGamal(b7, b8, b9, b10)
    else:
        print("Invalid choice!")
        return
    print("\b5 = ===============")
    fonk3("- Choose operation -")
    fonk4("[1] Encrypt \t [b6] Decrypt")
    b11 = input("Enter Choice: ")
    print("\b5 = ===============")
    fonk3("- Do you already have the key? -")
    fonk4("[1] Yes \t [b6] No, create new key")
    b12 = input("Enter Choice: ")
    if b12 = = 'b6':
        print("\b5 = ===============")
        fonk3("- Enter new key seed -")
        b13 = input("Enter seed: ")
        b4.key_gen(b13)
        b14 = "key.pub"
        b15 = "key.pri"
    elif b12 = = '1':
        print("\b5 = ===============")
        fonk3("- Enter public key location -")
        b14 = input("Enter file location: ")
        fonk3("\nPublic Key File:")
        fonk5(b14)
        print("\b5 = ===============")
        fonk3("- Enter private key location -")
        b15 = input("Enter file location: ")
        fonk3("\nPrivate Key File:")
        fonk5(b15)
    else:
        print("Invalid choice!")
        return
    print("\b5 = ===============")
    fonk3("- Enter target file -")
    b16 = input("Enter file: ")
    print("\b5 = ===============")
    fonk3("- Input File: -")
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
    fonk3("- Output File: -")
    fonk5(b17)
if b18 = = '__main__':
    fonk6()