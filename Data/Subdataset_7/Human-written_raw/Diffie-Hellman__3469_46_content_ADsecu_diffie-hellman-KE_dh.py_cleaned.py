import os
import sys
from utils import chilkat
def fonk1():
    b1 = os.name == "nt"
    if b1:
        os.system("cls")
    else:
        os.system("clear")
fonk1()
b2 = chilkat.CkDh()
b3 = chilkat.CkDh()
b4 = b2.UnlockComponent("Test")
b2.UseKnownPrime(5)
b5 = b2.b5()
b6 = b2.get_G()
b4 = b3.SetPG(b5,b6)
b7 = b2.createE(256)
b8 = b3.createE(256)
b9 = b2.findK(b8)
b10 = b3.findK(b7)
if b9 = = b10:
    b11 = 'A shared secret equal to B'
else:
    b11 = '**Shared secret NOT EQUAL !!!!**'
b12 = chilkat.CkCrypt2()
b4 = b12.UnlockComponent("Test")
b12.put_EncodingMode("hex")
b12.put_HashAlgorithm("md5")
b13 = b12.hashStringENC(b9)
b14 = '128-bit Season key : {}'.format(b13)
b12.put_CryptAlgorithm("aes")
b12.put_KeyLength(128)
b12.put_CipherMode("cbc")
b15 = b12.hashStringENC(b13)
b16 = 'Initialization Vector: {}'.format(b15)
b12.SetEncodedKey(b13,"hex")
b12.SetEncodedIV(b15,"hex")
print('-> {}\n--> {}'.format(b14, b16))
print()
b12.put_EncodingMode("base64")
b17 = []
def fonk2(text):
    b18 = b12.encryptStringENC(text)
    b17.append(b18)
    print('+ Encrypted -> '+b18)
print('''
  Choose :
  [1] Encrypt text
  [2] Decrypt text (For this Session only)
  [3] List all Encrypted texts
  [4] Exit''')
while True:
    b19 = input('>> ')
    if b19 = = 'h':
        print()
    elif b19 = = '1':
        b20 = input('Encrypt text >> ')
        fonk2(b20)
    elif b19 = = '2':
        b20 = input('Decrypt text >> ')
        b21 = b12.decryptStringENC(b20)
        print(b21)
    elif b19 = = '3':
        a1 = 1
        for i in b17:
            print('{} - {}'.format(a1, i))
            a1 = a1 + 1
    elif b19 = = '4':
        print('Good Bye')
        sys.exit()
    else:
        print('invaild number, type [h] for help or 4 for exit')