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
        self.a1 = int(file_control.b9[0])
        self.a2 = int(file_control.b9[1])
        self.a5 = int(file_control.b9[2])
        self.a4 = int(file_control.b9[3])
        self.a3 = int(file_control.b9[4])
        return self.a4, self.a3
    def fonk3(self):
        b1 = self.fonk4(self.a6, self.a7)
        self.a1 = self.fonk5(b1)
        self.a2 = self.fonk5(b1, b3=self.a1)
        self.a3 = self.a1 * self.a2
        b2 = (self.a1 - 1) * (self.a2 - 1)
        self.a5 = math_functions.mulinv(self.a4, b2)
        return self.a4, self.a3
    def fonk4(self, start, end):
        return [i for i in range(start, end) if math_functions.is_prime(i)]
    def fonk5(self, b1, b3 = None):
        b4 = secrets.choice(b1)
        while not self.fonk6(b4, b3):
            b4 = secrets.choice(b1)
        return b4
    def fonk6(self, b4, b3):
        return (b4 - 5) % b5 = = 0 and b4 != b3
    def fonk7(self, msg):
        b6 = [pow(ord(char), self.a4, self.a3) for char in msg]
        return ' '.join(map(str, b6))
    def fonk8(self, encrypted_msg):
        b7 = map(int, encrypted_msg.split())
        b8 = [chr(pow(char, self.a5, self.a3)) for char in b7]
        return ''.join(b8)
    def fonk9(self):
        return self.a3
    def fonk10(self):
        b9 = [self.a1, self.a2, self.a5, self.a4, self.a3]
        return ' '.join(map(str, b9))