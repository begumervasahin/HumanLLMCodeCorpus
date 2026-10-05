import pyAesCrypt
class AES256:
    def __init__(self, bufferSize=512*1024):
        self.bufferSize = bufferSize
    def crypt(self, filename):
        print('-----------------------------------')
        password = input('Enter key: ')
        try:
            pyAesCrypt.encryptFile(filename, filename + '.aes', password, self.bufferSize)
            print('[Crypted] ' + filename + '.aes')
        except Exception as e:
            print('Error:', e)
    def decrypt(self, filename):
        try:
            print('-----------------------------------')
            password = input('Enter key: ')
            pyAesCrypt.decryptFile(filename + '.aes', 'decrypted.' + filename, password, self.bufferSize)
            print('[Decrypted] decrypted.' + filename)
        except Exception as e:
            print('Error:', e)