__version__ = '1.0.0'
__license__ = 'GPLv3'
__author__ = 'Mario Saso'
__email__ = 'mariosaso@protonmail.com'
__url__ = 'https:
import sys
import subprocess
BANNER =
MENU =
COMMANDS = {
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
def get_user_choice():
    choice = input('Choose a number > ')
    while choice not in COMMANDS and choice not in ['0', '00']:
        print("Invalid option. Please try again.")
        choice = input('Choose a number > ')
    return choice
def normalize_path(path):
    return path.strip('\'\"')
def clear_screen():
    subprocess.run(['cls' if sys.platform == 'win32' else 'clear'], check=True)
def execute_command(choice):
    if choice in ['0', '00']:
        if choice == '00':
            sys.exit()
        elif choice == '0':
            clear_screen()
            print(BANNER + MENU)
    else:
        prompt, function_name = COMMANDS[choice]
        args = []
        if prompt:
            for p in prompt.split('\n'):
                args.append(normalize_path(input(p)))
        globals()[function_name](*args)
def start():
    print(BANNER + MENU)
    while True:
        choice = get_user_choice()
        execute_command(choice)
if __name__ == '__main__':
    start()