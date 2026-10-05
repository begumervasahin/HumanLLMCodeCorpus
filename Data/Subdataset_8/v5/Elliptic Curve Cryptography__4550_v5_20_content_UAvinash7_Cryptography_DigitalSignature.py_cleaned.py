from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random
def generate_rsa_key_pair(key_length=1024):
    random_generator = Random.new().read
    key_pair = RSA.generate(key_length, random_generator)
    return key_pair
def calculate_hash(message):
    hash_object = SHA256.new(message.encode())
    return hash_object.digest()
def sign_message(private_key, message_hash):
    digital_signature = private_key.sign(message_hash, "")
    return digital_signature
def verify_signature(public_key, message_hash, digital_signature):
    is_valid = public_key.verify(message_hash, digital_signature)
    return is_valid
def main():
    key_pair = generate_rsa_key_pair()
    public_key = key_pair.publickey()
    plain_text = "Hello World"
    hash_a = calculate_hash(plain_text)
    digital_signature = sign_message(key_pair, hash_a)
    print("Hash A:", repr(hash_a))
    print("Digital Signature:", repr(digital_signature))
    hash_b = calculate_hash(plain_text)
    print("Hash B:", repr(hash_b))
    is_signature_valid = verify_signature(public_key, hash_b, digital_signature)
    if is_signature_valid:
        print("Match")
    else:
        print("No Match")
if __name__ == "__main__":
    main()