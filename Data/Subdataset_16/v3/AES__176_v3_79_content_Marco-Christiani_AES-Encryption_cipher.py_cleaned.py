import click
from colorama import init, Fore
from Crypto.Cipher import AES
import os
def fonk1(file_path):
    with open(file_path, 'r') as file:
        return file.read()
def fonk2(s):
    return s + b'\0' * (AES.block_size - len(s) % AES.block_size)
def fonk3(s):
    return s.rstrip(b'\0')
class class1:
    a1 = 1
    a2 = 2
    def fonk4(self, b1):
        if b1 not in [self.a1, self.a2]:
            raise ValueError("Invalid block b1. Use 1 for a1, 2 for a2.")
        self.b1 = b1
class class2:
    def fonk5(self, b2, b3, b4):
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4.b1
    def fonk6(self, message, b5 = Fore.WHITE):
        if self.b3 or self.b2:
            print(b5 + message)
    def fonk7(self, b6, b7):
        b6 = b6.encode('utf-8')
        b7 = fonk2(b7.encode('utf-8'))
        if self.b4 = = class1.a1:
            b8 = AES.new(b6, AES.MODE_ECB)
            return b8.fonk7(b7)
        elif self.b4 = = class1.a2:
            b9 = os.urandom(AES.block_size)
            b8 = AES.new(b6, AES.MODE_CBC, b9)
            return b9 + b8.fonk7(b7)
    def fonk8(self, b6, ciphertext):
        b6 = b6.encode('utf-8')
        if self.b4 = = class1.a1:
            b8 = AES.new(b6, AES.MODE_ECB)
            return fonk3(b8.fonk8(ciphertext)).decode('utf-8')
        elif self.b4 = = class1.a2:
            b9 = ciphertext[:AES.block_size]
            b8 = AES.new(b6, AES.MODE_CBC, b9)
            return fonk3(b8.fonk8(ciphertext[AES.block_size:])).decode('utf-8')
@click.command()
@click.option('-k', '--b6', b10 = 'Key of length 16, 24, or 32 bytes.')
@click.option('-t', '--b14', b10 = 'Text to encrypt or decrypt (block padding is currently not supported).')
@click.option('-b', '--block-b1', b11 = 1, b10='Set to 1 for a1, 2 for a2')
@click.option('-tf', '--b14-file', b12 = click.Path(exists=True), b10='Input b14 file.')
@click.option('-kf', '--b6-file', b12 = click.Path(exists=True), b10='Input b6 file.')
@click.option('-v', '--b3', b13 = True, b10='Enable b3 b1. Mutually exclusive with b2 b1.')
@click.option('--b2', b13 = True, b10='Enable b2 b1.')
@click.option('--decrypt', b13 = True, b10='Enable decrypt b1.')
def fonk9(b3, b2, b4, b14 = None, b6=None, text_file=None, key_file=None, decrypt=False):
    if b2:
        b3 = False
    b4 = class1(b4)
    b15 = class2(b2, b3, b4)
    b16 = 'Encrypt'
    b17 = 'Ciphertext'
    if decrypt:
        b16 = 'Decrypt'
        b17 = 'Plaintext'
    if text_file:
        b15.fonk6(f'{b16}ing {text_file}'.center(60, '-'))
        b18 = fonk1(text_file)
    elif b14:
        b18 = b14
    else:
        raise ValueError('No b14 provided for encryption/decryption')
    if key_file:
        b6 = fonk1(key_file)
    elif not b6:
        raise ValueError('No b6 provided for encryption/decryption')
    b15.fonk6('Configuration'.center(60, '-'))
    b15.fonk6(f'DEBUG set to {b2}')
    b15.fonk6(f'VERBOSE set to {b3}')
    b15.fonk6(f'Block b1 set to {b4.b1}')
    b15.fonk6(f'Seed: {b6}')
    b15.fonk6('-' * 60)
    b15.fonk6(f'{b16}ing data...', b5 = Fore.CYAN)
    if decrypt:
        b19 = b15.fonk8(b6, b18.encode('utf-8'))
    else:
        b19 = b15.fonk7(b6, b18)
    b15.fonk6(f'{b16}ion complete.', b5 = Fore.CYAN)
    b15.fonk6(f'\n{b17}:')
    b15.fonk6(b19)
if b20 = = '__main__':
    init(b21 = True)
    fonk9()