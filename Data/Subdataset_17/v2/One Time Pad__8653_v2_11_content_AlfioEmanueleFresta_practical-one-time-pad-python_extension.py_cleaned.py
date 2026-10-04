
from cp_otp import strxor
from extension.utils import keystream_generator
def stream_cipher(key, message, key_length=8):
    keystream = keystream_generator(key, key_length)
    return strxor(message, keystream)
if __name__ == "__main__":
    plaintext = b'WOULD YOU KINDLY ENCRYPT ME, PLEASE'
    key = b'I will be very useful as a key for your encryption task, curious stranger'
    key_length = 8
    encrypted_message = stream_cipher(key, plaintext, key_length)
    print("Encrypted message:", encrypted_message)
    secret = b'\xcf\xab|\xb40\x92y\x03r&\x014\xee\xae\xc92r(U\x98\xdee\xe8\x8fG,\x00B\xdb\xcf\xa8L6F\xa8c\x15\x89\x94>*J\xc8q\xf2"\xd9\xeb\xc5\xb4\x15i\xad\xbc!n\x92I\xee\x8a\x18\x93\x94\xfc\x11'
    decrypted_message = stream_cipher(key, secret, key_length)
    print("Decrypted message:", decrypted_message)