b1 = '1.0.0'
b2 = 'GPLv3'
b3 = 'Mario Saso'
b4 = 'mariosaso@protonmail.com'
b5 = 'https:
import sys
import subprocess
b6 = MENU =
b7 = {
    '1': ("Enter the path of the file: ", "encrypt_file_aes"),
    '2': ("Enter the path of the file: ", "decrypt_file_aes"),
    '3': (None, "generate_rsa_keypair"),
    '4': (None, "generate_default_rsa_keypair"),
    '5': ("Enter the path of the key file: ", "import_rsa_key"),
    '6': ("Enter the user ID: ", "export_rsa_key"),
    '7': (None, "list_public_keys"),
    '8': (None, "list_private_keys"),
    '9': ("Enter the user ID: ", "delete_public_key"),
    '10': ("Enter the user ID: ", "delete_private_key"),
    '11': ("Enter the recipient's user ID: \nEnter the path of the file: ", "encrypt_file_rsa"),
    '12': ("Enter your user ID: \nEnter the path of the file: ", "decrypt_file_rsa"),
    '13': ("Enter the path of the file: ", "generate_md5_hash"),
    '14': ("Enter the path of the file: ", "generate_sha1_hash"),
    '15': ("Enter the path of the file: ", "generate_sha224_hash"),
    '16': ("Enter the path of the file: ", "generate_sha256_hash"),
}
def fonk1():
    b8 = input('Choose a number > ')
    while b8 not in b7 and b8 not in ['0', '00']:
        print("Invalid option. Please try again.")
        b8 = input('Choose a number > ')
    return b8
def fonk2(path):
    return path.strip('\'\"')
def fonk3():
    subprocess.run(['cls' if sys.b9 = = 'win32' else 'clear'], check=True)
def fonk4(b8):
    if b8 in ['0', '00']:
        if b8 = = '00':
            sys.exit()
        elif b8 = = '0':
            fonk3()
            print(b6 + MENU)
    else:
        prompt, b10 = b7[b8]
        b11 = []
        if prompt:
            for p in prompt.split('\n'):
                b11.append(fonk2(input(p)))
        globals()[b10](*b11)
def fonk5():
    print(b6 + MENU)
    while True:
        b8 = fonk1()
        fonk4(b8)
if b12 = = '__main__':
    fonk5()