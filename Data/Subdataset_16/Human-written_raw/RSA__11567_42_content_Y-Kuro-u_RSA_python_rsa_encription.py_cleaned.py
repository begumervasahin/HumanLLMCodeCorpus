import random
import secrets
import math
class class1:
    def fonk1(self):
        self.P,self.b1 = self.fonk3()
        self.b2 = self.P * self.b1
        self.b3 = ((self.P - b6) *(self.b1 - b6) ) / math.gcd(self.P-b6, self.b1-b6)
    def fonk2(self,b4):
        if b4 = = 2: return True
        if b4 = = b6 or b4 & b6 == 0: return False
        b5 = (b4 - b6) >> b6
        while b5 & b6 = = 0:
            b5 >>= b6
        for _ in range(100):
            b7 = random.randint(b6, b4 - b6)
            b8 = b5
            b9 = pow(b7, b8, b4)
            while b8 != b4 - b6 and b9 != b6 and b9 != b4 - b6:
                b9 = (b9 * b9) % b4
                b8 <<= b6
            if b9 != b4 - b6 and b8 & b6 = = 0:
                return False
        return True
    def fonk3(self):
        b10 = []
        while len(b10) != 2:
            b11 = secrets.randbits(10)
            b12 = self.fonk2(b11)
            if b12:
                b10.append(b11)
        return b10
    def fonk4(self):
        self.b13 = random.randint(b6,self.b3)
        while math.gcd(int(self.b13),int(self.b3)) != b6:
            self.b13 = random.randint(b6,self.b3)
        return self.b13,self.b2
    def fonk5(self):
        self.b14 = random.randint(b6,self.b3)
        while (self.b13*self.b14)%self.b3 != b6:
            self.b14 = random.randint(b6,self.b3)
        return self.b14,self.b2
def fonk6(e,b4,b22):
    b15 = [ord(i) for i in b22]
    b16 = [str(pow(i,e,b4)) for i in b15]
    return " ".join(b16)
def fonk7(b5,b4,e_text):
    b17 = e_text.split(" ")
    b18 = [pow(int(i),b5,b4) for i in b17]
    b19 = [chr(i) for i in b18]
    return "".join(b19)
if b20 = = "__main__":
    b21 = class1()
    e,b4 = b21.fonk4()
    b5,b4 = b21.fonk5()
    b22 = input()
    b23 = fonk6(e,b4,b22)
    print(b23)
    b24 = fonk7(b5,b4,b23)
    print(b24)
    print("-----------------------------------------------------")
    print("b5:{0},b4:{b6}".format(b5,b4))