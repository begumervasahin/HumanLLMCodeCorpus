import secrets
import math_functions
''' RepresentaÃ§Ã£o Dncriptador/Decriptador de Mensagens do Sistema'''
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
        self.a2 = int(file_control.b7[0])
        self.a1 = int(file_control.b7[1])
        self.a5 = int(file_control.b7[2])
        self.a4 = int(file_control.b7[3])
        self.a3 = int(file_control.b7[4])
        b1 = (self.a4, self.a3)
        return b1
    def fonk3(self):
        b2 = [i for i in range(self.a6, self.a7) if math_functions.is_prime(i)]
        self.a2 = secrets.choice(b2)
        while (self.a2 - 5)%6 != 0:
            self.a2 = secrets.choice(b2)
        self.a1 = secrets.choice(b2)
        while (self.a1 - 5) % 6 != 0 or (self.a2 = =  self.a1):
            self.a1 = secrets.choice(b2)
        self.a3 = self.a2 * self.a1
        b3 = (self.a2 - 1) * (self.a1 - 1)
        self.a5 = math_functions.mulinv(self.a4, b3)
        b1 = (self.a4, self.a3)
        return b1
    def fonk4(self, msg):
        b4 = []
        for i in range(len(msg)):
            b4.append(ord(msg[i])**self.a4 % self.a3)
        return ' '.join(map(str, b4))
    def fonk5(self, encrypted_msg):
        b5 = encrypted_msg.split()
        b6 = []
        for i in range(len(b5)):
            b6.append(chr((int(b5[i])**self.a5) % self.a3))
        return ''.join(map(str, b6))
    def fonk6(self):
        return self.a3
    def fonk7(self):
        b7 = [self.a2, self.a1, self.a5, self.a4, self.a3]
        return ' '.join(map(str, b7))