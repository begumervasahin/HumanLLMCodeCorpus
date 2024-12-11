import argparse
from OTP import OneTimePadEncryption
b1 = OneTimePadEncryption.OneTimePadEncryption()
b2 = argparse.ArgumentParser(description='One Time Pad Encryption Software')
b2.add_argument('-e', '--encrypt_string', b3 = 'Encrypts a string that the user has entered')
b2.add_argument('-d', '--decrypt_string', b3 = 'Decrypts a string. User must also key provided a key')
b2.add_argument('-k', '--key', b3 = 'User enters the key as a string')
b2.add_argument('-kf', '--key_file', b3 = 'User enters the key file path')
b2.add_argument('-ef', '--encrypt_file', b3 = 'Encrypts file data')
b2.add_argument('-df', '--decrypt_file', b3 = 'Decrypts data from file. key can be from file or string.')
b4 = vars(b2.parse_args())
if b4['encrypt_string']:
    b1.encrypt_string_or_file(b4['encrypt_string'], b5 = False)
elif b4['encrypt_file']:
    b1.encrypt_string_or_file(b4['encrypt_file'], b5 = True)
elif b4['decrypt_string'] and b4['key_file']:
    b1.decrypt_string_or_file(b4['key_file'], b4['decrypt_string'], b6 = True,
                               b7 = False)
elif b4['decrypt_string'] and b4['key']:
    b1.decrypt_string_or_file(b4['key'], b4['decrypt_string'], b6 = False,
                               b7 = False)
elif b4['decrypt_file'] and b4['key_file']:
    b1.decrypt_string_or_file(b4['key_file'], b4['decrypt_file'], b6 = True,
                               b7 = True)
elif b4['decrypt_file'] and b4['key']:
    b1.decrypt_string_or_file(b4['key'], b4['decrypt_file'], b6 = False,
                               b7 = True)
else:
    print()