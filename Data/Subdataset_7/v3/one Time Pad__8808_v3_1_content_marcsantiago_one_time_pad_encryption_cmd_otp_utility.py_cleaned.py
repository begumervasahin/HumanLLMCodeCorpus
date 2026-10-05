import argparse
from OTP import OneTimePadEncryption
def fonk1():
    b1 = argparse.ArgumentParser(description='One Time Pad Encryption Software')
    b1.add_argument('-e', '--encrypt_string', b2 = 'Encrypt a string entered by the user')
    b1.add_argument('-d', '--decrypt_string', b2 = 'Decrypt a string. Requires a key')
    b1.add_argument('-k', '--key', b2 = 'Specify the key as a string')
    b1.add_argument('-kf', '--key_file', b2 = 'Specify the key file path')
    b1.add_argument('-ef', '--encrypt_file', b2 = 'Encrypt file data')
    b1.add_argument('-df', '--decrypt_file', b2 = 'Decrypt data from a file. Key can be from a file or a string.')
    return b1.parse_args()
def fonk2():
    b3 = fonk1()
    b4 = OneTimePadEncryption.OneTimePadEncryption()
    if b3.encrypt_string:
        b4.encrypt_string_or_file(b3.encrypt_string, b5 = False)
    elif b3.encrypt_file:
        b4.encrypt_string_or_file(b3.encrypt_file, b5 = True)
    elif b3.decrypt_string and b3.key_file:
        b4.decrypt_string_or_file(b3.key_file, b3.decrypt_string, b6 = True, encrypted_string_file_mode=False)
    elif b3.decrypt_string and b3.key:
        b4.decrypt_string_or_file(b3.key, b3.decrypt_string, b6 = False, encrypted_string_file_mode=False)
    elif b3.decrypt_file and b3.key_file:
        b4.decrypt_string_or_file(b3.key_file, b3.decrypt_file, b6 = True, encrypted_string_file_mode=True)
    elif b3.decrypt_file and b3.key:
        b4.decrypt_string_or_file(b3.key, b3.decrypt_file, b6 = False, encrypted_string_file_mode=True)
    else:
        fonk3()
def fonk3():
    print()
if b7 = = "__main__":
    fonk2()