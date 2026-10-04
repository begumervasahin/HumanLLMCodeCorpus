import secrets
import sympy
def fonk1(num):
    return sympy.isprime(num)
def fonk2(e, totient):
    g, b3, b1 = fonk3(e, totient)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return b3 % totient
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
        self.a2 = int(file_control.b10[0])
        self.a1 = int(file_control.b10[1])
        self.a5 = int(file_control.b10[2])
        self.a4 = int(file_control.b10[3])
        self.a3 = int(file_control.b10[4])
        b4 = (self.a4, self.a3)
        return b4
    def fonk6(self):
        b5 = [i for i in range(self.a6, self.a7) if fonk1(i)]
        self.a2 = secrets.choice(b5)
        while (self.a2 - 5) % 6 != 0:
            self.a2 = secrets.choice(b5)
        self.a1 = secrets.choice(b5)
        while (self.a1 - 5) % 6 != 0 or (self.a2 = = self.a1):
            self.a1 = secrets.choice(b5)
        self.a3 = self.a2 * self.a1
        b6 = (self.a2 - 1) * (self.a1 - 1)
        self.a5 = fonk2(self.a4, b6)
        b4 = (self.a4, self.a3)
        return b4
    def fonk7(self, msg):
        b7 = []
        for i in range(len(msg)):
            b7.append(ord(msg[i]) ** self.a4 % self.a3)
        return ' '.join(map(str, b7))
    def fonk8(self, encrypted_msg):
        b8 = encrypted_msg.split()
        b9 = []
        for i in range(len(b8)):
            b9.append(chr((int(b8[i]) ** self.a5) % self.a3))
        return ''.join(map(str, b9))
    def fonk9(self):
        return self.a3
    def fonk10(self):
        b10 = [self.a2, self.a1, self.a5, self.a4, self.a3]
        return ' '.join(map(str, b10))
if b11 = = "__main__":
    b12 = class1()
    b4 = b12.fonk6()
    print(f"Public b10: {b4}")
    b13 = "Hello, World!"
    b14 = b12.fonk7(b13)
    print(f"Encrypted b13: {b14}")
    b15 = b12.fonk8(b14)
    print(f"Decrypted b13: {b15}")