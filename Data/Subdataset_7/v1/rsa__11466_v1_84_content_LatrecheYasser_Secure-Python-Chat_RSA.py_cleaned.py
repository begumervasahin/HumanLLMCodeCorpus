import rsa
import gmpy2
class class1(object):
    def fonk1(self, b9):
        return rsa.prime.getprime(b9), rsa.prime.getprime(b9)
    def fonk2(self, b3):
        return b3 - 1
    def fonk3(self, b9):
        p, b1 = self.fonk1(b9)
        b2 = p * b1
        b3 = (p - 1) * (b1 - 1)
        b4 = self.fonk2(b3)
        b5 = int(gmpy2.invert(b4, b3).digits())
        return b5, (b2, b4)
    def fonk4(self, b4, b2, b11):
        b6 = int.from_bytes(bytes(b11.encode()), byteorder='little')
        return pow(b6, b4, b2)
    def fonk5(self, b5, b2, b11):
        b7 = pow(b11, b5, b2).to_bytes((b11.bit_length()
        return b7
if b8 = = "__main__":
    b9 = int(input('Enter the number of b9 in the keys: '))
    b10 = class1()
    b5, (b2, b4) = b10.fonk3(b9)
    b11 = input('Write your b11 here: ')
    b12 = b10.fonk4(b4, b2, b11)
    print('Encrypted b11:', b12)
    b13 = b10.fonk5(b5, b2, b12)
    print('The decrypted b11 is:', b13)