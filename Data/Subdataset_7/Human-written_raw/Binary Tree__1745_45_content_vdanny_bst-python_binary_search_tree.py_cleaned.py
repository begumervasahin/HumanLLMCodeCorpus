import sys
class class1:
    def fonk1(self, b2):
        self.b1 = self.b5 = None
        self.b2 = b2
class class2:
    def fonk2(self, b3, b2):
        if b3 = = None:
            return class1(b2)
        else:
            if b2 <= b3.b2:
                b4 = self.fonk2(b3.b5, b2)
                b3.b5 = b4
            else:
                b4 = self.fonk2(b3.b1, b2)
                b3.b1 = b4
        return b3
    def fonk3(self,b3):
        if b3 = = None:
            return -1
        else:
            b5 = self.fonk3(b3.b5)
            b1 = self.fonk3(b3.b1)
            if b5 > b1:
                return b5 + 1
            else:
                return b1 + 1
    def fonk4(self, b3):
        if b3 != None:
            self.fonk4(b3.b5)
            sys.stdout.write(str(b3.b2) + " ")
            sys.stdout.flush()
            self.fonk4(b3.b1)
    def fonk5(self, b3):
        if b3 != None:
            self.fonk5(b3.b5)
            self.fonk5(b3.b1)
            sys.stdout.write(str(b3.b2) + " ")
            sys.stdout.flush()
    def fonk6(self, b3):
        if b3 != None:
            sys.stdout.write(str(b3.b2) + " ")
            sys.stdout.flush()
            self.fonk6(b3.b5)
            self.fonk6(b3.b1)
    b6 = []
    def fonk7(self, b3):
        if b3 != None:
            self.b6.append(b3)
            a1 = 0
            b4 = self.b6[a1]
            while b4 != None:
                sys.stdout.write(str(b4.b2) + " ")
                sys.stdout.flush()
                if b4.b5 != None:
                    self.b6.append(b4.b5)
                if b4.b1 != None:
                    self.b6.append(b4.b1)
                a1+=1
                if a1 < len(self.b6):
                    b4 = self.b6[a1]
                else:
                    b4 = None