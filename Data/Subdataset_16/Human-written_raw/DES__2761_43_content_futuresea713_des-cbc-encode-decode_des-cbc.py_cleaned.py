import pyDes
import base64
b1 = "abc123"
b2 = pyDes.des('g9G16nTs', pyDes.CBC, "g9G16nTs", pad=None, padmode=pyDes.PAD_PKCS5)
b3 = b2.encrypt(b1)
b4 = base64.b64encode(b2.encrypt(b1))
b5 = base64.b64decode(b4)
b6 = b2.decrypt(base64.b64decode(b4))
print ("Encrypted: ",b4)
print ("Decrypted: ",b2.decrypt(b3))