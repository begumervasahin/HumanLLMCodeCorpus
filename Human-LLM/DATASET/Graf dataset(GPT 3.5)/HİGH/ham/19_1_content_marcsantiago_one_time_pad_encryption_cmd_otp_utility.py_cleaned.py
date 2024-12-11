b1 = 'marcsantiago'
import argparse
from OTP import OneTimePadEncryption
b2 = OneTimePadEncryption.OneTimePadEncryption()
b3 = argparse.ArgumentParser(description='One Time Pad Encryption Software')
b3.add_argument('-e', '--encrypt_string', b4 = 'Encrypts a string that the user has entered')
b3.add_argument('-d', '--decrypt_string', b4 = 'Decrypts a string. User must also key provided a key')
b3.add_argument('-k', '--key', b4 = 'User enters the key as a string')
b3.add_argument('-kf', '--key_file', b4 = 'User enters the key file path')
b3.add_argument('-ef', '--encrypt_file', b4 = 'Encrypts file data')
b3.add_argument('-df', '--decrypt_file', b4 = 'Decrypts data from file. key can be from file or string.')
b5 = vars(b3.parse_args())
if b5['encrypt_string']:
    b2.encrypt_string_or_file(b5['encrypt_string'], b6 = False)
elif b5['encrypt_file']:
    b2.encrypt_string_or_file(b5['encrypt_file'], b6 = True)
elif b5['decrypt_string'] and b5['key_file']:
    b2.decrypt_string_or_file(b5['key_file'], b5['decrypt_string'], b7 = True,
                               b8 = False)
elif b5['decrypt_string'] and b5['key']:
    b2.decrypt_string_or_file(b5['key'], b5['decrypt_string'], b7 = False,
                               b8 = False)
elif b5['decrypt_file'] and b5['key_file']:
    b2.decrypt_string_or_file(b5['key_file'], b5['decrypt_file'], b7 = True,
                               b8 = True)
elif b5['decrypt_file'] and b5['key']:
    b2.decrypt_string_or_file(b5['key'], b5['decrypt_file'], b7 = False, b8=True)
else:
    print()