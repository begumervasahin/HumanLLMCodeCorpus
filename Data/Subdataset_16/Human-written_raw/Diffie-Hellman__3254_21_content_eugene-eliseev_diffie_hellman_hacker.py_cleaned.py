from person import Person
from tools import AESCipher
class class1(Person):
    def fonk1(self, sent):
        send_from, send_to, b2, b1 = sent
        if b2 = = "my param":
            b3 = (int(b1) ** self.prime) % self.p
            self.keys[send_from] = AESCipher(str(b3))
            _, _, b2, b1 = self.start_communication_with("")
            return send_from, send_to, b2, b1
        elif send_from in self.keys and send_to in self.keys:
            b1 = self.decode(self.keys[send_from], b1)
            if b1 in self.messages:
                b1 = self.messages[b1]
            return send_from, send_to, "message", self.encode(self.keys[send_to], b1)
        return sent