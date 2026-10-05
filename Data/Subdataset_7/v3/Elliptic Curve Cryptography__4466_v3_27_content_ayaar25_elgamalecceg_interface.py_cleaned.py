from ecceg import EllipticCurveCryptoElGamal
from elgamal import ElGamal
def fonk1(b1):
    b1 = '\033[1;34m' + b1 + '\033[1;m'
    print(b1)
def fonk2(b1):
    b1 = '\033[1;32m' + b1 + '\033[1;m'
    print(b1)
def fonk3(b1):
    b1 = '\033[1;35m' + b1 + '\033[1;m'
    print(b1)
def fonk4():
    print("\b2")
    fonk2("- Choose algorithm -")
    fonk3("[1] ElGamal \t [b3] ECC")
    return input("Enter Choice: ")
def fonk5():
    print("\b2 = ===============")
    fonk2("- Enter constants -")
    fonk3("Formula: y^b3 = ( x^3 + Ax + B ) mod P")
    fonk3("K is used in encoding/decoding process")
    b4 = input("Enter A: ")
    b5 = input("Enter B: ")
    b6 = input("Enter P: ")
    b7 = input("Enter K: ")
    return b4, b5, b6, b7
def fonk6():
    print("\b2 = ===============")
    fonk2("- Choose b18 -")
    fonk3("[1] Encrypt \t [b3] Decrypt")
    return input("Enter Choice: ")
def fonk7():
    print("\b2 = ===============")
    fonk2("- Do you already have the key? -")
    fonk3("[1] Yes \t [b3] No, create new key")
    return input("Enter Choice: ")
def fonk8(b14):
    print("\b2 = ===============")
    fonk2("- Enter new key seed -")
    b8 = input("Enter seed: ")
    b14.key_gen(b8)
def fonk9():
    print("\b2 = ===============")
    fonk2("- Enter public key location -")
    b9 = input("Enter file location: ")
    fonk2("\nPublic Key File:")
    with open(b9, 'rb') as file:
        b10 = file.read()
    for c in b10:
        print(hex(c), b11 = ' ')
    print()
    print("\b2 = ===============")
    fonk2("- Enter private key location -")
    b12 = input("Enter file location: ")
    fonk2("\nPrivate Key File:")
    with open(b12, 'rb') as file:
        b10 = file.read()
    for c in b10:
        print(hex(c), b11 = ' ')
    print()
    return b9, b12
def fonk10():
    print("\b2 = ===============")
    fonk2("- Enter target file -")
    return input("Enter file: ")
def fonk11(file_name):
    print("\b2 = ===============")
    fonk2("- Input File: -")
    with open(file_name, 'r') as file:
        b10 = file.read()
    print(b10)
    return b10
def fonk12(b13, b14, in_file, b9, b12, b7 = None):
    if b13 = = '1':
        if b14 = = '1':
            b14.encrypt(in_file, b9, b12)
            b15 = 'cipher.txt'
        elif b14 = = 'b3':
            b14.encrypt(in_file, b9, b12, b7)
            b15 = 'cipher_ecceg.txt'
    elif b13 = = 'b3':
        b14.decrypt(in_file, b9, b12)
        b15 = 'out.txt'
    return b15
def fonk13(b15):
    print("\b2 = ===============")
    fonk2("- Output File: -")
    with open(b15, 'rb') as file:
        b10 = file.read()
    for c in b10:
        print(hex(c), b11 = ' ')
    print()
if b16 = = '__main__':
    b17 = fonk4()
    b14 = None
    if b17 = = '1':
        b14 = ElGamal()
    elif b17 = = 'b3':
        b4, b5, b6, b7 = fonk5()
        b14 = EllipticCurveCryptoElGamal(b4, b5, b6, b7)
    b18 = fonk6()
    b19 = fonk7()
    if b19 = = 'b3':
        fonk8(b14)
    elif b19 = = '1':
        b9, b12 = fonk9()
    b20 = fonk10()
    b10 = fonk11(b20)
    if b18 = = '1':
        b15 = fonk12(b18, b17, b20, b9, b12)
    elif b18 = = 'b3':
        b15 = fonk12(b18, b17, b20, b9, b12, b7)
    fonk13(b15)