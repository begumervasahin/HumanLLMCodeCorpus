from Crypto.Cipher import Blowfish
from struct import pack
def blowfish_encrypt(key, plaintext):
    cipher = Blowfish.new(key, Blowfish.MODE_CBC)
    block_size = Blowfish.block_size
    padding_length = block_size - len(plaintext) % block_size
    padding = pack('b' * padding_length, *([padding_length] * padding_length))
    encrypted_message = cipher.iv + cipher.encrypt(plaintext + padding)
    return encrypted_message
def main():
    key = b'An arbitrarily long key'
    plaintext = b'docendo discimus '
    encrypted_message = blowfish_encrypt(key, plaintext)
    print("Encrypted message:", encrypted_message)
if __name__ == "__main__":
    main()