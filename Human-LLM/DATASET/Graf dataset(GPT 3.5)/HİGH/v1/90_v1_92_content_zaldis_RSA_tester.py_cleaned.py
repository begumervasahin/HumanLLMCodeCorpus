
from rsa.crypt.crypt import Crypt
from rsa.decrypt.decrypt import Decrypt
from rsa.b1.b1 import KeyGenerator
def fonk1(file_path):
    with open(file_path, 'rb') as fin:
        return fin.read()
def fonk2(data_bytes):
    b1 = KeyGenerator()
    priv_key, b2 = b1.generate()
    b3 = Crypt(b2)
    b4 = b3.crypt(list(data_bytes))
    print(b4)
    b5 = Decrypt(priv_key)
    b6 = b5.decrypt(b4)
    print(bytes(b6))
def fonk3():
    import math
    b7 = []
    for num in range(10_000, 2, -1):
        b8 = True
        for b9 in range(2, int(math.sqrt(num)) + 1):
            if num % b9 = = 0:
                b8 = False
                break
        if b8:
            b7.append(num)
        if len(b7) == 2:
            break
    print(b7)
if b10 = = "__main__":
    b11 = fonk1("files/input.txt")
    print(b11)
    print(list(b11))
    fonk2(b11)
    fonk3()