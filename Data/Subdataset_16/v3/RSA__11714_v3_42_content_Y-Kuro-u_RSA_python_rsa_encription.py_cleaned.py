import random
import secrets
import math
class class1:
    def fonk1(self):
        self.P, self.b1 = self.fonk3()
        self.b2 = self.P * self.b1
        self.b3 = (self.P - 1) * (self.b1 - 1)
    def fonk2(self, b17):
        if b17 in (b4, 3):
            return True
        if b17 < b4 or b17 % b4 = = 0:
            return False
        b5 = b17 - 1
        while b5 % b4 = = 0:
            b5
        for _ in range(100):
            b6 = random.randint(b4, b17 - b4)
            b7 = pow(b6, b5, b17)
            if b7 in (1, b17 - 1):
                continue
            while b5 != b17 - 1:
                b7 = pow(b7, b4, b17)
                b5 *= b4
                if b7 = = 1:
                    return False
                if b7 = = b17 - 1:
                    break
            else:
                return False
        return True
    def fonk3(self):
        b8 = []
        while len(b8) < b4:
            b9 = secrets.randbits(10)
            if b9 > 1 and self.fonk2(b9):
                b8.append(b9)
        return b8
    def fonk4(self):
        self.b10 = random.randint(b4, self.b3 - 1)
        while math.gcd(self.b10, self.b3) != 1:
            self.b10 = random.randint(b4, self.b3 - 1)
        return self.b10, self.b2
    def fonk5(self):
        self.b11 = random.randint(b4, self.b3 - 1)
        while (self.b10 * self.b11) % self.b3 != 1:
            self.b11 = random.randint(b4, self.b3 - 1)
        return self.b11, self.b2
def fonk6(e, b17, b18):
    b12 = [ord(char) for char in b18]
    b13 = [str(pow(i, e, b17)) for i in b12]
    return " ".join(b13)
def fonk7(b5, b17, b19):
    b13 = b19.split()
    b14 = [pow(int(i), b5, b17) for i in b13]
    b15 = ''.join(chr(i) for i in b14)
    return b15
def fonk8():
    b16 = class1()
    e, b17 = b16.fonk4()
    b5, b17 = b16.fonk5()
    b18 = input("Enter the b18 to encrypt: ")
    b19 = fonk6(e, b17, b18)
    print("Encrypted b18:", b19)
    b15 = fonk7(b5, b17, b19)
    print("Decrypted b18:", b15)
    print("-----------------------------------------------------")
    print(f"Private key (b5, b17): ({b5}, {b17})")
if b20 = = "__main__":
    fonk8()