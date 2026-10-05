import os
import sys
from tqdm import tqdm
from termcolor import colored, cprint
class Encryption:
    def __init__(self, filename):
        self.filename = filename
    def encryption(self):
        try:
            with open(self.filename, 'rb') as original_file:
                content = bytearray(original_file.read())
        except (IOError, FileNotFoundError):
            cprint(f'File "{self.filename}" not found.', color='red', attrs=['bold', 'blink'])
            sys.exit(0)
        key = 192
        encrypted_filename = 'cipher_' + self.filename
        try:
            with open(encrypted_filename, 'wb') as encrypted_file:
                cprint('Encryption Process is in progress...!', color='green', attrs=['bold'])
                for i, val in tqdm(enumerate(content)):
                    content[i] = val ^ key
                encrypted_file.write(content)
        except Exception:
            cprint(f'Something went wrong with {self.filename}', color='red', attrs=['bold', 'blink'])
class Decryption:
    def __init__(self, filename):
        self.filename = filename
    def decryption(self):
        try:
            with open(self.filename, 'rb') as encrypted_file:
                cipher_text = bytearray(encrypted_file.read())
        except (FileNotFoundError, IOError):
            cprint(f'File "{self.filename}" not found.', color='red', attrs=['bold', 'blink'])
            sys.exit(0)
        key = 192
        try:
            decrypted_filename = input('Enter the filename for the Decryption file with extension:')
            with open(decrypted_filename, 'wb') as decrypted_file:
                cprint('Decryption Process is in progress...!', color='green', attrs=['bold'])
                for i, val in tqdm(enumerate(cipher_text)):
                    cipher_text[i] = val ^ key
                decrypted_file.write(cipher_text)
        except Exception:
            cprint('Some problem with Ciphertext unable to handle.', color='red', attrs=['bold', 'blink'])
space_count = 30 * ' '
cprint(f'{space_count} File Encryption And Decryption Tool. {space_count}', 'red')
cprint(f'{space_count + 3 * " "}Programmed by Sri Manikanta.', 'green')
while True:
    cprint('1. Encryption', color='magenta')
    cprint('2. Decryption', color='magenta')
    cprint('3. Exit', color='red')
    cprint('~Python3:', end=' ', color='green')
    choice = int(input())
    if choice == 1:
        logo = '''  ___                       _   _
 | __|_ _  __ _ _ _  _ _ __| |_(_)___ _ _
 | _|| ' \/ _| '_| || | '_ \  _| / _ \ ' \
 |___|_||_\__|_|  \_, | .__/\__|_\___/_||_|
                  |__/|_|                  '''
        cprint(logo, color='red', attrs=['bold'])
        cprint('Enter the filename for Encryption with proper extension:', end=' ', color='yellow', attrs=['bold'])
        file = input()
        E1 = Encryption(file)
        E1.encryption()
        cprint(f'{file} Encryption is done Successfully...!', color='green', attrs=['bold'])
        cprint('Do you want to do it again (y/n):', end=' ', color='red', attrs=['bold', 'blink'])
        again_choice = input()
        if again_choice.lower() == 'y':
            continue
        else:
            break
    elif choice == 2:
        logo = '''  ___                       _   _
 |   \ ___ __ _ _ _  _ _ __| |_(_)___ _ _
 | |) / -_) _| '_| || | '_ \  _| / _ \ ' \
 |___/\___\__|_|  \_, | .__/\__|_\___/_||_|
                  |__/|_|                  '''
        cprint(logo, color='red', attrs=['bold'])
        cprint('Enter the Encrypted filename with proper extension:', end=' ', color='yellow', attrs=['bold'])
        file = input()
        D1 = Decryption(file)
        D1.decryption()
        cprint(f'{file} Decryption is done Successfully...!', color='green', attrs=['bold'])
        cprint('Do you want to do it again (y/n):', end=' ', color='red', attrs=['bold', 'blink'])
        again_choice = input()
        if again_choice.lower() == 'y':
            continue
        else:
            break
    elif choice == 3:
        sys.exit(0)
    else:
        print('Your choice of selection is not available. Sorry to see you again.')