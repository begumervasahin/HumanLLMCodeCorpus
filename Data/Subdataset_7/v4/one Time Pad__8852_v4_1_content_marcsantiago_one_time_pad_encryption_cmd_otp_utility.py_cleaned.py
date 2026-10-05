
import argparse
from OTP import OneTimePadEncryption
b1 = OneTimePadEncryption.OneTimePadEncryption()
b2 = argparse.ArgumentParser(description='One Time Pad Encryption Software')
b2.add_argument('-e', '--encrypt_string', b3 = 'Encrypts a string entered by the user')
b2.add_argument('-d', '--decrypt_string', b3 = 'Decrypts a string. Requires a key provided by the user')
b2.add_argument('-k', '--key', b3 = 'The key provided by the user as a string')
b2.add_argument('-kf', '--key_file', b3 = 'The file path containing the key provided by the user')
b2.add_argument('-ef', '--encrypt_file', b3 = 'Encrypts data from a file')
b2.add_argument('-df', '--decrypt_file', b3 = 'Decrypts data from a file. The key can be provided as a file or a string.')
b4 = vars(b2.parse_args())
if b4['encrypt_string']:
    b1.encrypt_string_or_file(b4['encrypt_string'], b5 = False)
elif b4['encrypt_file']:
    b1.encrypt_string_or_file(b4['encrypt_file'], b5 = True)
elif b4['decrypt_string'] and b4['key_file']:
    b1.decrypt_string_or_file(b4['key_file'], b4['decrypt_string'], b6 = True, encrypted_string_file_mode=False)
elif b4['decrypt_string'] and b4['key']:
    b1.decrypt_string_or_file(b4['key'], b4['decrypt_string'], b6 = False, encrypted_string_file_mode=False)
elif b4['decrypt_file'] and b4['key_file']:
    b1.decrypt_string_or_file(b4['key_file'], b4['decrypt_file'], b6 = True, encrypted_string_file_mode=True)
elif b4['decrypt_file'] and b4['key']:
    b1.decrypt_string_or_file(b4['key'], b4['decrypt_file'], b6 = False, encrypted_string_file_mode=True)
else:
    print()