b1 = '1.0.0'
b2 = 'GPLv3'
b3 = 'Mario Saso'
b4 = 'mariosaso@protonmail.com'
b5 = 'https:
b6 = menu =
import sys
import subprocess
def fonk1(b11):
	b7 = input('Choose a number > ')
	while b7 not in b11:
		b7 = input('Choose a number > ')
	print()
	return b7
def fonk2(string):
	if (string[0] == '\''):
		return string.split('\'')[1]
	elif (string[0] == '\"'):
		return string.split('\"')[1]
	return string
def fonk3():
	subprocess.fonk21(['clear'])
def fonk4(b13):
	b8 = ["gpg", "-a", "-o", b13+".aes", "--symmetric", "--cipher-algo", "AES256", b13]
	b9 = subprocess.fonk21(b8, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (b9.b10 = = 0):
		print("\n[+] File is correctly encrypted")
		print(b9.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(b9.stderr.decode('utf-8'))
def fonk5(b13):
	b8 = ["gpg", "-o", b13[:-4], "-d", b13]
	b9 = subprocess.fonk21(b8, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (b9.b10 = = 0):
		print("\n[+] File is correctly decrypted")
		print(b9.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(b9.stderr.decode('utf-8'))
def fonk6():
	b8 = ["gpg", "--full-generate-key"]
	b9 = subprocess.fonk21(b8, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (b9.b10 = = 0):
		print("\n[+] Keypair is correctly generated")
		print(b9.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(b9.stderr.decode('utf-8'))
def fonk7():
	b8 = ["gpg", "--gen-key"]
	b9 = subprocess.fonk21(b8, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (b9.b10 = = 0):
		print("\n[+] Keypair is correctly generated")
		print(b9.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(b9.stderr.decode('utf-8'))
def fonk8(b13):
	b8 = ["gpg", "--import", b13]
	b9 = subprocess.fonk21(b8, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (b9.b10 = = 0):
		print("\n[+] Key is correctly imported")
		print(b9.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(b9.stderr.decode('utf-8'))
def fonk9(b14):
	b8 = ["gpg", "--export", b14]
	b9 = subprocess.fonk21(b8, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (b9.b10 = = 0):
		print("\n[+] Key is correctly exported")
		print(b9.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(b9.stderr.decode('utf-8'))
def fonk10():
	b8 = ["gpg", "--list-keys"]
	b9 = subprocess.fonk21(b8, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (b9.b10 = = 0):
		print("\n[+] Public Keys are correctly loaded")
		print(b9.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(b9.stderr.decode('utf-8'))
def fonk11():
	b8 = ["gpg", "--list-secret-keys"]
	b9 = subprocess.fonk21(b8, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (b9.b10 = = 0):
		print("\n[+] Private Keys are correctly loaded")
		print(b9.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(b9.stderr.decode('utf-8'))
def fonk12(b14):
	b8 = ["gpg", "--delete-key", b14]
	b9 = subprocess.fonk21(b8, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (b9.b10 = = 0):
		print("\n[+] Key is correctly deleted")
		print(b9.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(b9.stderr.decode('utf-8'))
def fonk13(b14):
	b8 = ["gpg", "--delete-secret-key", b14]
	b9 = subprocess.fonk21(b8, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (b9.b10 = = 0):
		print("\n[+] Key is correctly deleted")
		print(b9.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(b9.stderr.decode('utf-8'))
def fonk14(uid_pub, b13):
	b8 = ["gpg", "-o", b13+".rsa", "-r", uid_pub, "--armor", "--encrypt", b13]
	b9 = subprocess.fonk21(b8, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (b9.b10 = = 0):
		print("\n[+] File is correctly encrypted")
		print(b9.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(b9.stderr.decode('utf-8'))
def fonk15(uid_prv, b13):
	b8 = ["gpg", "-o", b13[:-4], "-u", uid_prv, "-d", b13]
	b9 = subprocess.fonk21(b8, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (b9.b10 = = 0):
		print("\n[+] File is correctly decrypted")
		print(b9.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(b9.stderr.decode('utf-8'))
def fonk16(b13):
	b8 = ["md5sum", b13]
	b9 = subprocess.fonk21(b8, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (b9.b10 = = 0):
		print("\n[+] MD5 is correctly calculated")
		print(b9.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(b9.stderr.decode('utf-8'))
def fonk17(b13):
	b8 = ["sha1sum", b13]
	b9 = subprocess.fonk21(b8, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (b9.b10 = = 0):
		print("\n[+] SHA-1 is correctly calculated")
		print(b9.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(b9.stderr.decode('utf-8'))
def fonk18(b13):
	b8 = ["sha224sum", b13]
	b9 = subprocess.fonk21(b8, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (b9.b10 = = 0):
		print("\n[+] SHA-224 is correctly calculated")
		print(b9.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(b9.stderr.decode('utf-8'))
def fonk19(b13):
	b8 = ["sha256sum", b13]
	b9 = subprocess.fonk21(b8, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (b9.b10 = = 0):
		print("\n[+] SHA-256 is correctly calculated")
		print(b9.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(b9.stderr.decode('utf-8'))
def fonk20():
	b11 = ['00', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
	b7 = fonk1(b11)
	if (b7 = = '1'):
		b12 = input('File path: ')
		b13 = fonk2(b12)
		fonk4(b13)
	elif (b7 = = '2'):
		b12 = input('File path: ')
		b13 = fonk2(b12)
		fonk5(b13)
	elif (b7 = = '3'):
		fonk6()
	elif (b7 = = '4'):
		fonk7()
	elif (b7 = = '5'):
		b12 = input('Key path: ')
		b13 = fonk2(b12)
		fonk8(b13)
	elif (b7 = = '6'):
		b14 = input('UID: ')
		fonk9(b14)
	elif (b7 = = '7'):
		fonk10()
	elif (b7 = = '8'):
		fonk11()
	elif (b7 = = '9'):
		b14 = input('Public UID: ')
		fonk12(b14)
	elif (b7 = = '10'):
		b14 = input('Private UID: ')
		fonk13(b14)
	elif (b7 = = '11'):
		b14 = input('Recipient Public UID: ')
		b12 = input('File path: ')
		b13 = fonk2(b12)
		fonk14(b14, b13)
	elif (b7 = = '12'):
		b14 = input('Private UID: ')
		b12 = input('File path: ')
		b13 = fonk2(b12)
		fonk15(b14, b13)
	elif (b7 = = '13'):
		b12 = input('File path: ')
		b13 = fonk2(b12)
		fonk16(b13)
	elif (b7 = = '14'):
		b12 = input('File path: ')
		b13 = fonk2(b12)
		fonk17(b13)
	elif (b7 = = '15'):
		b12 = input('File path: ')
		b13 = fonk2(b12)
		fonk18(b13)
	elif (b7 = = '16'):
		b12 = input('File path: ')
		b13 = fonk2(b12)
		fonk19(b13)
	elif (b7 = = '0'):
		print(menu)
	elif (b7 = = '00'):
		sys.exit(0)
def fonk21():
    while 1:
        try:
            fonk20()
        except KeyboardInterrupt:
            print('\n')
            fonk21()
def fonk22():
    fonk3()
    print(b6)
    print(menu)
    fonk21()
if b15 = = '__main__':
	fonk22()