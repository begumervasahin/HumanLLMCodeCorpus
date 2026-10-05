class AES256():
    import pyAesCrypt
    def __init__(self, bufferSize=512*1024):
        self.bufferSize = bufferSize
    def crypt(self, dir):
        print('-----------------------------------')
        password = input('Enter key: ')
        pyAesCrypt.encryptFile(str(dir), str(dir)+'.aes',
                               password, self.bufferSize)
        print('[Crypted] ' + str(dir) + '.aes')
    def decrypt(self, dir):
        try:
            print('-----------------------------------')
            password = input('Enter key: ')
            pyAesCrypt.decryptFile(
                str(dir) + '.aes', 'decrypted.' + str(dir), password, self.bufferSize)
            print('[Decrypted] decrypted.' + str(dir))
        except:
            print('Error! Wrong key!')