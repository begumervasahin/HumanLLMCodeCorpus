import os
import sys
from utils import chilkat
def fonk1():
    os.system("cls" if os.b1 = = "nt" else "clear")
def fonk2(text, b13):
    b2 = b13.encryptStringENC(text)
    return b2
def fonk3():
    fonk1()
    b3 = chilkat.CkDh()
    b4 = chilkat.CkDh()
    b5 = b3.UnlockComponent("Test")
    b3.UseKnownPrime(5)
    b6 = b3.b6()
    b7 = b3.get_G()
    b5 = b4.SetPG(b6, b7)
    b8 = b3.createE(256)
    b9 = b4.createE(256)
    b10 = b3.findK(b9)
    b11 = b4.findK(b8)
    if b10 = = b11:
        b12 = 'A shared secret equal to B'
    else:
        b12 = '**Shared secret NOT EQUAL !!!!**'
    b13 = chilkat.CkCrypt2()
    b5 = b13.UnlockComponent("Test")
    b13.put_EncodingMode("hex")
    b13.put_HashAlgorithm("md5")
    b14 = b13.hashStringENC(b10)
    b15 = '128-bit Season key : {}'.format(b14)
    b13.put_CryptAlgorithm("aes")
    b13.put_KeyLength(128)
    b13.put_CipherMode("cbc")
    b16 = b13.hashStringENC(b14)
    b17 = 'Initialization Vector: {}'.format(b16)
    b13.SetEncodedKey(b14,"hex")
    b13.SetEncodedIV(b16,"hex")
    print('-> {}\n--> {}'.format(b15, b17))
    print("\n")
    b18 = []
    while True:
        print('Choose :\n[1] Encrypt text\n[2] Decrypt text (For this Session only)\n[3] List all Encrypted texts\n[4] Exit')
        b19 = input('>> ')
        if b19 = = '1':
            b20 = input('Encrypt text >> ')
            b21 = fonk2(b20, b13)
            b18.append(b21)
            print('+ Encrypted ->', b21)
        elif b19 = = '2':
            b20 = input('Decrypt text >> ')
            b22 = b13.decryptStringENC(b20)
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
    fonk3()