from sys import argv
import io
from decrypt import *
from encrypt import *
from keyGenerator import *
import Key
a1 = 500
b1 = 'in.txt'
b2 = 'crypted.txt'
b3 = 'decrypted.txt'
def fonk1(file):
    b4 = io.open(b1, "r+", encoding="utf-8")
    b5 = b4.read()
    b4.close()
    return b5
def fonk2():
    b6 = io.open(b2, "w", encoding="utf-8")
    b7 = io.open(b3, "w", encoding="utf-8")
    b8 = generateRandomNumber(a1)
    b9 = generateRandomNumber(a1)
    b10 = findNearPrime(b8)
    b11 = findNearPrime(b9)
    privata, b12 = generateKeys(b10, b11)
    print(privata, b12)
    b13 = fonk1(b1)
    b14 = encrypt(b13, privata)
    print("crypted", b14)
    b6.write(b14)
    b15 = decrypt(b14, b12)
    b7.write(b15)
    b6.close()
    b7.close()
if b16 = = "__main__":
    fonk2()