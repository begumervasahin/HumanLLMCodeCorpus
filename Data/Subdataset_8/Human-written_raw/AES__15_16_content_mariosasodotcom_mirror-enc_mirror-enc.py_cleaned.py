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
	out = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (out.returncode == 0):
		print("\n[+] File is correctly encrypted")
		print(out.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(out.stderr.decode('utf-8'))
def aes_dec(file):
	command = ["gpg", "-o", file[:-4], "-d", file]
	out = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (out.returncode == 0):
		print("\n[+] File is correctly decrypted")
		print(out.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(out.stderr.decode('utf-8'))
def rsa_gen():
	command = ["gpg", "--full-generate-key"]
	out = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (out.returncode == 0):
		print("\n[+] Keypair is correctly generated")
		print(out.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(out.stderr.decode('utf-8'))
def rsa_def_gen():
	command = ["gpg", "--gen-key"]
	out = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (out.returncode == 0):
		print("\n[+] Keypair is correctly generated")
		print(out.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(out.stderr.decode('utf-8'))
def rsa_import(file):
	command = ["gpg", "--import", file]
	out = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (out.returncode == 0):
		print("\n[+] Key is correctly imported")
		print(out.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(out.stderr.decode('utf-8'))
def rsa_export(uid):
	command = ["gpg", "--export", uid]
	out = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (out.returncode == 0):
		print("\n[+] Key is correctly exported")
		print(out.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(out.stderr.decode('utf-8'))
def rsa_list():
	command = ["gpg", "--list-keys"]
	out = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (out.returncode == 0):
		print("\n[+] Public Keys are correctly loaded")
		print(out.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(out.stderr.decode('utf-8'))
def rsa_sec_list():
	command = ["gpg", "--list-secret-keys"]
	out = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (out.returncode == 0):
		print("\n[+] Private Keys are correctly loaded")
		print(out.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(out.stderr.decode('utf-8'))
def rsa_delete(uid):
	command = ["gpg", "--delete-key", uid]
	out = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (out.returncode == 0):
		print("\n[+] Key is correctly deleted")
		print(out.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(out.stderr.decode('utf-8'))
def rsa_sec_delete(uid):
	command = ["gpg", "--delete-secret-key", uid]
	out = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (out.returncode == 0):
		print("\n[+] Key is correctly deleted")
		print(out.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(out.stderr.decode('utf-8'))
def rsa_enc(uid_pub, file):
	command = ["gpg", "-o", file+".rsa", "-r", uid_pub, "--armor", "--encrypt", file]
	out = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (out.returncode == 0):
		print("\n[+] File is correctly encrypted")
		print(out.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(out.stderr.decode('utf-8'))
def rsa_dec(uid_prv, file):
	command = ["gpg", "-o", file[:-4], "-u", uid_prv, "-d", file]
	out = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (out.returncode == 0):
		print("\n[+] File is correctly decrypted")
		print(out.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(out.stderr.decode('utf-8'))
def md5(file):
	command = ["md5sum", file]
	out = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (out.returncode == 0):
		print("\n[+] MD5 is correctly calculated")
		print(out.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(out.stderr.decode('utf-8'))
def sha1(file):
	command = ["sha1sum", file]
	out = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (out.returncode == 0):
		print("\n[+] SHA-1 is correctly calculated")
		print(out.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(out.stderr.decode('utf-8'))
def sha224(file):
	command = ["sha224sum", file]
	out = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (out.returncode == 0):
		print("\n[+] SHA-224 is correctly calculated")
		print(out.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(out.stderr.decode('utf-8'))
def sha256(file):
	command = ["sha256sum", file]
	out = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (out.returncode == 0):
		print("\n[+] SHA-256 is correctly calculated")
		print(out.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(out.stderr.decode('utf-8'))
def start():
	opts = ['00', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
	option = set_option(opts)
	if (option == '1'):
		file_in = input('File path: ')
		file = normalize(file_in)
		aes_enc(file)
	elif (option == '2'):
		file_in = input('File path: ')
		file = normalize(file_in)
		aes_dec(file)
	elif (option == '3'):
		rsa_gen()
	elif (option == '4'):
		rsa_def_gen()
	elif (option == '5'):
		file_in = input('Key path: ')
		file = normalize(file_in)
		rsa_import(file)
	elif (option == '6'):
		uid = input('UID: ')
		rsa_export(uid)
	elif (option == '7'):
		rsa_list()
	elif (option == '8'):
		rsa_sec_list()
	elif (option == '9'):
		uid = input('Public UID: ')
		rsa_delete(uid)
	elif (option == '10'):
		uid = input('Private UID: ')
		rsa_sec_delete(uid)
	elif (option == '11'):
		uid = input('Recipient Public UID: ')
		file_in = input('File path: ')
		file = normalize(file_in)
		rsa_enc(uid, file)
	elif (option == '12'):
		uid = input('Private UID: ')
		file_in = input('File path: ')
		file = normalize(file_in)
		rsa_dec(uid, file)
	elif (option == '13'):
		file_in = input('File path: ')
		file = normalize(file_in)
		md5(file)
	elif (option == '14'):
		file_in = input('File path: ')
		file = normalize(file_in)
		sha1(file)
	elif (option == '15'):
		file_in = input('File path: ')
		file = normalize(file_in)
		sha224(file)
	elif (option == '16'):
		file_in = input('File path: ')
		file = normalize(file_in)
		sha256(file)
	elif (option == '0'):
		print(menu)
	elif (option == '00'):
		sys.exit(0)
def run():
    while 1:
        try:
            start()
        except KeyboardInterrupt:
            print('\n')
            run()
def main():
    clear_screen()
    print(banner)
    print(menu)
    run()
if __name__ == '__main__':
	main()