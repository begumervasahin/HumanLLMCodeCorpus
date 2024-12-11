import sys
import subprocess
class class1:
    def fonk1(self):
        self.b1 = self.fonk2()
        self.b2 = self.fonk3()
    def fonk2(self):
        return
    def fonk3(self):
        return
    def fonk4(self):
        subprocess.run(['clear'], b3 = True)
    def fonk5(self, b7):
        return b7.strip('\'"')
    def fonk6(self, command):
        try:
            b4 = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, b3=True)
            print("\n[+] Operation completed successfully")
            print(b4.stdout.decode('utf-8'))
        except subprocess.CalledProcessError as e:
            print("\n[-] An error occurred")
            print(e.stderr.decode('utf-8'))
    def fonk7(self, prompt):
        return self.fonk5(input(prompt))
    def fonk8(self):
        self.fonk4()
        print(self.b1)
        print(self.b2)
    def fonk9(self, b6):
        b5 = {
            '1': self.aes_encrypt,
            '2': self.aes_decrypt,
            '3': lambda: self.rsa_generate_keypair(False),
            '4': lambda: self.rsa_generate_keypair(True),
            '5': self.rsa_import_key,
            '6': self.rsa_export_key,
            '7': lambda: self.rsa_list_keys(False),
            '8': lambda: self.rsa_list_keys(True),
            '9': lambda: self.rsa_delete_key(False),
            '10': lambda: self.rsa_delete_key(True),
            '11': self.rsa_encrypt,
            '12': self.rsa_decrypt,
            '13': lambda: self.calculate_hash('md5'),
            '14': lambda: self.calculate_hash('sha1'),
            '15': lambda: self.calculate_hash('sha224'),
            '16': lambda: self.calculate_hash('sha256'),
            '0': self.show_banner_and_menu,
        }
        if b6 in b5:
            b5[b6]()
        elif b6 = = '00':
            print('Exiting mirror-enc...')
            sys.exit(0)
        else:
            print('Invalid b6. Please try again.')
    def fonk10(self):
        b7 = self.fonk7('Enter the file path: ')
        self.fonk6(["gpg", "-a", "-o", f"{b7}.aes", "--symmetric", "--cipher-algo", "AES256", b7])
def fonk11():
    b8 = class1()
    b8.fonk8()
    b9 = [str(i) for i in range(17)] + ['00']
    while True:
        try:
            b6 = b8.fonk7('Choose an b6 > ')
            b8.fonk9(b6)
        except KeyboardInterrupt:
            print("\nOperation canceled by the user.")
            break
if b10 = = "__main__":
    fonk11()