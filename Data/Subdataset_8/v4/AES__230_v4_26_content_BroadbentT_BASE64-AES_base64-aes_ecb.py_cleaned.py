import os
import base64
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
def clear_screen():
    os.system("clear")
def generate_key(company_key):
    salt = 'Pots de sel et de poivre'
    key = PBKDF2(company_key, salt.encode(), 64, 1000)
    return key[:32]
def encrypt(plaintext, company_key):
    private_key = generate_key(company_key)
    cipher = AES.new(private_key, AES.MODE_ECB)
    padded_plaintext = pad(plaintext)
    encrypted_text = cipher.encrypt(padded_plaintext)
    return base64.b64encode(encrypted_text)
def decrypt(encryption, company_key):
    private_key = generate_key(company_key)
    decrypted = base64.b64decode(encryption)
    cipher = AES.new(private_key, AES.MODE_ECB)
    unpadded_text = unpad(cipher.decrypt(decrypted))
    return unpadded_text.decode()
def pad(text):
    block_size = 32
    padding_length = block_size - len(text) % block_size
    padding = chr(padding_length) * padding_length
    return text + padding
def unpad(text):
    padding_length = text[-1]
    return text[:-padding_length]
clear_screen()
plain_text = "Blessent mon coeur d'une langueur monotone"
company_key = 'W269N-WFGWX-YVC9B-4J6C9-T83GX'
encrypted_text = encrypt(plain_text, company_key)
decrypted_text = decrypt(encrypted_text, company_key)
print("Plain Text  : " + plain_text)
print("Company Key : " + company_key)
print("Unique Salt : Pots de sel et de poivre")
print("Cipher Mode : ECB\n")
print("Encrypted   : " + encrypted_text.decode())
print("Decrypted   : " + decrypted_text + "\n")