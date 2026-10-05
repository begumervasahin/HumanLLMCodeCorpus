from Node import Node
class class1:
    def fonk1(self):
        self.b1 = None
        self.b2 = None
        self.a1 = 0
    def fonk2(self):
        return self.b1 is None
    def fonk3(self, item):
        b3 = Node(item)
        b3.b4 = self.b1
        if self.b1 is None:
            self.b2 = b3
        self.b1 = b3
        self.a1 += 1
    def fonk4(self, item):
        b3 = Node(item)
        b3.b4 = None
        b5 = self.b2
        b6 = None
        while b5 is not None:
            if b5.b7 > item:
                break
            else:
                b6 = b5
                b5 = b5.b4
        if b6 is None:
            b3.b4 = self.b2
            self.b2 = b3
        else:
            b3.b4 = b5
            b6.b4 = b3
    def fonk5(self):
        b5 = self.b1
        a2 = 0
        while b5 is not None:
            a2 += 1
            b5 = b5.b4
        return a2
    def fonk6(self, item):
        b5 = self.b1
        while b5 is not None:
            if b5.b7 = = item:
                return True
            b5 = b5.b4
        return False
    def fonk7(self, item):
        b5 = self.b1
        b6 = None
        b8 = False
        while not b8:
            if b5.b7 = = item:
                b8 = True
            else:
                b6 = b5
                b5 = b5.b4
        if b6 is None:
            self.b1 = b5.b4
        else:
            b6.b4 = b5.b4
        self.a1 -= 1