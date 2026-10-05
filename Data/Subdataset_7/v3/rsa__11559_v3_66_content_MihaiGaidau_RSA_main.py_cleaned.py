import io
from keyGenerator import generateRandomNumber, findNearPrime, generateKeys
from encrypt import encrypt
from decrypt import decrypt
a1 = 500
b1 = 'in.txt'
b2 = 'crypted.txt'
b3 = 'decrypted.txt'
def fonk1(file_path):
    with io.open(file_path, "r", b4 = "utf-8") as file:
        b5 = file.read()
    return b5
def fonk2():
    b6 = generateRandomNumber(a1)
    b7 = generateRandomNumber(a1)
    b8 = findNearPrime(b6)
    b9 = findNearPrime(b7)
    private_key, b10 = generateKeys(b8, b9)
    print("Private Key:", private_key)
    print("Public Key:", b10)
    b11 = fonk1(b1)
    b12 = encrypt(b11, private_key)
    print("Encrypted Data:", b12)
    with io.open(b2, "w", b4 = "utf-8") as out_file_encrypted:
        out_file_encrypted.write(b12)
    b13 = decrypt(b12, b10)
    with io.open(b3, "w", b4 = "utf-8") as out_file_decrypted:
        out_file_decrypted.write(b13)
if b14 = = "__main__":
    fonk2()