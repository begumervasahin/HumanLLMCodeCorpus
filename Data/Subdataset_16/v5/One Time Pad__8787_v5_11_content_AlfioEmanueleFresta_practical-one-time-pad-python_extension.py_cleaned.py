from cp_otp import strxor
from extension.utils import keystream_generator
def fonk1(b3: bytes, message: bytes, key_length: int) -> bytes:
    b1 = keystream_generator(b3, key_length)
    return strxor(b1, message)
def fonk2():
    b2 = b'WOULD YOU KINDLY ENCRYPT ME, PLEASE'
    b3 = b'I will be very useful as a b3 for your encryption task, curious stranger'
    b4 = b'\xcf\xab|\xb40\x92y\x03r&\x014\xee\xae\xc92r(U\x98\xdee\xe8\x8fG,\x00B\xdb\xcf\xa8L6F\xa8c\x15\x89\x94>*J\xc8q\xf2"\xd9\xeb\xc5\xb4\x15i\xad\xbc!n\x92I\xee\x8a\x18\x93\x94\xfc\x11'
    b5 = fonk1(b3, b2, key_length=len(b2))
    print("Encrypted message:", b5)
    b6 = fonk1(b3, b4, key_length=len(b4))
    print("Decrypted message:", b6)
if b7 = = "__main__":
    fonk2()