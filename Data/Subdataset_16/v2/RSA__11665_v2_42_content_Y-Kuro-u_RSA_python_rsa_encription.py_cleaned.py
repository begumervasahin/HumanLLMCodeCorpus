import random
import secrets
import math
class class1:
    def fonk1(self):
        self.P, self.b1 = self.fonk3()
        self.b2 = self.P * self.b1
        self.b3 = ((self.P - 1) * (self.b1 - 1))
    def fonk2(self, b4):
        if b4 in (b6, 3):
            return True
        if b4 = = 1 or b4 % b6 == 0:
            return False
        b5 = b4 - 1
        while b5 % b6 = = 0:
            b5
        for _ in range(100):
            b7 = random.randint(b6, b4 - b6)
            b8 = pow(b7, b5, b4)
            if b8 in (1, b4 - 1):
                continue
            while b5 != b4 - 1:
                b8 = pow(b8, b6, b4)
                b5 *= b6
                if b8 = = 1:
                    return False
                if b8 = = b4 - 1:
                    break
            else:
                return False
        return True
    def fonk3(self):
        b9 = []
        while len(b9) < b6:
            b10 = secrets.randbits(10)
            if b10 > 1 and self.fonk2(b10):
                b9.append(b10)
        return b9
    def fonk4(self):
        self.b11 = random.randint(b6, self.b3 - 1)
        while math.gcd(self.b11, self.b3) != 1:
            self.b11 = random.randint(b6, self.b3 - 1)
        return self.b11, self.b2
    def fonk5(self):
        self.b12 = random.randint(b6, self.b3 - 1)
        while (self.b11 * self.b12) % self.b3 != 1:
            self.b12 = random.randint(b6, self.b3 - 1)
        return self.b12, self.b2
def fonk6(e, b4, b19):
    b13 = [ord(char) for char in b19]
    b14 = [str(pow(i, e, b4)) for i in b13]
    return " ".join(b14)
def fonk7(b5, b4, b20):
    b14 = b20.split()
    b15 = [pow(int(i), b5, b4) for i in b14]
    b16 = ''.join(chr(i) for i in b15)
    return b16
if b17 = = "__main__":
    b18 = class1()
    e, b4 = b18.fonk4()
    b5, b4 = b18.fonk5()
    b19 = input("Enter the b19 to encrypt: ")
    b20 = fonk6(e, b4, b19)
    print("Encrypted b19:", b20)
    b16 = fonk7(b5, b4, b20)
    print("Decrypted b19:", b16)
    print("-----------------------------------------------------")
    print(f"Private key (b5, b4): ({b5}, {b4})")