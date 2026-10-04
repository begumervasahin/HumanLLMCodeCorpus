import pyDes
import base64
data = "abc123"
k = pyDes.des('g9G16nTs', pyDes.CBC, "g9G16nTs", pad=None, padmode=pyDes.PAD_PKCS5)
d = k.encrypt(data)
encryptstring = base64.b64encode(k.encrypt(data))
res = base64.b64decode(encryptstring)
decryptstring = k.decrypt(base64.b64decode(encryptstring))
print ("Encrypted: ",encryptstring)
print ("Decrypted: ",k.decrypt(d))