import secrets
import math_functions
class class1:
    def fonk1(self):
        self.a1 = 0
        self.a2 = 0
        self.a3 = 0
        self.a4 = 3
        self.a5 = 0
        self.a6 = 0
        self.a7 = 1000
    def fonk2(self, file_control):
        self.a2 = int(file_control.b8[0])
        self.a1 = int(file_control.b8[1])
        self.a5 = int(file_control.b8[2])
        self.a4 = int(file_control.b8[3])
        self.a3 = int(file_control.b8[4])
        return self.a4, self.a3
    def fonk3(self):
        b1 = [i for i in range(self.a6, self.a7) if math_functions.is_prime(i)]
        self.a2 = self.fonk4(b1)
        self.a1 = self.fonk4(b1, b3=self.a2)
        self.a3 = self.a2 * self.a1
        b2 = (self.a2 - 1) * (self.a1 - 1)
        self.a5 = math_functions.mulinv(self.a4, b2)
        return self.a4, self.a3
    def fonk4(self, b1, b3 = None):
        b4 = secrets.choice(b1)
        while (b4 - 5) % 6 != 0 or b4 = = b3:
            b4 = secrets.choice(b1)
        return b4
    def fonk5(self, msg):
        b5 = [pow(ord(char), self.a4, self.a3) for char in msg]
        return ' '.join(map(str, b5))
    def fonk6(self, encrypted_msg):
        b6 = map(int, encrypted_msg.split())
        b7 = [chr(pow(char, self.a5, self.a3)) for char in b6]
        return ''.join(b7)
    def fonk7(self):
        return self.a3
    def fonk8(self):
        b8 = [self.a2, self.a1, self.a5, self.a4, self.a3]
        return ' '.join(map(str, b8))