class class1():
    import pyAesCrypt
    def fonk1(self, b1 = 512*1024):
        self.b1 = b1
    def fonk2(self, dir):
        print('-----------------------------------')
        b2 = input('Enter key: ')
        pyAesCrypt.encryptFile(str(dir), str(dir)+'.aes',
                               b2, self.b1)
        print('[Crypted] ' + str(dir) + '.aes')
    def fonk3(self, dir):
        try:
            print('-----------------------------------')
            b2 = input('Enter key: ')
            pyAesCrypt.decryptFile(
                str(dir) + '.aes', 'decrypted.' + str(dir), b2, self.b1)
            print('[Decrypted] decrypted.' + str(dir))
        except:
            print('Error! Wrong key!')