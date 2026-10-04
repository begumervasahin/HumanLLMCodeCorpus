import random
import secrets
import math
class class1:
    def fonk1(self):
        self.P, self.b1 = self.fonk3()
        self.b2 = self.P * self.b1
        self.b3 = ((self.P - 1) * (self.b1 - 1))
    def fonk2(self, b4):
        if b4 = = b6:
            return True
        if b4 = = 1 or b4 % b6 == 0:
            return False
        b5 = (b4 - 1) >> 1
        while b5 % b6 = = 0:
            b5 >>= 1
        for _ in range(100):
            b7 = random.randint(1, b4 - 1)
            b8 = b5
            b9 = pow(b7, b8, b4)
            while b8 != b4 - 1 and b9 != 1 and b9 != b4 - 1:
                b9 = (b9 * b9) % b4
                b8 <<= 1
            if b9 != b4 - 1 and b8 % b6 = = 0:
                return False
        return True
    def fonk3(self):
        b10 = []
        while len(b10) != b6:
            b11 = secrets.randbits(10)
            if b11 > 1 and self.fonk2(b11):
                b10.append(b11)
        return b10
    def fonk4(self):
        self.b12 = random.randint(1, self.b3)
        while math.gcd(int(self.b12), int(self.b3)) != 1:
            self.b12 = random.randint(1, self.b3)
        return self.b12, self.b2
    def fonk5(self):
        self.b13 = random.randint(1, self.b3)
        while (self.b12 * self.b13) % self.b3 != 1:
            self.b13 = random.randint(1, self.b3)
        return self.b13, self.b2
def fonk6(e, b4, b21):
    b14 = [ord(i) for i in b21]
    b15 = [str(pow(i, e, b4)) for i in b14]
    return " ".join(b15)
def fonk7(b5, b4, e_text):
    b16 = e_text.split(" ")
    b17 = [pow(int(i), b5, b4) for i in b16]
    b18 = [chr(i) for i in b17]
    return "".join(b18)
if b19 = = "__main__":
    b20 = class1()
    e, b4 = b20.fonk4()
    b5, b4 = b20.fonk5()
    b21 = input("Enter the b21 to encrypt: ")
    b22 = fonk6(e, b4, b21)
    print("Encrypted b21:", b22)
    b23 = fonk7(b5, b4, b22)
    print("Decrypted b21:", b23)
    print("-----------------------------------------------------")
    print("Private key (b5, b4): ({0}, {1})".format(b5, b4))