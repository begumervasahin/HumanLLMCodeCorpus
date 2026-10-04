from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto import Random
def generate_key_pair():
    random_generator = Random.new().read
    key_pair = RSA.generate(1024, random_generator)
    return key_pair, key_pair.publickey()
def create_hash(message):
    return SHA256.new(message.encode())
def sign_hash(private_key, hash_value):
    return pkcs1_15.new(private_key).sign(hash_value)
def verify_signature(public_key, hash_value, signature):
    try:
        pkcs1_15.new(public_key).verify(hash_value, signature)
        return True
    except (ValueError, TypeError):
        return False
def main():
    private_key, public_key = generate_key_pair()
    plain_text = "Hello World"
    hash_a = create_hash(plain_text)
    print("Hash A:", hash_a.hexdigest(), "\n")
    digital_signature = sign_hash(private_key, hash_a)
    print("Digital Signature:", repr(digital_signature), "\n")
    hash_b = create_hash(plain_text)
    print("Hash B:", hash_b.hexdigest(), "\n")
    is_valid = verify_signature(public_key, hash_b, digital_signature)
    print("Match" if is_valid else "No Match")
if __name__ == "__main__":
    main()