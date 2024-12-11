
from rsa.b3.b3 import KeyGenerator
from rsa.crypt.crypt import Crypt
from rsa.decrypt.decrypt import Decrypt
import math
with open("files/input.txt", 'rb') as file_input:
    b1 = file_input.read()
b2 = list(b1)
b3 = KeyGenerator()
private_key, b4 = b3.generate()
b5 = Crypt(b4)
b6 = b5.crypt(b2)
b7 = Decrypt(private_key)
b8 = b7.decrypt(b6)
def fonk1():
    b9 = []
    for num in range(10_000_000_000, 1_000_000_000, -1):
        b10 = True
        for b11 in range(2, round(math.sqrt(num)) + 1):
            if num % b11 = = 0:
                b10 = False
                break
        if b10:
            b9.append(num)
        if len(b9) == 2:
            break
    print(b9)
print("Original Bytes:", b1)
print("Encrypted Bytes:", b6)
print("Decrypted Bytes:", bytes(b8))