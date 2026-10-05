class class1(object):
    def fonk1(self, b3, b4, b5):
        b1 = (b3 ** b4) % b5
        return b1
    def fonk2(self, b1, b7, b5):
        b2 = (b1 ** b7) % b5
        return b2
    def fonk3(self):
        b3 = input("Enter the b3: \t")
        while len(b3) > 128:
            print("You have exceeded the character limit.")
            b3 = input("Please enter the b3 again: \t")
        print('='*5 + ' Enter the public keys: ' + '='*5)
        b4 = int(input("Public key: \t"))
        b5 = int(input("Modulus: \t"))
        b6 = ''.join(chr(self.fonk1(ord(char), b4, b5)) for char in b3)
        print('Encrypted Text: ', b6, '\n')
        return b6
    def fonk4(self, b6):
        print('='*5 + ' Enter the private keys: ' + '='*5)
        b7 = int(input("Private key: \t"))
        b5 = int(input("Modulus: \t"))
        b8 = ''.join(chr(self.fonk2(ord(char), b7, b5)) for char in b6)
        return print('Decrypted Text: ', b8, '\n')