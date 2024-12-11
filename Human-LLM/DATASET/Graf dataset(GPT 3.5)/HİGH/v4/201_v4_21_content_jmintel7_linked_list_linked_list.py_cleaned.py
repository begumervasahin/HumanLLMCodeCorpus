class class1:
    def fonk1(self, b1 = None):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self):
        self.b3 = class1()
    def fonk3(self, b1):
        b4 = class1(b1)
        b5 = self.b3
        while b5.b2 is not None:
            b5 = b5.b2
        b5.b2 = b4
    def fonk4(self):
        b5 = self.b3
        a1 = 0
        while b5.b2 is not None:
            b5 = b5.b2
            a1 += 1
        return a1
    def fonk5(self):
        b5 = self.b3
        b6 = []
        a2 = 0
        while b5.b2 is not None:
            if b5.b1:
                b6.fonk3(b5.b1[0])
            b5 = b5.b2
        return b6
    def fonk6(self, b7):
        b5 = self.b3
        while b5.b2 is not None:
            b5 = b5.b2
            b1 = b5.b1
            if b1.b7 = = b7:
                return b1
        print('Student with the roll no does not exist')
        return None
    def fonk7(self, b7):
        b5 = self.b3
        while b5.b2 is not None:
            b8 = b5
            b5 = b5.b2
            b1 = b5.b1
            if b1.b7 = = b7:
                b8.b2 = b5.b2
                print('Record erased')
                return
        print('Student with the roll no does not exist')
    def fonk8(self, index):
        if index >= self.fonk4():
            print('ERROR: Index out of range')
            return None
        b5 = self.b3
        for i in range(index + 1):
            b5 = b5.b2
        return b5.b1
    def fonk9(self, index):
        if index >= self.fonk4():
            print('ERROR: Index out of range')
            return None
        b5 = self.b3
        for i in range(index + 1):
            b8 = b5
            b5 = b5.b2
        b8.b2 = b5.b2