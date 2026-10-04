import pyDes
import base64
def fonk1(b6, b7, b8):
    b1 = pyDes.des(b7, pyDes.CBC, b8, pad=None, padmode=pyDes.PAD_PKCS5)
    b2 = b1.encrypt(b6)
    b3 = base64.b64encode(b2)
    return b3
def fonk2(b3, b7, b8):
    b4 = base64.b64decode(b3)
    b1 = pyDes.des(b7, pyDes.CBC, b8, pad=None, padmode=pyDes.PAD_PKCS5)
    b5 = b1.decrypt(b4)
    return b5
def fonk3():
    b6 = "abc123"
    b7 = 'g9G16nTs'
    b8 = 'g9G16nTs'
    b3 = fonk1(b6, b7, b8)
    b5 = fonk2(b3, b7, b8)
    print("Encrypted (base64 encoded):", b3.decode())
    print("Decrypted Data:", b5.decode())
if b9 = = "__main__":
    fonk3()