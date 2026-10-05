from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random
random_generator = Random.new().read
key_pair = RSA.generate(1024, random_generator)
public_key = key_pair.publickey()
plain_text = "Hello World"
hash_a = SHA256.new(plain_text.encode()).digest()
digital_signature = key_pair.sign(hash_a, "")
print("Hash A:", repr(hash_a))
print("Digital Signature:", repr(digital_signature))
hash_b = SHA256.new(plain_text.encode()).digest()
print("Hash B:", repr(hash_b))
if public_key.verify(hash_b, digital_signature):
    print("Match")
else:
    print("No Match")