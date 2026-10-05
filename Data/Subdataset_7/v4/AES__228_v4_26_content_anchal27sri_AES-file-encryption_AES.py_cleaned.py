import os
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Hash import SHA256
def fonk1(key, b10):
    b1 = 64 * 1024
    b2 = "(enc)" + b10
    b3 = str(os.path.getsize(b10)).zfill(16)
    b4 = Random.new().read(16)
    b5 = AES.new(key, AES.MODE_CBC, b4)
    with open(b10, 'rb') as infile:
        with open(b2, 'wb') as outfile:
            outfile.write(b3.encode('utf-8'))
            outfile.write(b4)
            while True:
                b6 = infile.read(b1)
                if len(b6) == 0:
                    break
                elif len(b6) % 16 != 0:
                    b6 += b' ' * (16 - (len(b6) % 16))
                outfile.write(b5.fonk1(b6))
def fonk2(key, b10):
    b1 = 64 * 1024
    b2 = b10[6:]
    with open(b10, 'rb') as infile:
        b3 = int(infile.read(16))
        b4 = infile.read(16)
        b7 = AES.new(key, AES.MODE_CBC, b4)
        with open(b2, 'wb') as outfile:
            while True:
                b6 = infile.read(b1)
                if len(b6) == 0:
                    break
                outfile.write(b7.fonk2(b6))
            outfile.truncate(b3)
def fonk3(b11):
    b8 = SHA256.new(b11.encode('utf-8'))
    return b8.digest()
def fonk4():
    b9 = input("Would you like to (E)encrypt or (D)decrypt: ").upper()
    if b9 = = 'E':
        b10 = input("File to encrypt: ")
        b11 = input("Password: ")
        fonk1(fonk3(b11), b10)
        print('Encryption done.')
    elif b9 = = 'D':
        b10 = input("File to decrypt: ")
        b11 = input("Password: ")
        fonk2(fonk3(b11), b10)
        print("Decryption done.")
    else:
        print("Invalid option selected. Exiting...")
if b12 = = "__main__":
    fonk4()