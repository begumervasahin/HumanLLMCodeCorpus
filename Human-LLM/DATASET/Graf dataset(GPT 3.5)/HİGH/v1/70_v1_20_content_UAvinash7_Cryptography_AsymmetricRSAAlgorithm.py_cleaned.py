from Crypto.PublicKey import RSA
from Crypto import Random
import ast
b1 = Random.new().read
b2 = RSA.generate(1024, b1)
b3 = b2.publickey()
b4 = "Hello World"
b5 = b3.encrypt(b4.encode(), 32)
print("Encrypted Text:", b5)
b6 = b2.decrypt(ast.literal_eval(str(b5)))
print("Decrypted Text:", b6.decode())