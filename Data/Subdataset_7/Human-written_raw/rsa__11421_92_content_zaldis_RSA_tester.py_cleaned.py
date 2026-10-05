from rsa.crypt.crypt import Crypt
from rsa.decrypt.decrypt import Decrypt
from rsa.b3.b3 import KeyGenerator
b1 = []
with open("files/input.txt", 'rb') as fin:
    for byte in fin:
        b1.append(byte)
    b1 = b''.join(b1)
b2 = []
for byte in b1:
    b2.append(int(byte))
print(b1)
print(b2)
b3 = KeyGenerator()
priv_key, b4 = b3.generate()
b5 = Crypt(b4)
b6 = b5.crypt(b2)
print(b6)
b7 = Decrypt(priv_key)
print(b7.decrypt(b6))
def fonk1():
    import math
    b8 = []
    for num in range(10_000_000_000, 1_000_000_000, -1):
        b9 = True
        print(f'check num: {num}')
        for b10 in range(2, round(math.sqrt(num))):
            print(f'\ton b10: {b10}')
            if num % b10 = = 0:
                b9 = False
                break
        if b9:
            b8.append(num)
        if len(b8) == 2:
            break
    print(b8)