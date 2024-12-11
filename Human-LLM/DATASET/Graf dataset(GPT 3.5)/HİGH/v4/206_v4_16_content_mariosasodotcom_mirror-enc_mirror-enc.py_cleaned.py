
b1 = '1.0.0'
b2 = 'GPLv3'
b3 = 'Mario Saso'
b4 = 'mariosaso@protonmail.com'
b5 = 'https:
import sys
import subprocess
b6 = MENU =
def fonk1():
    subprocess.run(['clear'])
def fonk2(b14):
    if b14.startswith(('\'', '\"')):
        return b14[1:-1]
    return b14
def fonk3(b10):
    b7 = subprocess.run(b10, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if b7.b8 = = 0:
        print("\n[+] Operation completed successfully")
        print(b7.stdout.decode('utf-8'))
    else:
        print("\n[-] An error occurred")
        print(b7.stderr.decode('utf-8'))
def fonk4(b14):
    fonk3(["gpg", "-a", "-o", f"{b14}.aes", "--symmetric", "--cipher-algo", "AES256", b14])
def fonk5(b14):
    fonk3(["gpg", "-o", b14[:-4], "-d", b14])
def fonk6(b9 = False):
    b10 = ["gpg", "--b9-generate-key"] if b9 else ["gpg", "--gen-key"]
    fonk3(b10)
def fonk7(b14):
    fonk3(["gpg", "--import", b14])
def fonk8(b15):
    fonk3(["gpg", "--export", b15])
def fonk9(b11 = False):
    b10 = ["gpg", "--list-b11-keys"] if b11 else ["gpg", "--list-keys"]
    fonk3(b10)
def fonk10(b15, b11 = False):
    b10 = ["gpg", "--delete-b11-key", b15] if b11 else ["gpg", "--delete-key", b15]
    fonk3(b10)
def fonk11(b14, b16):
    fonk3(["gpg", "-o", f"{b14}.rsa", "-r", b16, "--armor", "--encrypt", b14])
def fonk12(b14, b15):
    fonk3(["gpg", "-o", b14[:-4], "-u", b15, "-d", b14])
def fonk13(b14, algorithm):
    fonk3([f"{algorithm}sum", b14])
def fonk14(b13):
    b12 = input('Choose a number > ')
    while b12 not in b13:
        b12 = input('Choose a number > ')
    print()
    return b12
def fonk15():
    fonk1()
    print(b6)
    print(MENU)
    b13 = [str(i) for i in range(17)] + ['00']
    while True:
        try:
            b12 = fonk14(b13)
            b14 = ''
            b15 = ''
            if b12 in ['1', '2', '5', '11', '12', '13', '14', '15', '16']:
                b14 = fonk2(input('Enter the file path: '))
            if b12 in ['6', '9', '10', '12']:
                b15 = input('Enter the UID: ')
            if b12 = = '1':
                fonk4(b14)
            elif b12 = = '2':
                fonk5(b14)
            elif b12 = = '3':
                fonk6()
            elif b12 = = '4':
                fonk6(b9 = True)
            elif b12 = = '5':
                fonk7(b14)
            elif b12 = = '6':
                fonk8(b15)
            elif b12 = = '7':
                fonk9()
            elif b12 = = '8':
                fonk9(b11 = True)
            elif b12 = = '9':
                fonk10(b15)
            elif b12 = = '10':
                fonk10(b15, b11 = True)
            elif b12 = = '11':
                b16 = input('Enter the recipient UID: ')
                fonk11(b14, b16)
            elif b12 = = '12':
                fonk12(b14, b15)
            elif b12 = = '13':
                fonk13(b14, 'md5')
            elif b12 = = '14':
                fonk13(b14, 'sha1')
            elif b12 = = '15':
                fonk13(b14, 'sha224')
            elif b12 = = '16':
                fonk13(b14, 'sha256')
            elif b12 = = '0':
                fonk1()
                print(b6)
                print(MENU)
            elif b12 = = '00':
                print('Exiting mirror-enc...')
                break
        except KeyboardInterrupt:
            print("\n\nOperation canceled by the user.")
            sys.exit(0)
if b17 = = "__main__":
    fonk15()