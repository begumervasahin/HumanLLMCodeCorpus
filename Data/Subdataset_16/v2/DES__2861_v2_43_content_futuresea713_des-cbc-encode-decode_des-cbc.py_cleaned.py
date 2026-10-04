import pyDes
import base64
b1 = "abc123"
b2 = 'g9G16nTs'
b3 = 'g9G16nTs'
b4 = pyDes.des(b2, pyDes.CBC, b3, pad=None, padmode=pyDes.PAD_PKCS5)
b5 = b4.encrypt(b1)
b6 = base64.b64encode(b5)
b7 = base64.b64decode(b6)
b8 = b4.decrypt(b7)
print("Original Data:", b1)
print("Encrypted (base64 encoded):", b6.decode())
print("Decrypted Data:", b8.decode())