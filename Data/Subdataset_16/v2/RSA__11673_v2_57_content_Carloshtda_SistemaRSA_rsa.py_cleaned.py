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
        self.a2 = int(file_control.b9[0])
        self.a1 = int(file_control.b9[1])
        self.a5 = int(file_control.b9[2])
        self.a4 = int(file_control.b9[3])
        self.a3 = int(file_control.b9[4])
        return self.a4, self.a3
    def fonk6(self):
        b4 = [i for i in range(self.a6, self.a7) if fonk1(i)]
        self.a2 = secrets.choice(b4)
        while (self.a2 - 5) % 6 != 0:
            self.a2 = secrets.choice(b4)
        self.a1 = secrets.choice(b4)
        while (self.a1 - 5) % 6 != 0 or (self.a2 = = self.a1):
            self.a1 = secrets.choice(b4)
        self.a3 = self.a2 * self.a1
        b5 = (self.a2 - 1) * (self.a1 - 1)
        self.a5 = fonk2(self.a4, b5)
        return self.a4, self.a3
    def fonk7(self, msg):
        b6 = [pow(ord(char), self.a4, self.a3) for char in msg]
        return ' '.join(map(str, b6))
    def fonk8(self, encrypted_msg):
        b7 = map(int, encrypted_msg.split())
        b8 = [chr(pow(num, self.a5, self.a3)) for num in b7]
        return ''.join(b8)
    def fonk9(self):
        return self.a3
    def fonk10(self):
        b9 = [self.a2, self.a1, self.a5, self.a4, self.a3]
        return ' '.join(map(str, b9))
if b10 = = "__main__":
    b11 = class1()
    b12 = b11.fonk6()
    print(f"Public b9: {b12}")
    b13 = "Hello, World!"
    b14 = b11.fonk7(b13)
    print(f"Encrypted b13: {b14}")
    b15 = b11.fonk8(b14)
    print(f"Decrypted b13: {b15}")