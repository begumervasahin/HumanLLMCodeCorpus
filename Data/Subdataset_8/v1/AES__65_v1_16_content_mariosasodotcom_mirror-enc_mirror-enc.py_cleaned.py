__version__ = '1.0.0'
__license__ = 'GPLv3'
__author__ = 'Mario Saso'
__email__ = 'mariosaso@protonmail.com'
__url__ = 'https:
banner =
menu =
import sys
import subprocess
def set_option(opts):
    option = input('Choose a number > ')
    while option not in opts:
        option = input('Choose a number > ')
    print()
    return option
def normalize(string):
    if (string[0] == '\''):
        return string.split('\'')[1]
    elif (string[0] == '\"'):
        return string.split('\"')[1]
    return string
def clear_screen():
    subprocess.run(['clear'])
def aes_enc(file):
    command = ["gpg", "-a", "-o", file+".aes", "--symmetric", "--cipher-algo", "AES256", file]
    run_command(command)
def aes_dec(file):
    command = ["gpg", "-o", file[:-4], "-d", file]
    run_command(command)
def rsa_gen():
    command = ["gpg", "--full-generate-key"]
    run_command(command)
def rsa_def_gen():
    command = ["gpg", "--gen-key"]
    run_command(command)
def rsa_import(file):
    command = ["gpg", "--import", file]
    run_command(command)
def rsa_export(uid):
    command = ["gpg", "--export", uid]
    run_command(command)
def rsa_list():
    command = ["gpg", "--list-keys"]
    run_command(command)
def rsa_sec_list():
    command = ["gpg", "--list-secret-keys"]
    run_command(command)
def rsa_delete(uid):
    command = ["gpg", "--delete-key", uid]
    run_command(command)
def rsa_sec_delete(uid):
    command = ["gpg", "--delete-secret-key", uid]
    run_command(command)
def rsa_enc(uid_pub, file):
    command = ["gpg", "-o", file+".rsa", "-r", uid_pub, "--armor", "--encrypt", file]
    run_command(command)
def rsa_dec(uid_prv, file):
    command = ["gpg", "-o", file[:-4], "-u", uid_prv, "-d", file]
    run_command(command)
def md5(file):
    command = ["md5sum", file]
    run_command(command)
def sha1(file):
    command = ["sha1sum", file]
    run_command(command)
def sha224(file):
    command = ["sha224sum", file]
    run_command(command)
def sha256(file):
    command = ["sha256sum", file]
    run_command(command)
def run_command(command):
    out = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if out.returncode == 0:
        print("\n[+] Operation completed successfully")
        print(out.stdout.decode('utf-8'))
    else:
        print("\n[-] An error has occurred")
        print(out.stderr.decode('utf-8'))
def start():
    opts = ['00', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
    print(banner)
    print(menu)
    while True:
        option = set_option(opts)
        if option == '00':
            sys.exit()
        elif option == '0':
            clear_screen()
            print(menu)
        elif option == '1':
            file = normalize(input('Enter the path of the file: '))
            aes_enc(file)
        elif option == '2':
            file = normalize(input('Enter the path of the file: '))
            aes_dec(file)
        elif option == '3':
            rsa_gen()
        elif option == '4':
            rsa_def_gen()
        elif option == '5':
            file = normalize(input('Enter the path of the key file: '))
            rsa_import(file)
        elif option == '6':
            uid = input('Enter the user ID: ')
            rsa_export(uid)
        elif option == '7':
            rsa_list()
        elif option == '8':
            rsa_sec_list()
        elif option == '9':
            uid = input('Enter the user ID: ')
            rsa_delete(uid)
        elif option == '10':
            uid = input('Enter the user ID: ')
            rsa_sec_delete(uid)
        elif option == '11':
            uid_pub = input('Enter the recipient\'s user ID: ')
            file = normalize(input('Enter the path of the file: '))
            rsa_enc(uid_pub, file)
        elif option == '12':
            uid_prv = input('Enter your user ID: ')
            file = normalize(input('Enter the path of the file: '))
            rsa_dec(uid_prv, file)
        elif option == '13':
            file = normalize(input('Enter the path of the file: '))
            md5(file)
        elif option == '14':
            file = normalize(input('Enter the path of the file: '))
            sha1(file)
        elif option == '15':
            file = normalize(input('Enter the path of the file: '))
            sha224(file)
        elif option == '16':
            file = normalize(input('Enter the path of the file: '))
            sha256(file)
        else:
            print("Invalid option")
if __name__ == '__main__':
    start()