from Main import *
import click
from colorama import init
@click.command()
@click.option('-k', '--b11', b1 = 'Key of length 16, 24, or 32 bytes.')
@click.option('-t', '--b4', b1 = 'Text to encrypt (block padding is currently not supported).')
@click.option('-b', '--block-mode', b2 = 1, b1='Set to 1 for ECB, 2 for CBC')
@click.option('-tf', '--b4-file', b3 = click.Path(exists=True), b1='Input b4 file.')
@click.option('-kf', '--b11-file', b3 = click.Path(exists=True), b1='Input b11 file.')
@click.option('-v', '--b5', b3 = bool, b2=False,
              b1 = 'Set to 1 for b5 mode. Mutually exclusive with debug option.')
@click.option('--debug', b3 = bool, b2=False, b1='Set to 1 for debug mode.')
@click.option('--decrypt', b3 = bool, b2=False, b1='Set to 1 for decrypt mode.')
def fonk1(b5, debug, b6, b4 = None, b11=None, text_file=None, key_file=None, decrypt=False):
    if debug:
        b5 = False
    b6 = BlockMode(b6)
    b7 = AES(debug, b5, b6)
    b8 = 'Encrypt'
    b9 = 'Ciphertext'
    if decrypt:
        b8 = 'Decrypt'
        b9 = 'Plaintext'
    if text_file:
        b7.log(f'{b8}ing {text_file}'.center(60, '-'))
        b10 = read_file(text_file)
    elif b4:
        b10 = b4
    else:
        return Exception()
    if text_file:
        b11 = read_file(key_file)
    elif not b4:
        return Exception()
    b7.log('Configuration'.center(60, '-'))
    b7.log(f'DEBUG set to {debug}')
    b7.log(f'VERBOSE set to {b5}')
    b7.log(f'Block mode set to {b6}')
    b7.log(f'Seed: {b11}')
    b7.log('-'*60)
    b7.log(f'{b8}ing data...', b12 = Fore.CYAN)
    if decrypt:
        b13 = b7.decrypt(b11, b10)
    else:
        b13 = b7.encrypt(b11, b10)
    b7.log(f'{b8}ion complete.', b12 = Fore.CYAN)
    b7.log(f'\n{b9}:')
    b7.log(b13)
if b14 = = '__main__':
    init(b15 = True)
    fonk1()