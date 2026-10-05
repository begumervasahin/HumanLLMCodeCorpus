__version__ = '1.0.0'
__license__ = 'GPLv3'
__author__ = 'Mario Saso'
__email__ = 'mariosaso@protonmail.com'
__url__ = 'https:
banner =
menu =
import sys
import subprocess
def get_user_choice(options):
    choice = input('Choose a number > ')
    while choice not in options:
        choice = input('Choose a number > ')
    print()
    return choice
def normalize_path(path):
    if path.startswith('\''):
        return path.split('\'')[1]
    elif path.startswith('\"'):
        return path.split('\"')[1]
    return path
def clear_screen():
    subprocess.run(['clear'])
def encrypt_file_aes(path):
    command = ["gpg", "-a", "-o", path + ".aes", "--symmetric", "--cipher-algo", "AES256", path]
    run_command(command)
def decrypt_file_aes(path):
    command = ["gpg", "-o", path[:-4], "-d", path]
    run_command(command)
def generate_rsa_keypair():
    command = ["gpg", "--full-generate-key"]
    run_command(command)
def generate_default_rsa_keypair():
    command = ["gpg", "--gen-key"]
    run_command(command)
def import_rsa_key(path):
    command = ["gpg", "--import", path]
    run_command(command)
def export_rsa_key(user_id):
    command = ["gpg", "--export", user_id]
    run_command(command)
def list_public_keys():
    command = ["gpg", "--list-keys"]
    run_command(command)
def list_private_keys():
    command = ["gpg", "--list-secret-keys"]
    run_command(command)
def delete_public_key(user_id):
    command = ["gpg", "--delete-key", user_id]
    run_command(command)
def delete_private_key(user_id):
    command = ["gpg", "--delete-secret-key", user_id]
    run_command(command)
def encrypt_file_rsa(user_id, path):
    command = ["gpg", "-o", path + ".rsa", "-r", user_id, "--armor", "--encrypt", path]
    run_command(command)
def decrypt_file_rsa(user_id, path):
    command = ["gpg", "-o", path[:-4], "-u", user_id, "-d", path]
    run_command(command)
def generate_md5_hash(path):
    command = ["md5sum", path]
    run_command(command)
def generate_sha1_hash(path):
    command = ["sha1sum", path]
    run_command(command)
def generate_sha224_hash(path):
    command = ["sha224sum", path]
    run_command(command)
def generate_sha256_hash(path):
    command = ["sha256sum", path]
    run_command(command)
def run_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        print("\n[+] Operation completed successfully")
        print(result.stdout.decode('utf-8'))
    else:
        print("\n[-] An error has occurred")
        print(result.stderr.decode('utf-8'))
def start():
    options = ['00', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
    print(banner)
    print(menu)
    while True:
        choice = get_user_choice(options)
        if choice == '00':
            sys.exit()
        elif choice == '0':
            clear_screen()
            print(menu)
        elif choice == '1':
            path = normalize_path(input('Enter the path of the file: '))
            encrypt_file_aes(path)
        elif choice == '2':
            path = normalize_path(input('Enter the path of the file: '))
            decrypt_file_aes(path)
        elif choice == '3':
            generate_rsa_keypair()
        elif choice == '4':
            generate_default_rsa_keypair()
        elif choice == '5':
            path = normalize_path(input('Enter the path of the key file: '))
            import_rsa_key(path)
        elif choice == '6':
            user_id = input('Enter the user ID: ')
            export_rsa_key(user_id)
        elif choice == '7':
            list_public_keys()
        elif choice == '8':
            list_private_keys()
        elif choice == '9':
            user_id = input('Enter the user ID: ')
            delete_public_key(user_id)
        elif choice == '10':
            user_id = input('Enter the user ID: ')
            delete_private_key(user_id)
        elif choice == '11':
            user_id = input('Enter the recipient\'s user ID: ')
            path = normalize_path(input('Enter the path of the file: '))
            encrypt_file_rsa(user_id, path)
        elif choice == '12':
            user_id = input('Enter your user ID: ')
            path = normalize_path(input('Enter the path of the file: '))
            decrypt_file_rsa(user_id, path)
        elif choice == '13':
            path = normalize_path(input('Enter the path of the file: '))
            generate_md5_hash(path)
        elif choice == '14':
            path = normalize_path(input('Enter the path of the file: '))
            generate_sha1_hash(path)
        elif choice == '15':
            path = normalize_path(input('Enter the path of the file: '))
            generate_sha224_hash(path)
        elif choice == '16':
            path = normalize_path(input('Enter the path of the file: '))
            generate_sha256_hash(path)
        else:
            print("Invalid option. Please try again.")
if __name__ == '__main__':
    start()