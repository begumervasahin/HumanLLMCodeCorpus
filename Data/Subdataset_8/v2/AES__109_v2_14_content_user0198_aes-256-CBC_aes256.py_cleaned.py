import pyAesCrypt
class AES256:
    def __init__(self, bufferSize=512*1024):
        self.bufferSize = bufferSize
    def crypt(self, filename):
        print('-----------------------------------')
        password = input('Enter key: ')
        try:
            with open(filename, 'rb') as file:
                with open(filename + '.aes', 'wb') as encrypted_file:
                    pyAesCrypt.encryptStream(file, encrypted_file, password, self.bufferSize)
            print('[Crypted] ' + filename + '.aes')
        except Exception as e:
            print('Error:', e)
    def decrypt(self, filename):
        try:
            print('-----------------------------------')
            password = input('Enter key: ')
            with open(filename + '.aes', 'rb') as encrypted_file:
                with open('decrypted.' + filename, 'wb') as decrypted_file:
                    pyAesCrypt.decryptStream(encrypted_file, decrypted_file, password, self.bufferSize)
            print('[Decrypted] decrypted.' + filename)
        except Exception as e:
            print('Error:', e)
if __name__ == "__main__":
    aes = AES256()
    aes.crypt("test.txt")
    aes.decrypt("test.txt")