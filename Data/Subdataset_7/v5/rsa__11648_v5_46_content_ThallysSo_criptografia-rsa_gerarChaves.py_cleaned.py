from cryptography import Cryptography
class class1(Cryptography):
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
    def fonk2(self):
        b3 = self.b1 * self.b2
        b4 = (self.b1 - 1) * (self.b2 - 1)
        print("Choose your public key:\b3")
        print(str(self.fonk5(b4)) + "\b3")
        b5 = int(input())
        b6 = self.fonk4(b5, b4)
        b7 = "(b5={}, b3={})".format(b5, b3)
        b8 = "(b6={}, b3={})".format(b6, b3)
        return print("\nPublic keys " + b7 + "\nPrivate keys " + b8 + "\b3")
    def fonk3(self, a, b9):
        while a != 0:
            a, b9 = b9 % a, a
        return b9
    def fonk4(self, a, b10):
        for b12 in range(1, b10):
            if (a * b12) % b10 = = 1:
                return b12
        print('No modular inverse for the block.\b3')
        return None
    def fonk5(self, a):
        b11 = []
        for b12 in range(2, a):
            if self.fonk3(a, b12) == 1 and self.fonk4(b12, a) is not None:
                b11.append(b12)
        for b12 in b11[:]:
            if b12 = = self.fonk4(b12, a):
                b11.remove(b12)
        return b11