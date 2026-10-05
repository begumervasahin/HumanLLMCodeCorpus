from rsa.b1.b1 import KeyGenerator
from rsa.crypt.crypt import Crypt
from rsa.decrypt.decrypt import Decrypt
import math
def fonk1(file_path):
    with open(file_path, 'rb') as file_input:
        return file_input.read()
def fonk2(byte_data):
    return list(byte_data)
def fonk3():
    b1 = KeyGenerator()
    return b1.generate()
def fonk4(b8, byte_data):
    b2 = Crypt(b8)
    return b2.crypt(byte_data)
def fonk5(private_key, encrypted_data):
    b3 = Decrypt(private_key)
    return b3.decrypt(encrypted_data)
def fonk6():
    b4 = []
    for num in range(10_000_000_000, 1_000_000_000, -1):
        if all(num % i != 0 for i in range(2, round(math.sqrt(num)) + 1)):
            b4.append(num)
        if len(b4) == 2:
            break
    return b4
def fonk7():
    b5 = "files/input.txt"
    b6 = fonk1(b5)
    b7 = fonk2(b6)
    private_key, b8 = fonk3()
    b9 = fonk4(b8, b7)
    b10 = fonk5(private_key, b9)
    b11 = fonk6()
    print("Original Bytes:", b6)
    print("Encrypted Bytes:", b9)
    print("Decrypted Bytes:", bytes(b10))
    print("Prime Numbers within Range:", b11)
if b12 = = "__main__":
    fonk7()