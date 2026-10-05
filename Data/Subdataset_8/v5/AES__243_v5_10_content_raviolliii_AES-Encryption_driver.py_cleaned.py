from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
class AESCipher:
    def __init__(self, key):
        self.key = pad(key.encode(), AES.block_size)
    def encrypt(self, plaintext):
        cipher = AES.new(self.key, AES.MODE_CBC)
        iv = cipher.iv
        encrypted = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
        return iv + encrypted
def main():
    key = "Thats my Kung Fu"
    message = "Two One Nine Two"
    aes_cipher = AESCipher(key)
    encrypted_message = aes_cipher.encrypt(message)
    print("Message:\t", message)
    print("Encrypted:\t", encrypted_message.hex())
if __name__ == "__main__":
    main()