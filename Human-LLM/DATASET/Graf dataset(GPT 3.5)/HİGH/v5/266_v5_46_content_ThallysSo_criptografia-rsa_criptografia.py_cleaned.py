class class1:
    def fonk1(self, b7, b4, b5):
        b1 = (b7 ** b4) % b5
        return b1
    def fonk2(self, b1, b6, b5):
        b2 = (b1 ** b6) % b5
        return b2
    def fonk3(self, prompt, limit):
        b3 = input(prompt)
        while len(b3) > limit:
            print("You have exceeded the character limit.")
            b3 = input("Please enter the b7 again: \t")
        return b3
    def fonk4(self):
        print('='*5 + ' Enter the public keys: ' + '='*5)
        b4 = int(input("Public key: \t"))
        b5 = int(input("Modulus: \t"))
        return b4, b5
    def fonk5(self):
        print('='*5 + ' Enter the private keys: ' + '='*5)
        b6 = int(input("Private key: \t"))
        b5 = int(input("Modulus: \t"))
        return b6, b5
    def fonk6(self):
        b7 = self.fonk3("Enter the b7: \t", 128)
        b4, b5 = self.fonk4()
        b8 = ''.join(chr(self.fonk1(ord(char), b4, b5)) for char in b7)
        print('Encrypted Text: ', b8, '\n')
        return b8
    def fonk7(self, b8):
        b6, b5 = self.fonk5()
        b9 = ''.join(chr(self.fonk2(ord(char), b6, b5)) for char in b8)
        return print('Decrypted Text: ', b9, '\n')