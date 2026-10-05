import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
b1 = "Python"
b2 = "cryptography and openssl"
b3 = "b3 1"
print("\nLanguage:\t", b1, "\nCryptographic Library:\t", b2, "\nTask:\t", b3)
def fonk1(length):
    return os.urandom(length)
def fonk2(b13, b14, plaintext):
    b4 = default_backend()
    b5 = Cipher(algorithms.AES(b13), modes.CBC(b14), b4=b4)
    b6 = b5.b6()
    b7 = b6.update(plaintext) + b6.finalize()
    b8 = b5.b8()
    b9 = b8.update(b7) + b8.finalize()
    return b7, b9
def fonk3(data):
    b10 = hashes.Hash(hashes.SHA256(), b4=default_backend())
    b10.update(data)
    return b10.finalize()
print("\nRandom Number Test")
b11 = fonk1(128)
b12 = fonk1(256)
print("Random Bytes (128 bits):\n", b11)
print("Random Bytes (256 bits):\n", b12)
print("\nAES Test")
b13 = fonk1(32)
b14 = fonk1(16)
b15 = b'Hello This is the secret message'
print("Plain Text:\n", b15)
ct, b16 = fonk2(b13, b14, b15)
print("Cipher Text:\n", ct)
print("Decrypted Text:\n", b16)
print("\nSHA 256 Test")
b17 = b'abc123'
b18 = fonk3(b17)
print("SHA256 Digest:\n", b18)