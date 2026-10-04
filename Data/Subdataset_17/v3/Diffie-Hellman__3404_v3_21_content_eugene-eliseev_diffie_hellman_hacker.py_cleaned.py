from person import Person
from tools import AESCipher
class Hacker(Person):
    def read_data(self, sent):
        send_from, send_to, action, data = sent
        if action == "my param":
            shared_key = (int(data) ** self.prime) % self.p
            self.keys[send_from] = AESCipher(str(shared_key))
            _, _, action, data = self.start_communication_with("")
            return send_from, send_to, action, data
        elif send_from in self.keys and send_to in self.keys:
            decoded_data = self.decode(self.keys[send_from], data)
            if decoded_data in self.messages:
                decoded_data = self.messages[decoded_data]
            encoded_data = self.encode(self.keys[send_to], decoded_data)
            return send_from, send_to, "message", encoded_data
        return sent
class Person:
    def __init__(self, name, prime, p):
        self.name = name
        self.prime = prime
        self.p = p
        self.keys = {}
        self.messages = {}
    def start_communication_with(self, person_name):
        return self.name, person_name, "initiate", "some_data"
    def encode(self, cipher, data):
        return cipher.encrypt(data)
    def decode(self, cipher, data):
        return cipher.decrypt(data)