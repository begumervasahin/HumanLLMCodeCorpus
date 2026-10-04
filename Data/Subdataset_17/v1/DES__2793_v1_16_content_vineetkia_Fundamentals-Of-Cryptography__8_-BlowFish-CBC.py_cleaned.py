from Crypto.Cipher import Blowfish
from struct import pack
def blowfish_encrypt(key, plaintext):
    cipher = Blowfish.new(key, Blowfish.MODE_CBC)
    bs = Blowfish.block_size
    plen = bs - len(plaintext) % bs
    padding = [plen] * plen
    padding = pack('b' * plen, *padding)
    encrypted_msg = cipher.iv + cipher.encrypt(plaintext + padding)
    return encrypted_msg
if __name__ == "__main__":
    key = b'An arbitrarily long key'
    plaintext = b'docendo discimus '
    encrypted_msg = blowfish_encrypt(key, plaintext)
    print("Encrypted message:", encrypted_msg)