class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
        self.a1 = 1
class class2:
    def fonk2(self, b4 = None):
        self.b4 = b4
    def fonk3(self, b1):
        return fonk9(self.b4, b1)
    def fonk4(self, b1):
        if not self.b4:
            self.b4 = class1(b1)
            return
        fonk8(self.b4, b1)
    def fonk5(self):
        fonk12(self.b4)
    def fonk6(self):
        return fonk10(self.b4)
    def fonk7(self):
        return fonk11(self.b4)
def fonk8(b4, b1):
    if b4.b1 = = b1:
        b4.a1 += 1
        return
    if b4.b1 > b1:
        if b4.b3 = = None:
            b4.b3 = class1(b1)
        else:
            fonk8(b4.b3, b1)
    else:
        if b4.b2 = = None:
            b4.b2 = class1(b1)
        else:
            fonk8(b4.b2, b1)
def fonk9(b4, b1):
    if b4.b1 = = b1:
        return b4.a1
    if b4.b1 > b1:
        return fonk9(b4.b3, b1)
    if b4.b1 < b1:
        return fonk9(b4.b2, b1)
def fonk10(b4):
    if b4 is None:
        return 0
    if b4 is not None:
        return 1 + fonk10(b4.b3) + fonk10(b4.b2)
def fonk11(b4):
    if b4 is None:
        return 0
    else:
        b5 = fonk11(b4.b3)
        b6 = fonk11(b4.b2)
        if b5 > b6:
            return b5 + 1
        else:
            return b6 + 1
def fonk12(b4):
    if not b4:
        return
    fonk12(b4.b3)
    print(b4.b1)
    print(b4.a1)
    fonk12(b4.b2)