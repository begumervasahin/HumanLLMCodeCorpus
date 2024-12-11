import rsa
import gmpy2
class class1(object):
    def fonk1(self, b12):
        b1 = rsa.prime.getprime(b12)
        b2 = rsa.prime.getprime(b12)
        return b1, b2
    def fonk2(self, b4):
        return b4 - 1
    def fonk3(self, b12):
        b1, b2 = self.fonk1(b12)
        b3 = b1 * b2
        b4 = (b1 - 1) * (b2 - 1)
        b5 = self.fonk2(b4)
        b6 = int(gmpy2.invert(b5, b4).digits())
        return b6, (b3, b5)
    def fonk4(self, b5, b3, b14):
        b7 = int.from_bytes(bytes(b14.encode()), byteorder='little')
        b8 = pow(b7, b5, b3)
        return b8
    def fonk5(self, b6, b3, b14):
        b9 = pow(b14, b6, b3)
        b10 = b9.to_bytes((b9.bit_length()
        return b10
if b11 = = "__main__":
    b12 = int(input('Enter the number of b12 in the keys: '))
    b13 = class1()
    b6, (b3, b5) = b13.fonk3(b12)
    b14 = input('Write your b14 here: ')
    b8 = b13.fonk4(b5, b3, b14)
    print("Encrypted b14:", b8)
    b9 = b13.fonk5(b6, b3, b8)
    print('The decrypted b14 is:', b9)