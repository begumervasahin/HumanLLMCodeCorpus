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