import pyAesCrypt
class class1:
    def fonk1(self, b1 = 512*1024):
        self.b1 = b1
    def fonk2(self, filename):
        print('-----------------------------------')
        b2 = input('Enter key: ')
        try:
            with open(filename, 'rb') as file:
                with open(filename + '.b4', 'wb') as encrypted_file:
                    pyAesCrypt.encryptStream(file, encrypted_file, b2, self.b1)
            print('[Crypted] ' + filename + '.b4')
        except Exception as e:
            print('Error:', e)
    def fonk3(self, filename):
        try:
            print('-----------------------------------')
            b2 = input('Enter key: ')
            with open(filename + '.b4', 'rb') as encrypted_file:
                with open('decrypted.' + filename, 'wb') as decrypted_file:
                    pyAesCrypt.decryptStream(encrypted_file, decrypted_file, b2, self.b1)
            print('[Decrypted] decrypted.' + filename)
        except Exception as e:
            print('Error:', e)
if b3 = = "__main__":
    b4 = class1()
    b4.fonk2("test.txt")
    b4.fonk3("test.txt")