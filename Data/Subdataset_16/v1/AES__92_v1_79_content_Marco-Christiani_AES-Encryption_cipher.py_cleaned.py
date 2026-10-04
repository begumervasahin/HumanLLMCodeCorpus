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
@click.option('-t', '--b13', b10 = 'Text to encrypt (block padding is currently not supported).')
@click.option('-b', '--block-b1', b11 = 1, b10='Set to 1 for a1, 2 for a2')
@click.option('-tf', '--b13-file', b12 = click.Path(exists=True), b10='Input b13 file.')
@click.option('-kf', '--b6-file', b12 = click.Path(exists=True), b10='Input b6 file.')
@click.option('-v', '--b3', b12 = bool, b11=False, b10='Set to 1 for b3 b1. Mutually exclusive with b2 option.')
@click.option('--b2', b12 = bool, b11=False, b10='Set to 1 for b2 b1.')
@click.option('--decrypt', b12 = bool, b11=False, b10='Set to 1 for decrypt b1.')
def fonk9(b3, b2, b4, b13 = None, b6=None, text_file=None, key_file=None, decrypt=False):
    if b2:
        b3 = False
    b4 = class1(b4)
    b14 = class2(b2, b3, b4)
    b15 = 'Encrypt'
    b16 = 'Ciphertext'
    if decrypt:
        b15 = 'Decrypt'
        b16 = 'Plaintext'
    if text_file:
        b14.fonk6(f'{b15}ing {text_file}'.center(60, '-'))
        b17 = fonk1(text_file)
    elif b13:
        b17 = b13
    else:
        raise Exception('No b13 provided for encryption/decryption')
    if key_file:
        b6 = fonk1(key_file)
    elif not b6:
        raise Exception('No b6 provided for encryption/decryption')
    b14.fonk6('Configuration'.center(60, '-'))
    b14.fonk6(f'DEBUG set to {b2}')
    b14.fonk6(f'VERBOSE set to {b3}')
    b14.fonk6(f'Block b1 set to {b4.b1}')
    b14.fonk6(f'Seed: {b6}')
    b14.fonk6('-' * 60)
    b14.fonk6(f'{b15}ing data...', b5 = Fore.CYAN)
    if decrypt:
        b18 = b14.fonk8(b6, b17.encode('utf-8'))
    else:
        b18 = b14.fonk7(b6, b17)
    b14.fonk6(f'{b15}ion complete.', b5 = Fore.CYAN)
    b14.fonk6(f'\n{b16}:')
    b14.fonk6(b18)
if b19 = = '__main__':
    init(b20 = True)
    fonk9()