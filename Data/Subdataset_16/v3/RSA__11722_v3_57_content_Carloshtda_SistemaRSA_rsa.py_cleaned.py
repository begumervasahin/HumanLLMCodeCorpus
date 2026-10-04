import secrets
import sympy
def fonk1(num):
    return sympy.isprime(num)
def fonk2(e, b5):
    g, b3, b1 = fonk3(e, b5)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return b3 % b5
def fonk3(b2, b):
    if b2 = = 0:
        return (b, 0, 1)
    else:
        g, b1, b3 = fonk3(b % b2, b2)
        return (g, b3 - (b
class class1:
    def fonk4(self):
        self.a1 = 0
        self.a2 = 0
        self.a3 = 0
        self.a4 = 3
        self.a5 = 0
        self.a6 = 0
        self.a7 = 1000
    def fonk5(self, file_control):
        self.a1 = int(file_control.b11[0])
        self.a2 = int(file_control.b11[1])
        self.a5 = int(file_control.b11[2])
        self.a4 = int(file_control.b11[3])
        self.a3 = int(file_control.b11[4])
        return self.a4, self.a3
    def fonk6(self):
        b4 = [i for i in range(self.a6, self.a7) if fonk1(i)]
        self.a1 = self.fonk7(b4)
        self.a2 = self.fonk7(b4, b6=self.a1)
        self.a3 = self.a1 * self.a2
        b5 = (self.a1 - 1) * (self.a2 - 1)
        self.a5 = fonk2(self.a4, b5)
        return self.a4, self.a3
    def fonk7(self, b4, b6 = None):
        b7 = secrets.choice(b4)
        while (b7 - 5) % 6 != 0 or b7 = = b6:
            b7 = secrets.choice(b4)
        return b7
    def fonk8(self, msg):
        b8 = [pow(ord(char), self.a4, self.a3) for char in msg]
        return ' '.join(map(str, b8))
    def fonk9(self, encrypted_msg):
        b9 = map(int, encrypted_msg.split())
        b10 = [chr(pow(num, self.a5, self.a3)) for num in b9]
        return ''.join(b10)
    def fonk10(self):
        return self.a3
    def fonk11(self):
        b11 = [self.a1, self.a2, self.a5, self.a4, self.a3]
        return ' '.join(map(str, b11))
if b12 = = "__main__":
    b13 = class1()
    b14 = b13.fonk6()
    print(f"Public b11: {b14}")
    b15 = "Hello, World!"
    b16 = b13.fonk8(b15)
    print(f"Encrypted b15: {b16}")
    b17 = b13.fonk9(b16)
    print(f"Decrypted b15: {b17}")