import os
import base64
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
os.system("clear")
print()
plain_text = "Blessent mon coeur d'une langueur monotone"
company_key = 'W269N-WFGWX-YVC9B-4J6C9-T83GX'
block_size = 32
padding = lambda s: s + (block_size - len(s) % block_size) * chr(block_size - len(s) % block_size)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]
def generate_key(company_key):
    salt = 'Pots de sel et de poivre'
    key = PBKDF2(company_key, salt, 64, 1000)
    return key[:32]
def encrypt(plain_text, company_key):
    private_key = generate_key(company_key)
    text = padding(plain_text)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(text))
def decrypt(encryption, company_key):
    private_key = generate_key(company_key)
    decrypted = base64.b64decode(encryption)
    iv = decrypted[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(decrypted[16:]))
print("Plain Text  : " + plain_text)
print("Company Key : " + company_key)
print("Unique Salt : Pots de sel et de poivre")
print("Cipher Mode : CBC\n")
encrypted_text = encrypt(plain_text, company_key)
decrypted_text = decrypt(encrypted_text, company_key)
print("Encrypted   : " + encrypted_text)
print("Decrypted   : " + decrypted_text.decode() + "\n")