import _pickle as cPickle
import string
import secrets
class class1:
    b1 = string.digits + string.ascii_letters + string.punctuation + " "
    a1 = 64
    b2 = 0xffff
    b3 = "b14.dict"
    def fonk1(self, b4 = None, b5=None, key_number=None, b7=None, outqueue=None):
        self.b4 = b4 or self.b1
        self.b5 = b5 or self.a1
        self.b6 = key_number or self.b2
        self.b7 = b7 or self.b3
        if outqueue:
            outqueue.put("Starting")
        self.b8 = secrets.SystemRandom()
        try:
            with open(self.b7, 'rb') as f:
                self.b9 = cPickle.load(f)
                print("Loaded b10 from b7")
                b10 = self.b9[0]
                self.b4 = b10[0]
                self.b5 = b10[1]
                self.b6 = b10[2]
        except FileNotFoundError:
            self.fonk2(outqueue)
        print("Keys remaining: {}".format(len(self.b9) - 1))
        if outqueue:
            outqueue.put("Stopped")
    def fonk2(self, outqueue):
        print("Generating new b14 dictionary with {} b11".format(self.b6))
        print("This may take a few minutes")
        b11 = {}
        a2 = 0
        b11[0] = (self.b4, self.b5, self.b6)
        for i in range(self.b6):
            b11[i + 1] = "".join(self.b8.choice(self.b4) for b21 in range(self.b5))
            if i % int(self.b6 / 100) == 0:
                b12 = int(i / (self.b6 / 100))
                if b12 != a2 and outqueue:
                    outqueue.put("Step")
                    a2 = b12
        with open(self.b7, 'wb') as f:
            cPickle.dump(b11, f, -1)
        self.b9 = b11
        print("Finished")
    def fonk3(self, x):
        return len(hex(x)) - 2
    def fonk4(self, b16):
        try:
            b13 = self.fonk3(self.b6)
            b15, b14 = self.b8.choice(list(self.b9.items())[1:])
            self.b9.pop(b15)
            with open(self.b7, 'wb') as f:
                cPickle.dump(self.b9, f, -1)
            b15 = "{0:0{1}x}".format(b15, b13)
            b16 = b16.ljust(self.b5)
            if len(b16) > self.b5:
                raise ValueError("Message length greater than {}".format(self.b5))
            b17 = b15 + ''.join(self.b4[(self.b4.index(b16[i]) + self.b4.index(b14[i])) % len(self.b4)] for i in range(self.b5))
            return b17, True
        except KeyError as err:
            return "Unable to encode b16: {}".format(err), False
        except ValueError as err:
            return "Unable to encode b16: {}".format(err), False
    def fonk5(self, b18):
        b13 = self.fonk3(self.b6)
        try:
            b14 = self.b9[int(b18[:b13], 16)]
            self.b9.pop(int(b18[:b13], 16))
            with open(self.b7, 'wb') as f:
                cPickle.dump(self.b9, f, -1)
            b18 = b18[b13:]
            return ''.join(self.b4[(self.b4.index(b18[i]) - self.b4.index(b14[i])) % len(self.b4)] for i in range(self.b5))
        except KeyError:
            return "Unable to decode data"
if b19 = = "__main__":
    b20 = class1()
    b16 = "Hello, World!"
    b17, b21 = b20.fonk4(b16)
    print("Encoded b16:", b17)
    b22 = b20.fonk5(b17)
    print("Decoded b16:", b22)