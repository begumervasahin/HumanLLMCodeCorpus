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
def fonk2(b12):
    if b12.startswith('\''):
        return b12.split('\'')[1]
    elif b12.startswith('\"'):
        return b12.split('\"')[1]
    return b12
def fonk3():
    subprocess.run(['clear'])
def fonk4(b12):
    b8 = ["gpg", "-a", "-o", b12 + ".aes", "--symmetric", "--cipher-algo", "AES256", b12]
    fonk20(b8)
def fonk5(b12):
    b8 = ["gpg", "-o", b12[:-4], "-d", b12]
    fonk20(b8)
def fonk6():
    b8 = ["gpg", "--full-generate-key"]
    fonk20(b8)
def fonk7():
    b8 = ["gpg", "--gen-key"]
    fonk20(b8)
def fonk8(b12):
    b8 = ["gpg", "--import", b12]
    fonk20(b8)
def fonk9(b13):
    b8 = ["gpg", "--export", b13]
    fonk20(b8)
def fonk10():
    b8 = ["gpg", "--list-keys"]
    fonk20(b8)
def fonk11():
    b8 = ["gpg", "--list-secret-keys"]
    fonk20(b8)
def fonk12(b13):
    b8 = ["gpg", "--delete-key", b13]
    fonk20(b8)
def fonk13(b13):
    b8 = ["gpg", "--delete-secret-key", b13]
    fonk20(b8)
def fonk14(b13, b12):
    b8 = ["gpg", "-o", b12 + ".rsa", "-r", b13, "--armor", "--encrypt", b12]
    fonk20(b8)
def fonk15(b13, b12):
    b8 = ["gpg", "-o", b12[:-4], "-u", b13, "-d", b12]
    fonk20(b8)
def fonk16(b12):
    b8 = ["md5sum", b12]
    fonk20(b8)
def fonk17(b12):
    b8 = ["sha1sum", b12]
    fonk20(b8)
def fonk18(b12):
    b8 = ["sha224sum", b12]
    fonk20(b8)
def fonk19(b12):
    b8 = ["sha256sum", b12]
    fonk20(b8)
def fonk20(b8):
    b9 = subprocess.run(b8, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if b9.b10 = = 0:
        print("\n[+] Operation completed successfully")
        print(b9.stdout.decode('utf-8'))
    else:
        print("\n[-] An error has occurred")
        print(b9.stderr.decode('utf-8'))
def fonk21():
    b11 = ['00', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
    print(b6)
    print(menu)
    while True:
        b7 = fonk1(b11)
        if b7 = = '00':
            sys.exit()
        elif b7 = = '0':
            fonk3()
            print(menu)
        elif b7 = = '1':
            b12 = fonk2(input('Enter the b12 of the file: '))
            fonk4(b12)
        elif b7 = = '2':
            b12 = fonk2(input('Enter the b12 of the file: '))
            fonk5(b12)
        elif b7 = = '3':
            fonk6()
        elif b7 = = '4':
            fonk7()
        elif b7 = = '5':
            b12 = fonk2(input('Enter the b12 of the key file: '))
            fonk8(b12)
        elif b7 = = '6':
            b13 = input('Enter the user ID: ')
            fonk9(b13)
        elif b7 = = '7':
            fonk10()
        elif b7 = = '8':
            fonk11()
        elif b7 = = '9':
            b13 = input('Enter the user ID: ')
            fonk12(b13)
        elif b7 = = '10':
            b13 = input('Enter the user ID: ')
            fonk13(b13)
        elif b7 = = '11':
            b13 = input('Enter the recipient\'s user ID: ')
            b12 = fonk2(input('Enter the b12 of the file: '))
            fonk14(b13, b12)
        elif b7 = = '12':
            b13 = input('Enter your user ID: ')
            b12 = fonk2(input('Enter the b12 of the file: '))
            fonk15(b13, b12)
        elif b7 = = '13':
            b12 = fonk2(input('Enter the b12 of the file: '))
            fonk16(b12)
        elif b7 = = '14':
            b12 = fonk2(input('Enter the b12 of the file: '))
            fonk17(b12)
        elif b7 = = '15':
            b12 = fonk2(input('Enter the b12 of the file: '))
            fonk18(b12)
        elif b7 = = '16':
            b12 = fonk2(input('Enter the b12 of the file: '))
            fonk19(b12)
        else:
            print("Invalid option. Please try again.")
if b14 = = '__main__':
    fonk21()