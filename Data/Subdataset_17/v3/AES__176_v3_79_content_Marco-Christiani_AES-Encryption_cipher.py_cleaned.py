import click
from colorama import init, Fore
from Crypto.Cipher import AES
import os
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()
def pad(s):
    return s + b'\0' * (AES.block_size - len(s) % AES.block_size)
def unpad(s):
    return s.rstrip(b'\0')
class BlockMode:
    ECB = 1
    CBC = 2
    def __init__(self, mode):
        if mode not in [self.ECB, self.CBC]:
            raise ValueError("Invalid block mode. Use 1 for ECB, 2 for CBC.")
        self.mode = mode
class AESHandler:
    def __init__(self, debug, verbose, block_mode):
        self.debug = debug
        self.verbose = verbose
        self.block_mode = block_mode.mode
    def log(self, message, color=Fore.WHITE):
        if self.verbose or self.debug:
            print(color + message)
    def encrypt(self, key, plaintext):
        key = key.encode('utf-8')
        plaintext = pad(plaintext.encode('utf-8'))
        if self.block_mode == BlockMode.ECB:
            cipher = AES.new(key, AES.MODE_ECB)
            return cipher.encrypt(plaintext)
        elif self.block_mode == BlockMode.CBC:
            iv = os.urandom(AES.block_size)
            cipher = AES.new(key, AES.MODE_CBC, iv)
            return iv + cipher.encrypt(plaintext)
    def decrypt(self, key, ciphertext):
        key = key.encode('utf-8')
        if self.block_mode == BlockMode.ECB:
            cipher = AES.new(key, AES.MODE_ECB)
            return unpad(cipher.decrypt(ciphertext)).decode('utf-8')
        elif self.block_mode == BlockMode.CBC:
            iv = ciphertext[:AES.block_size]
            cipher = AES.new(key, AES.MODE_CBC, iv)
            return unpad(cipher.decrypt(ciphertext[AES.block_size:])).decode('utf-8')
@click.command()
@click.option('-k', '--key', help='Key of length 16, 24, or 32 bytes.')
@click.option('-t', '--text', help='Text to encrypt or decrypt (block padding is currently not supported).')
@click.option('-b', '--block-mode', default=1, help='Set to 1 for ECB, 2 for CBC')
@click.option('-tf', '--text-file', type=click.Path(exists=True), help='Input text file.')
@click.option('-kf', '--key-file', type=click.Path(exists=True), help='Input key file.')
@click.option('-v', '--verbose', is_flag=True, help='Enable verbose mode. Mutually exclusive with debug mode.')
@click.option('--debug', is_flag=True, help='Enable debug mode.')
@click.option('--decrypt', is_flag=True, help='Enable decrypt mode.')
def cipher(verbose, debug, block_mode, text=None, key=None, text_file=None, key_file=None, decrypt=False):
    if debug:
        verbose = False
    block_mode = BlockMode(block_mode)
    aes = AESHandler(debug, verbose, block_mode)
    operation = 'Encrypt'
    output_label = 'Ciphertext'
    if decrypt:
        operation = 'Decrypt'
        output_label = 'Plaintext'
    if text_file:
        aes.log(f'{operation}ing {text_file}'.center(60, '-'))
        txt = read_file(text_file)
    elif text:
        txt = text
    else:
        raise ValueError('No text provided for encryption/decryption')
    if key_file:
        key = read_file(key_file)
    elif not key:
        raise ValueError('No key provided for encryption/decryption')
    aes.log('Configuration'.center(60, '-'))
    aes.log(f'DEBUG set to {debug}')
    aes.log(f'VERBOSE set to {verbose}')
    aes.log(f'Block mode set to {block_mode.mode}')
    aes.log(f'Seed: {key}')
    aes.log('-' * 60)
    aes.log(f'{operation}ing data...', color=Fore.CYAN)
    if decrypt:
        output = aes.decrypt(key, txt.encode('utf-8'))
    else:
        output = aes.encrypt(key, txt)
    aes.log(f'{operation}ion complete.', color=Fore.CYAN)
    aes.log(f'\n{output_label}:')
    aes.log(output)
if __name__ == '__main__':
    init(autoreset=True)
    cipher()