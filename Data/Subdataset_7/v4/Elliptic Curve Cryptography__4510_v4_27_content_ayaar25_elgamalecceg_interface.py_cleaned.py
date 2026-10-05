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
print("\b4")
fonk2("- Choose algorithm -")
fonk3("[1] ElGamal \t [b5] ECC")
b2 = input("Enter Choice: ")
b3 = None
if b2 = = '1':
    b3 = ElGamal()
elif b2 = = 'b5':
    print("\b4 = ===============")
    fonk2("- Enter constants -")
    fonk3("Formula: y^b5 = ( x^3 + Ax + B ) mod P")
    fonk3("K is used in encoding/decoding process")
    b6 = input("Enter A: ")
    b7 = input("Enter B: ")
    b8 = input("Enter P: ")
    b9 = input("Enter K: ")
    b3 = EllipticCurveCryptoElGamal(b6, b7, b8, b9)
print("\b4 = ===============")
fonk2("- Choose operation -")
fonk3("[1] Encrypt \t [b5] Decrypt")
b10 = input("Enter Choice: ")
print("\b4 = ===============")
fonk2("- Do you already have the key? -")
fonk3("[1] Yes \t [b5] No, create new key")
b11 = input("Enter Choice: ")
if b11 = = 'b5':
    print("\b4 = ===============")
    fonk2("- Enter new key seed -")
    b12 = input("Enter seed: ")
    b3.key_gen(b12)
elif b11 = = '1':
    print("\b4 = ===============")
    fonk2("- Enter public key location -")
    b13 = input("Enter file location: ")
    fonk2("\nPublic Key File:")
    with open(b13, 'rb') as file:
        b14 = file.read()
    for c in b14:
        print(hex(c), b15 = ' ')
    print()
    print("\b4 = ===============")
    fonk2("- Enter private key location -")
    b16 = input("Enter file location: ")
    fonk2("\nPrivate Key File:")
    with open(b16, 'rb') as file:
        b14 = file.read()
    for c in b14:
        print(hex(c), b15 = ' ')
    print()
print("\b4 = ===============")
fonk2("- Enter target file -")
b17 = input("Enter file: ")
print("\b4 = ===============")
fonk2("- Input File: -")
with open(b17, 'r') as file:
    b14 = file.read()
print(b14)
if b10 = = '1':
    if b2 = = '1':
        b3.encrypt(b17, b13, b16)
        b18 = 'cipher.txt'
    elif b2 = = 'b5':
        b3.encrypt(b17, b13, b16, b9)
        b18 = 'cipher_ecceg.txt'
elif b10 = = 'b5':
    b3.decrypt(b17, b13, b16)
    b18 = 'out.txt'
print("\b4 = ===============")
fonk2("- Output File: -")
with open(b18, 'rb') as file:
    b14 = file.read()
for c in b14:
    print(hex(c), b15 = ' ')
print()