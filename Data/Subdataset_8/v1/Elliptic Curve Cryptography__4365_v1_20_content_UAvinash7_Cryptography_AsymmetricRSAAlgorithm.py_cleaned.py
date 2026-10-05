from Crypto.PublicKey import RSA
from Crypto import Random
import ast
random_generator = Random.new().read
key_pair = RSA.generate(1024, random_generator)
public_key = key_pair.publickey()
plain_text = "Hello World"
encrypted_text = public_key.encrypt(plain_text.encode(), 32)
print("Encrypted Text:", encrypted_text)
decrypted_text = key_pair.decrypt(ast.literal_eval(str(encrypted_text)))
print("Decrypted Text:", decrypted_text.decode())