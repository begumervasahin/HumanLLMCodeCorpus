import rsa
import gmpy2
class class1:
    def fonk1(self):
        pass
    def fonk2(self, b14):
        return rsa.prime.getprime(b14)
    def fonk3(self, b4):
        return b4 - 1
    def fonk4(self, b14):
        b1 = self.fonk2(b14)
        b2 = self.fonk2(b14)
        b3 = b1 * b2
        b4 = (b1 - 1) * (b2 - 1)
        b5 = self.fonk3(b4)
        b6 = int(gmpy2.invert(b5, b4).digits())
        return b6, (b3, b5)
    def fonk5(self, b5, b3, b16):
        b7 = b16.encode('utf-8')
        b8 = int.from_bytes(b7, byteorder='little')
        b9 = pow(b8, b5, b3)
        return b9
    def fonk6(self, b6, b3, b9):
        b10 = pow(b9, b6, b3)
        b11 = b10.to_bytes((b10.bit_length() + 7)
        b12 = b11.decode('utf-8')
        return b12
if b13 = = "__main__":
    b14 = int(input('Enter the number of b14 in the keys: '))
    b15 = class1()
    b6, (b3, b5) = b15.fonk4(b14)
    b16 = input('Write your b16 here: ')
    b9 = b15.fonk5(b5, b3, b16)
    print('Encrypted b16:', b9)
    b12 = b15.fonk6(b6, b3, b9)
    print('The decrypted b16 is:', b12)