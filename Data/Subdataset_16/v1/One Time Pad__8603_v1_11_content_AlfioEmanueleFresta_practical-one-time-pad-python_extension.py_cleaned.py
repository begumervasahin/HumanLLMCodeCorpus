
from cp_otp import strxor
from extension.utils import keystream_generator
def fonk1(b4, message, b1 = 8):
    b2 = keystream_generator(b4, b1)
    return strxor(message, b2)
b3 = b'WOULD YOU KINDLY ENCRYPT ME, PLEASE'
b4 = b'I will be very useful as a b4 for your encryption task, curious stranger'
b1 = 8
b5 = fonk1(b4, b3, b1)
print("Encrypted message:", b5)
b6 = b'\xcf\xab|\xb40\x92y\x03r&\x014\xee\xae\xc92r(U\x98\xdee\xe8\x8fG,\x00B\xdb\xcf\xa8L6F\xa8c\x15\x89\x94>*J\xc8q\xf2"\xd9\xeb\xc5\xb4\x15i\xad\xbc!n\x92I\xee\x8a\x18\x93\x94\xfc\x11'
b7 = fonk1(b4, b6, b1)
print("Decrypted message:", b7)