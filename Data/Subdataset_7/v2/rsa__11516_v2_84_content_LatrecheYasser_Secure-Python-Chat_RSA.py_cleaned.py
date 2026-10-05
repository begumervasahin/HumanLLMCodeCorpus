import rsa
import gmpy2
class class1(object):
    def fonk1(self, b10):
        b1 = rsa.prime.getprime(b10)
        b2 = rsa.prime.getprime(b10)
        return b1, b2
    def fonk2(self, b4):
        return b4 - 1
    def fonk3(self, b10):
        b1, b2 = self.fonk1(b10)
        b3 = b1 * b2
        b4 = (b1 - 1) * (b2 - 1)
        b5 = self.fonk2(b4)
        b6 = int(gmpy2.invert(b5, b4).digits())
        return b6, (b3, b5)
    def fonk4(self, b5, b3, b12):
        b7 = int.from_bytes(bytes(b12.encode()), byteorder='little')
        return pow(b7, b5, b3)
    def fonk5(self, b6, b3, b12):
        b8 = pow(b12, b6, b3)
        b8 = b8.to_bytes((b8.bit_length()
        return b8
if b9 = = "__main__":
    b10 = int(input('Enter the number of b10 in the keys: '))
    b11 = class1()
    b6, (b3, b5) = b11.fonk3(b10)
    b12 = input('Write your b12 here: ')
    b13 = b11.fonk4(b5, b3, b12)
    print('Encrypted b12:', b13)
    b14 = b11.fonk5(b6, b3, b13)
    print('The decrypted b12 is:', b14)