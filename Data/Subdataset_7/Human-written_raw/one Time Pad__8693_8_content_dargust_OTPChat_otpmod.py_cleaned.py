import _pickle as cPickle
import string
import secrets
class class1():
    b1 = string.digits+string.ascii_letters+string.punctuation+" "
    a1 = 64
    b2 = 0xffff
    b3 = "key.dict"
    def fonk1(self, b4 = string.digits+string.ascii_letters+string.punctuation+" ", message_length=64, key_number=0xffff, b8="key.dict", b9=None):
        self.b5 = self.b1
        self.b6 = message_length
        self.b7 = key_number
        self.b8 = b8
        if not b9 = = None:
            b9.put("Starting")
        self.b10 = secrets.SystemRandom()
        try:
            with open(self.b8,'rb') as f:
                self.b11 = cPickle.load(f)
                print("Taking dictionary b12 from b8")
                b12 = self.b11[0]
                self.b5 = b12[0]
                self.b6 = b12[1]
                self.b7 = b12[2]
        except FileNotFoundError:
            self.fonk2(b9)
        print("b13 remaining: {}".format(len(self.b11)-1))
        if not b9 = = None:
            b9.put("Stopped")
    def fonk2(self, b9):
        print("Generating new key dictionary with {} b13".format(self.b7))
        print("This may take b5 few minutes")
        b13 = {}
        a2 = 0
        b13[0] = (self.b5, self.b6, self.b7)
        for i in range(self.b7):
            b13[i+1] = "".join(self.b10.choice(self.b5) for i in range(self.b6))
            if i%int(self.b7/100) == 0:
                b14 = int(i/(self.b7/100))
                if not b14 = = a2 and not b9 == None:
                    b9.put("Step")
                    a2 = b14
        with open(self.b8,'wb') as f:
            cPickle.dump(b13, f, -1)
        self.b11 = b13
        print("Finished")
    def fonk3(self, x):
        return(len(hex(x))-2)
    def fonk4(self,b18):
        try:
            b15 = self.fonk3(self.b7)
            b17, b16 = self.b10.choice(list(self.b11.items())[1:])
            self.b11.pop(b17)
            with open(self.b8,'wb') as f:
                cPickle.dump(self.b11, f, -1)
            b17 = "{0:0{1}x}".format(b17,b15)
            b18 = b18.ljust(self.b6)
            if len(b18)>self.b6:
                raise ValueError("b19 length greater than {}".format(self.b6))
            b19 = b17+''.join(self.b5[(self.b5.index(b18[i])+self.b5.index(b16[i]))%len(self.b5)] for i in range(self.b6))
            return(b19, True)
        except KeyError as err:
            return("Unable to encode b19: {}".format(err), False)
        except ValueError as err:
            return("Unable to encode b19: {}".format(err), False)
    def fonk5(self,b20):
        b15 = self.fonk3(self.b7)
        try:
            b16 = self.b11[int(b20[:b15],16)]
            self.b11.pop(int(b20[:b15],16))
            with open(self.b8,'wb') as f:
                cPickle.dump(self.b11, f, -1)
            b20 = b20[b15:]
            return(''.join(self.b5[(self.b5.index(b20[i])-self.b5.index(b16[i]))%len(self.b5)] for i in range(self.b6)))
        except KeyError:
            return("Unable to decode data")