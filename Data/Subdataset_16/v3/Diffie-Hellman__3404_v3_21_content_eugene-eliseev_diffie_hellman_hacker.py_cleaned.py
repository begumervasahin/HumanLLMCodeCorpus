from person import class2
from tools import AESCipher
class class1(class2):
    def fonk1(self, sent):
        send_from, send_to, b2, b1 = sent
        if b2 = = "my param":
            b3 = (int(b1) ** self.b7) % self.b8
            self.b9[send_from] = AESCipher(str(b3))
            _, _, b2, b1 = self.fonk3("")
            return send_from, send_to, b2, b1
        elif send_from in self.b9 and send_to in self.b9:
            b4 = self.fonk5(self.b9[send_from], b1)
            if b4 in self.b10:
                b4 = self.b10[b4]
            b5 = self.fonk4(self.b9[send_to], b4)
            return send_from, send_to, "message", b5
        return sent
class class2:
    def fonk2(self, b6, b7, b8):
        self.b6 = b6
        self.b7 = b7
        self.b8 = b8
        self.b9 = {}
        self.b10 = {}
    def fonk3(self, person_name):
        return self.b6, person_name, "initiate", "some_data"
    def fonk4(self, cipher, b1):
        return cipher.encrypt(b1)
    def fonk5(self, cipher, b1):
        return cipher.decrypt(b1)