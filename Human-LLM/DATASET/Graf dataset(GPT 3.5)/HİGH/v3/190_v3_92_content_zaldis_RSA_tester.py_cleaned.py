
from rsa.crypt.crypt import Crypt
from rsa.decrypt.decrypt import Decrypt
from rsa.key_generator.key_generator import KeyGenerator
def fonk1(file_path):
    with open(file_path, 'rb') as file:
        return file.read()
def fonk2(data_bytes):
    private_key, b1 = KeyGenerator().generate()
    b2 = Crypt(b1).crypt(list(data_bytes))
    b3 = Decrypt(private_key).decrypt(b2)
    print("Encrypted Bytes:", b2)
    print("Decrypted Bytes:", bytes(b3))
def fonk3():
    import math
    b4 = []
    for num in range(10_000, 2, -1):
        b5 = True
        for b6 in range(2, int(math.sqrt(num)) + 1):
            if num % b6 = = 0:
                b5 = False
                break
        if b5:
            b4.append(num)
        if len(b4) == 2:
            break
    print("Two Large Prime Numbers:", b4)
if b7 = = "__main__":
    b8 = fonk1("files/input.txt")
    print("Input Bytes:", b8)
    fonk2(b8)
    fonk3()