import _pickle as cPickle
import string
import secrets
class class1:
    def fonk1(self, b1 = None, b5=None, key_number=None, b7=None, outqueue=None):
        self.b2 = string.digits + string.ascii_letters + string.punctuation + " "
        self.a1 = 64
        self.b3 = 0xffff
        self.b4 = "b11.dict"
        self.b1 = b1 if b1 else self.b2
        self.b5 = b5 if b5 else self.a1
        self.b6 = key_number if key_number else self.b3
        self.b7 = b7 if b7 else self.b4
        if outqueue:
            outqueue.put("Starting")
        self.b8 = secrets.SystemRandom()
        try:
            with open(self.b7, 'rb') as f:
                self.b9 = cPickle.load(f)
                print("Loaded dictionary b10 from b7")
                self.fonk2()
        except FileNotFoundError:
            self.fonk3(outqueue)
        print("Keys remaining: {}".format(len(self.b9) - 1))
        if outqueue:
            outqueue.put("Stopped")
    def fonk2(self):
        b10 = self.b9[0]
        self.b1, self.b5, self.b6 = b10
    def fonk3(self, outqueue):
        print("Generating a new b11 dictionary with {} keys".format(self.b6))
        print("This may take a few minutes")
        self.b9 = {0: (self.b1, self.b5, self.b6)}
        a2 = 0
        for i in range(self.b6):
            b11 = "".join(self.b8.choice(self.b1) for _ in range(self.b5))
            self.b9[i + 1] = b11
            if i % int(self.b6 / 100) == 0:
                b12 = int(i / (self.b6 / 100))
                if b12 != a2 and outqueue:
                    outqueue.put("Step")
                    a2 = b12
        with open(self.b7, 'wb') as f:
            cPickle.dump(self.b9, f, -1)
        print("Key dictionary generation complete")
    def fonk4(self):
        return len(hex(self.b6)) - 2
    def fonk5(self, b15):
        try:
            b13 = self.fonk4()
            b14, b11 = self.b8.choice(list(self.b9.items())[1:])
            self.b9.pop(b14)
            with open(self.b7, 'wb') as f:
                cPickle.dump(self.b9, f, -1)
            b14 = "{0:0{1}x}".format(b14, b13)
            b15 = b15.ljust(self.b5)
            if len(b15) > self.b5:
                raise ValueError("Message length exceeds {}".format(self.b5))
            b16 = b14 + ''.join(self.b1[(self.b1.index(b15[i]) + self.b1.index(b11[i])) % len(self.b1)] for i in range(self.b5))
            return b16, True
        except (KeyError, ValueError) as err:
            return "Unable to encode b15: {}".format(err), False
    def fonk6(self, b17):
        b13 = self.fonk4()
        try:
            b11 = self.b9[int(b17[:b13], 16)]
            self.b9.pop(int(b17[:b13], 16))
            with open(self.b7, 'wb') as f:
                cPickle.dump(self.b9, f, -1)
            b17 = b17[b13:]
            return ''.join(self.b1[(self.b1.index(b17[i]) - self.b1.index(b11[i])) % len(self.b1)] for i in range(self.b5))
        except KeyError:
            return "Unable to decode b17"