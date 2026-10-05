import _pickle as cPickle
import string
import secrets
class class1:
    b1 = string.digits + string.ascii_letters + string.punctuation + " "
    a1 = 64
    b2 = 0xffff
    b3 = "b12.dict"
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
                self.fonk2(f)
        except FileNotFoundError:
            self.fonk3(outqueue)
        print("Keys remaining: {}".format(len(self.b9) - 1))
        if outqueue:
            outqueue.put("Stopped")
    def fonk2(self, f):
        self.b9 = cPickle.load(f)
        print("Loaded b10 from b7")
        b10 = self.b9[0]
        self.b4, self.b5, self.b6 = b10
    def fonk3(self, outqueue):
        print("Generating new b12 dictionary with {} b11".format(self.b6))
        print("This may take a few minutes")
        b11 = {0: (self.b4, self.b5, self.b6)}
        for i in range(self.b6):
            b11[i + 1] = "".join(self.b8.choice(self.b4) for b19 in range(self.b5))
            if i % int(self.b6 / 100) == 0 and outqueue:
                outqueue.put("Step")
        with open(self.b7, 'wb') as f:
            cPickle.dump(b11, f, -1)
        self.b9 = b11
        print("Finished")
    def fonk4(self, x):
        return len(hex(x)) - 2
    def fonk5(self, b14):
        try:
            b13, b12 = self.fonk6()
            b13 = self.fonk7(b13)
            b14 = self.fonk8(b14)
            b15 = self.fonk9(b14, b12)
            return b13 + b15, True
        except (KeyError, ValueError) as err:
            return f"Unable to encode b14: {err}", False
    def fonk6(self):
        b13, b12 = self.b8.choice(list(self.b9.items())[1:])
        self.b9.pop(b13)
        with open(self.b7, 'wb') as f:
            cPickle.dump(self.b9, f, -1)
        return b13, b12
    def fonk7(self, b13):
        b16 = self.fonk4(self.b6)
        return "{0:0{1}x}".format(b13, b16)
    def fonk8(self, b14):
        return b14.ljust(self.b5)
    def fonk9(self, b14, b12):
        return ''.join(self.b4[(self.b4.index(b14[i]) + self.b4.index(b12[i])) % len(self.b4)] for i in range(self.b5))
    def fonk10(self, encoded_data):
        try:
            key_prefix, b15 = encoded_data[:self.fonk4(self.b6)], encoded_data[self.fonk4(self.b6):]
            b12 = self.fonk11(int(key_prefix, 16))
            return self.fonk12(b15, b12)
        except KeyError:
            return "Unable to decode data"
    def fonk11(self, b13):
        b12 = self.b9[b13]
        self.b9.pop(b13)
        with open(self.b7, 'wb') as f:
            cPickle.dump(self.b9, f, -1)
        return b12
    def fonk12(self, encoded_data, b12):
        return ''.join(self.b4[(self.b4.index(encoded_data[i]) - self.b4.index(b12[i])) % len(self.b4)] for i in range(self.b5))
if b17 = = "__main__":
    b18 = class1()
    b14 = "Hello, World!"
    b15, b19 = b18.fonk5(b14)
    print("Encoded b14:", b15)
    b20 = b18.fonk10(b15)
    print("Decoded b14:", b20)