import argparse
from OTP import OneTimePadEncryption
def parse_arguments():
    parser = argparse.ArgumentParser(description='One Time Pad Encryption Software')
    parser.add_argument('-e', '--encrypt_string', help='Encrypt a string entered by the user')
    parser.add_argument('-d', '--decrypt_string', help='Decrypt a string. Requires a key')
    parser.add_argument('-k', '--key', help='Specify the key as a string')
    parser.add_argument('-kf', '--key_file', help='Specify the key file path')
    parser.add_argument('-ef', '--encrypt_file', help='Encrypt file data')
    parser.add_argument('-df', '--decrypt_file', help='Decrypt data from a file. Key can be from a file or a string.')
    return parser.parse_args()
def main():
    args = parse_arguments()
    otp = OneTimePadEncryption.OneTimePadEncryption()
    if args.encrypt_string:
        otp.encrypt_string_or_file(args.encrypt_string, string_file_mode=False)
    elif args.encrypt_file:
        otp.encrypt_string_or_file(args.encrypt_file, string_file_mode=True)
    elif args.decrypt_string and args.key_file:
        otp.decrypt_string_or_file(args.key_file, args.decrypt_string, key_file_mode=True, encrypted_string_file_mode=False)
    elif args.decrypt_string and args.key:
        otp.decrypt_string_or_file(args.key, args.decrypt_string, key_file_mode=False, encrypted_string_file_mode=False)
    elif args.decrypt_file and args.key_file:
        otp.decrypt_string_or_file(args.key_file, args.decrypt_file, key_file_mode=True, encrypted_string_file_mode=True)
    elif args.decrypt_file and args.key:
        otp.decrypt_string_or_file(args.key, args.decrypt_file, key_file_mode=False, encrypted_string_file_mode=True)
    else:
        print_help_message()
def print_help_message():
    print()
if __name__ == "__main__":
    main()