import os
import sys
from utils import chilkat
def fonk1():
    if os.b1 = = "nt":
        os.system("cls")
    else:
        os.system("clear")
def fonk2():
    b2 = chilkat.CkDh()
    b3 = chilkat.CkDh()
    b4 = b2.UnlockComponent("Test")
    b2.UseKnownPrime(5)
    b5 = b2.b5()
    b6 = b2.get_G()
    b4 = b3.SetPG(b5, b6)
    return b2, b3
def fonk3(b2, b3):
    b7 = b2.createE(256)
    b8 = b3.createE(256)
    return b7, b8
def fonk4(b2, b3, b7, b8):
    b9 = b2.findK(b8)
    b10 = b3.findK(b7)
    return b9, b10
def fonk5(b9):
    b11 = chilkat.CkCrypt2()
    b4 = b11.UnlockComponent("Test")
    b11.put_EncodingMode("hex")
    b11.put_HashAlgorithm("md5")
    b12 = b11.hashStringENC(b9)
    b13 = '128-bit Season key : {}'.format(b12)
    b11.put_CryptAlgorithm("aes")
    b11.put_KeyLength(128)
    b11.put_CipherMode("cbc")
    b14 = b11.hashStringENC(b12)
    b15 = 'Initialization Vector: {}'.format(b14)
    b11.SetEncodedKey(b12, "hex")
    b11.SetEncodedIV(b14, "hex")
    return b11, b13, b15
def fonk6(text, b11):
    b16 = b11.encryptStringENC(text)
    return b16
def fonk7():
    fonk1()
    b2, b3 = fonk2()
    b7, b8 = fonk3(b2, b3)
    b9, b10 = fonk4(b2, b3, b7, b8)
    b17 = 'A shared secret equal to B' if b9 == b10 else '**Shared secret NOT EQUAL !!!!**'
    b11, b13, b15 = fonk5(b9)
    print('-> {}\n--> {}'.format(b13, b15))
    print("\n")
    b18 = []
    while True:
        print('Choose :\n[1] Encrypt text\n[2] Decrypt text (For this Session only)\n[3] List all Encrypted texts\n[4] Exit')
        b19 = input('>> ')
        if b19 = = 'h':
            print()
        elif b19 = = '1':
            b20 = input('Encrypt text >> ')
            b21 = fonk6(b20, b11)
            b18.append(b21)
            print('+ Encrypted ->', b21)
        elif b19 = = '2':
            b20 = input('Decrypt text >> ')
            b22 = b11.decryptStringENC(b20)
            print(b22)
        elif b19 = = '3':
            a1 = 1
            for i in b18:
                print('{} - {}'.format(a1, i))
                a1 += 1
        elif b19 = = '4':
            print('Good Bye')
            sys.exit()
        else:
            print('Invalid number, type [h] for help or 4 for exit')
if b23 = = "__main__":
    fonk7()