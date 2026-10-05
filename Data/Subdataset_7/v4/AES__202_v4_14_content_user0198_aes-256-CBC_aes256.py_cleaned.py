import pyAesCrypt
class class1:
    def fonk1(self, b1 = 512*1024):
        self.b1 = b1
    def fonk2(self, filename):
        print('-----------------------------------')
        b2 = input('Enter key: ')
        try:
            pyAesCrypt.encryptFile(filename, filename + '.aes', b2, self.b1)
            print('[Crypted] ' + filename + '.aes')
        except Exception as e:
            print('Error:', e)
    def fonk3(self, filename):
        try:
            print('-----------------------------------')
            b2 = input('Enter key: ')
            pyAesCrypt.decryptFile(filename + '.aes', 'decrypted.' + filename, b2, self.b1)
            print('[Decrypted] decrypted.' + filename)
        except Exception as e:
            print('Error:', e)