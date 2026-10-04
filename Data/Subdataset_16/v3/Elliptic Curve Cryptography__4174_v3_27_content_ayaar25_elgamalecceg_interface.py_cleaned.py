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
    print("\b4")
    fonk3("- Choose algorithm -")
    fonk4("[1] ElGamal \t [b5] ECC")
    b3 = input("Enter Choice: ")
    if b3 = = '1':
        return ElGamal()
    elif b3 = = 'b5':
        print("\b4 = ===============")
        fonk3("- Enter constants -")
        fonk4("Formula: y^b5 = ( x^3 + Ax + B ) mod P")
        fonk4("K is used in encoding/decoding process")
        b6 = int(input("Enter A: "))
        b7 = int(input("Enter B: "))
        b8 = int(input("Enter P: "))
        b9 = int(input("Enter K: "))
        return EllipticCurveCryptoElGamal(b6, b7, b8, b9)
    else:
        print("Invalid b3!")
        return None
def fonk7():
    print("\b4 = ===============")
    fonk3("- Choose b14 -")
    fonk4("[1] Encrypt \t [b5] Decrypt")
    return input("Enter Choice: ")
def fonk8():
    print("\b4 = ===============")
    fonk3("- Do you already have the key? -")
    fonk4("[1] Yes \t [b5] No, create new key")
    b3 = input("Enter Choice: ")
    if b3 = = 'b5':
        print("\b4 = ===============")
        fonk3("- Enter new key b10 -")
        b10 = input("Enter b10: ")
        b13.key_gen(b10)
        return "key.pub", "key.pri"
    elif b3 = = '1':
        print("\b4 = ===============")
        fonk3("- Enter public key location -")
        b11 = input("Enter file location: ")
        fonk3("\nPublic Key File:")
        fonk5(b11)
        print("\b4 = ===============")
        fonk3("- Enter private key location -")
        b12 = input("Enter file location: ")
        fonk3("\nPrivate Key File:")
        fonk5(b12)
        return b11, b12
    else:
        print("Invalid b3!")
        return None, None
def fonk9():
    b13 = fonk6()
    if not b13:
        return
    b14 = fonk7()
    if b14 not in ['1', 'b5']:
        print("Invalid b3!")
        return
    b11, b12 = fonk8()
    if not b11 or not b12:
        return
    print("\b4 = ===============")
    fonk3("- Enter target file -")
    b15 = input("Enter file: ")
    print("\b4 = ===============")
    fonk3("- Input File: -")
    with open(b15, 'r') as file:
        b1 = file.read()
    print(b1)
    if b14 = = '1':
        if isinstance(b13, ElGamal):
            b13.encrypt(b15, b11, b12)
            b16 = 'cipher.txt'
        else:
            b13.encrypt(b15, b11, b12, b9)
            b16 = 'cipher_ecceg.txt'
    else:
        b13.decrypt(b15, b11, b12)
        b16 = 'out.txt'
    print("\b4 = ===============")
    fonk3("- Output File: -")
    fonk5(b16)
if b17 = = '__main__':
    fonk9()