import io
from keyGenerator import generateRandomNumber, findNearPrime, generateKeys
from encrypt import encrypt
from decrypt import decrypt
a1 = 500
b1 = 'in.txt'
b2 = 'crypted.txt'
b3 = 'decrypted.txt'
def fonk1(file):
    with io.open(file, "r+", b4 = "utf-8") as myFile:
        b5 = myFile.read()
    return b5
def fonk2():
    with io.open(b2, "w", b4 = "utf-8") as out, io.open(b3, "w", b4="utf-8") as out2:
        b6 = generateRandomNumber(a1)
        b7 = generateRandomNumber(a1)
        b8 = findNearPrime(b6)
        b9 = findNearPrime(b7)
        privKey, b10 = generateKeys(b8, b9)
        print("Private Key:", privKey)
        print("Public Key:", b10)
        b11 = fonk1(b1)
        b12 = encrypt(b11, privKey)
        print("Encrypted b5:", b12)
        out.write(b12)
        b13 = decrypt(b12, b10)
        out2.write(b13)
if b14 = = "__main__":
    fonk2()