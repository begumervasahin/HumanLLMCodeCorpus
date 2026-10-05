import os
import sys
from tqdm import tqdm
from termcolor import colored, cprint
class class1:
    def fonk1(self, b1):
        self.b1 = b1
    def fonk2(self):
        try:
            b2 = open(self.b1, 'rb')
        except (IOError, FileNotFoundError):
            cprint('File with name {} is not found.'.format(self.b1), b3 = 'red', attrs=['bold', 'blink'])
            sys.exit(0)
        try:
            b4 = 'cipher_' + self.b1
            b5 = open(b4, 'wb')
            b6 = b2.read()
            b6 = bytearray(b6)
            a1 = 192
            cprint('class1 Process is in progress...!', b3 = 'green', attrs=['bold'])
            for i, val in tqdm(enumerate(b6)):
                b6[i] = val ^ a1
            b5.write(b6)
        except Exception:
            cprint('Something went wrong with {}'.format(self.b1), b3 = 'red', attrs=['bold', 'blink'])
        finally:
            b5.close()
            b2.close()
class class2:
    def fonk3(self, b1):
        self.b1 = b1
    def fonk4(self):
        try:
            b5 = open(self.b1, 'rb')
        except (FileNotFoundError, IOError):
            cprint('File with name {} is not found'.format(self.b1), b3 = 'red', attrs=['bold', 'blink'])
            sys.exit(0)
        try:
            b7 = input('Enter the b1 for the class2 b14 with extension:')
            b8 = open(b7, 'wb')
            b9 = b5.read()
            a1 = 192
            b9 = bytearray(b9)
            cprint('class2 Process is in progress...!', b3 = 'green', attrs=['bold'])
            for i, val in tqdm(enumerate(b9)):
                b9[i] = val ^ a1
            b8.write(b9)
        except Exception:
            cprint('Some problem with Ciphertext unable to handle.', b3 = 'red', attrs=['bold', 'blink'])
        finally:
            b5.close()
            b8.close()
b10 = 30 * ' '
cprint('{} File class1 And class2 Tool. {}'.format(b10, b10), 'red')
cprint('{} {}'.format(b10 + 3 * ' ', 'Programmed by Sri Manikanta.'), 'green')
while True:
    cprint('1. class1', b3 = 'magenta')
    cprint('2. class2', b3 = 'magenta')
    cprint('3. Exit', b3 = 'red')
    cprint('~Python3:', b11 = ' ', b3='green')
    b12 = int(input())
    if b12 = = 1:
        b13 = '''  ___                       _   _
 | __|_ _  __ _ _ _  _ _ __| |_(_)___ _ _
 | _|| ' \/ _| '_| || | '_ \  _| / _ \ ' \
 |___|_||_\__|_|  \_, | .__/\__|_\___/_||_|
                  |__/|_|                  '''
        cprint(b13, b3 = 'red', attrs=['bold'])
        cprint('Enter the b1 for class1 with proper extension:', b11 = ' ', b3='yellow', attrs=['bold'])
        b14 = input()
        b15 = class1(b14)
        b15.fonk2()
        cprint('{} class1 is done Sucessfully...!'.format(b14), b3 = 'green', attrs=['bold'])
        cprint('Do you want to do it again (y/n):', b11 = ' ', b3='red', attrs=['bold', 'blink'])
        b16 = input()
        if b16.lower() == 'y':
            continue
        else:
            break
    elif b12 = = 2:
        b13 = '''  ___                       _   _
 |   \ ___ __ _ _ _  _ _ __| |_(_)___ _ _
 | |) / -_) _| '_| || | '_ \  _| / _ \ ' \
 |___/\___\__|_|  \_, | .__/\__|_\___/_||_|
                  |__/|_|                  '''
        cprint(b13, b3 = 'red', attrs=['bold'])
        cprint('Enter the Encrypted b1 with proper extension:', b11 = ' ', b3='yellow', attrs=['bold'])
        b14 = input()
        b17 = class2(b14)
        b17.fonk4()
        cprint('{} class2 is done Sucessfully...!'.format(b14), b3 = 'green', attrs=['bold'])
        cprint('Do you want to do it again (y/n):', b11 = ' ', b3='red', attrs=['bold', 'blink'])
        b16 = input()
        if b16.lower() == 'y':
            continue
        else:
            break
    elif b12 = = 3:
        sys.exit(0)
    else:
        print('Your b12 of selection is not available. Sorry to see you again.')