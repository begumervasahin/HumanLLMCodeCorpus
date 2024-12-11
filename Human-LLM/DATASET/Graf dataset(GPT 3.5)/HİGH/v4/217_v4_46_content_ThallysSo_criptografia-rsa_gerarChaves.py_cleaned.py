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
        return print("\nPublic keys (b5 = " + str(b5) + ", b3=" + str(b3) + ")" + "\nPrivate keys (b6=" + str(b6) + ", b3=" + str(b3) + ")\b3")
    def fonk3(self, a, b7):
        while a != 0:
            a, b7 = b7 % a, a
        return b7
    def fonk4(self, a, b8):
        for b10 in range(1, b8):
            if (a * b10) % b8 = = 1:
                return b10
        print('No modular inverse for the block.\b3')
        return None
    def fonk5(self, a):
        b9 = []
        for b10 in range(2, a):
            if self.fonk3(a, b10) == 1 and self.fonk4(b10, a) is not None:
                b9.append(b10)
        for b10 in b9:
            if b10 = = self.fonk4(b10, a):
                b9.remove(b10)
        return b9