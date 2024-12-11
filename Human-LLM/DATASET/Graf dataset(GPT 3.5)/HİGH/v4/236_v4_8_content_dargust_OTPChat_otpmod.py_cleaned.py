import _pickle as cPickle
import string
import secrets
class class1:
    def fonk1(self, b1 = None, message_length=None, key_number=None, b8=None, outqueue=None):
        self.b2 = string.digits + string.ascii_letters + string.punctuation + " "
        self.a1 = 64
        self.b3 = 0xffff
        self.b4 = "key.dict"
        self.b5 = b1 if b1 else self.b2
        self.b6 = message_length if message_length else self.a1
        self.b7 = key_number if key_number else self.b3
        self.b8 = b8 if b8 else self.b4
        if outqueue:
            outqueue.put("Starting")
        self.b9 = secrets.SystemRandom()
        try:
            with open(self.b8, 'rb') as f:
                self.b10 = cPickle.load(f)
                print("Taking dictionary b11 from b8")
                b11 = self.b10[0]
                self.b5 = b11[0]
                self.b6 = b11[1]
                self.b7 = b11[2]
        except FileNotFoundError:
            self.fonk2(outqueue)
        print("b12 remaining: {}".format(len(self.b10) - 1))
        if outqueue:
            outqueue.put("Stopped")
    def fonk2(self, outqueue):
        print("Generating new key dictionary with {} b12".format(self.b7))
        print("This may take b5 few minutes")
        b12 = {}
        a2 = 0
        b12[0] = (self.b5, self.b6, self.b7)
        for i in range(self.b7):
            b12[i + 1] = "".join(self.b9.choice(self.b5) for i in range(self.b6))
            if i % int(self.b7 / 100) == 0:
                b13 = int(i / (self.b7 / 100))
                if b13 != a2 and outqueue:
                    outqueue.put("Step")
                    a2 = b13
        with open(self.b8, 'wb') as f:
            cPickle.dump(b12, f, -1)
        self.b10 = b12
        print("Finished")
    def fonk3(self, x):
        return len(hex(x)) - 2
    def fonk4(self, b17):
        try:
            b14 = self.fonk3(self.b7)
            b16, b15 = self.b9.choice(list(self.b10.items())[1:])
            self.b10.pop(b16)
            with open(self.b8, 'wb') as f:
                cPickle.dump(self.b10, f, -1)
            b16 = "{0:0{1}x}".format(b16, b14)
            b17 = b17.ljust(self.b6)
            if len(b17) > self.b6:
                raise ValueError("b18 length greater than {}".format(self.b6))
            b18 = b16 + ''.join(self.b5[(self.b5.index(b17[i]) + self.b5.index(b15[i])) % len(self.b5)] for i in range(self.b6))
            return b18, True
        except (KeyError, ValueError) as err:
            return "Unable to encode b18: {}".format(err), False
    def fonk5(self, b19):
        b14 = self.fonk3(self.b7)
        try:
            b15 = self.b10[int(b19[:b14], 16)]
            self.b10.pop(int(b19[:b14], 16))
            with open(self.b8, 'wb') as f:
                cPickle.dump(self.b10, f, -1)
            b19 = b19[b14:]
            return ''.join(self.b5[(self.b5.index(b19[i]) - self.b5.index(b15[i])) % len(self.b5)] for i in range(self.b6))
        except KeyError:
            return "Unable to decode data"