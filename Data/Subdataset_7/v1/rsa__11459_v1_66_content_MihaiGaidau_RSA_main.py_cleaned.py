import io
from keyGenerator import generateRandomNumber, findNearPrime, generateKeys
from encrypt import encrypt
from decrypt import decrypt
a1 = 500
b1 = 'in.txt'
b2 = 'crypted.txt'
b3 = 'decrypted.txt'
def fonk1(file):
    with io.open(file, "r", b4 = "utf-8") as f:
        b5 = f.read()
    return b5
def fonk2():
    b6 = io.open(b2, "w", b4="utf-8")
    b7 = io.open(b3, "w", b4="utf-8")
    b8 = generateRandomNumber(a1)
    b9 = generateRandomNumber(a1)
    b10 = findNearPrime(b8)
    b11 = findNearPrime(b9)
    priv_key, b12 = generateKeys(b10, b11)
    print("Private Key:", priv_key)
    print("Public Key:", b12)
    b13 = fonk1(b1)
    b14 = encrypt(b13, priv_key)
    print("Encrypted Data:", b14)
    b6.write(b14)
    b15 = decrypt(b14, b12)
    b7.write(b15)
    b6.close()
    b7.close()
if b16 = = "__main__":
    fonk2()