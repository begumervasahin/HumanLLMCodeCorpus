
__version__ = '1.0.0'
__license__ = 'GPLv3'
__author__ = 'Mario Saso'
__email__ = 'mariosaso@protonmail.com'
__url__ = 'https:
import sys
import subprocess
BANNER =
MENU =
def clear_screen():
    subprocess.run(['clear'])
def normalize_path(file_path):
    if file_path.startswith(('\'', '\"')):
        return file_path[1:-1]
    return file_path
def execute_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        print("\n[+] Operation completed successfully")
        print(result.stdout.decode('utf-8'))
    else:
        print("\n[-] An error occurred")
        print(result.stderr.decode('utf-8'))
def aes_encrypt(file_path):
    execute_command(["gpg", "-a", "-o", f"{file_path}.aes", "--symmetric", "--cipher-algo", "AES256", file_path])
def aes_decrypt(file_path):
    execute_command(["gpg", "-o", file_path[:-4], "-d", file_path])
def rsa_generate_keypair(full=False):
    command = ["gpg", "--full-generate-key"] if full else ["gpg", "--gen-key"]
    execute_command(command)
def rsa_import_key(file_path):
    execute_command(["gpg", "--import", file_path])
def rsa_export_key(uid):
    execute_command(["gpg", "--export", uid])
def rsa_list_keys(secret=False):
    command = ["gpg", "--list-secret-keys"] if secret else ["gpg", "--list-keys"]
    execute_command(command)
def rsa_delete_key(uid, secret=False):
    command = ["gpg", "--delete-secret-key", uid] if secret else ["gpg", "--delete-key", uid]
    execute_command(command)
def rsa_encrypt(file_path, recipient_uid):
    execute_command(["gpg", "-o", f"{file_path}.rsa", "-r", recipient_uid, "--armor", "--encrypt", file_path])
def rsa_decrypt(file_path, uid):
    execute_command(["gpg", "-o", file_path[:-4], "-u", uid, "-d", file_path])
def calculate_hash(file_path, algorithm):
    execute_command([f"{algorithm}sum", file_path])
def get_user_option(options):
    option = input('Choose a number > ')
    while option not in options:
        option = input('Choose a number > ')
    print()
    return option
def main():
    clear_screen()
    print(BANNER)
    print(MENU)
    options = [str(i) for i in range(17)] + ['00']
    while True:
        try:
            option = get_user_option(options)
            file_path = ''
            uid = ''
            if option in ['1', '2', '5', '11', '12', '13', '14', '15', '16']:
                file_path = normalize_path(input('Enter the file path: '))
            if option in ['6', '9', '10', '12']:
                uid = input('Enter the UID: ')
            if option == '1':
                aes_encrypt(file_path)
            elif option == '2':
                aes_decrypt(file_path)
            elif option == '3':
                rsa_generate_keypair()
            elif option == '4':
                rsa_generate_keypair(full=True)
            elif option == '5':
                rsa_import_key(file_path)
            elif option == '6':
                rsa_export_key(uid)
            elif option == '7':
                rsa_list_keys()
            elif option == '8':
                rsa_list_keys(secret=True)
            elif option == '9':
                rsa_delete_key(uid)
            elif option == '10':
                rsa_delete_key(uid, secret=True)
            elif option == '11':
                recipient_uid = input('Enter the recipient UID: ')
                rsa_encrypt(file_path, recipient_uid)
            elif option == '12':
                rsa_decrypt(file_path, uid)
            elif option == '13':
                calculate_hash(file_path, 'md5')
            elif option == '14':
                calculate_hash(file_path, 'sha1')
            elif option == '15':
                calculate_hash(file_path, 'sha224')
            elif option == '16':
                calculate_hash(file_path, 'sha256')
            elif option == '0':
                clear_screen()
                print(BANNER)
                print(MENU)
            elif option == '00':
                print('Exiting mirror-enc...')
                break
        except KeyboardInterrupt:
            print("\n\nOperation canceled by the user.")
            sys.exit(0)
if __name__ == "__main__":
    main()