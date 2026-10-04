import random
import secrets
import math
class class1:
    def fonk1(self):
        self.P, self.b1 = self.fonk3()
        self.b2 = self.P * self.b1
        self.b3 = (self.P - 1) * (self.b1 - 1)
        self.b4 = self.fonk4()
        self.b5 = self.fonk5()
    def fonk2(self, b6):
        if b6 = = b8:
            return True
        if b6 = = 1 or b6 % b8 == 0:
            return False
        b7 = (b6 - 1)
        while b7 % b8 = = 0:
            b7
        for _ in range(100):
            b9 = random.randint(1, b6 - 1)
            b10 = b7
            b11 = pow(b9, b10, b6)
            while b10 != b6 - 1 and b11 != 1 and b11 != b6 - 1:
                b11 = (b11 * b11) % b6
                b10 *= b8
            if b11 != b6 - 1 and b10 % b8 = = 0:
                return False
        return True
    def fonk3(self):
        b12 = []
        while len(b12) < b8:
            b13 = secrets.randbits(10)
            if self.fonk2(b13):
                b12.append(b13)
        return b12
    def fonk4(self):
        b14 = random.randint(1, self.b3)
        while math.gcd(b14, self.b3) != 1:
            b14 = random.randint(1, self.b3)
        return b14
    def fonk5(self):
        b7 = random.randint(1, self.b3)
        while (self.b4 * b7) % self.b3 != 1:
            b7 = random.randint(1, self.b3)
        return b7
    def fonk6(self):
        return self.b4, self.b2
    def fonk7(self):
        return self.b5, self.b2
def fonk8(b14, b6, b20):
    b15 = [ord(char) for char in b20]
    b16 = [str(pow(char, b14, b6)) for char in b15]
    return " ".join(b16)
def fonk9(b7, b6, b21):
    b16 = [int(char) for char in b21.split()]
    b17 = [pow(char, b7, b6) for char in b16]
    return "".join(chr(char) for char in b17)
if b18 = = "__main__":
    b19 = class1()
    b14, b6 = b19.fonk6()
    b7, b6 = b19.fonk7()
    b20 = input("Enter b20 to encrypt: ")
    b21 = fonk8(b14, b6, b20)
    print("Encrypted b20:", b21)
    b22 = fonk9(b7, b6, b21)
    print("Decrypted b20:", b22)
    print("-----------------------------------------------------")
    print(f"Private key (b7): {b7}, Modulus (b6): {b6}")