from Node import Node
class class1:
    def fonk1(self):
        self.b1 = None
    def fonk2(self):
        return self.b1 is None
    def fonk3(self, b8):
        b2 = Node(b8)
        b2.set_next(self.b1)
        self.b1 = b2
    def fonk4(self):
        b3 = self.b1
        a1 = 0
        while b3 is not None:
            a1 += 1
            b3 = b3.get_next()
        return a1
    def fonk5(self, b8):
        b3 = self.b1
        while b3 is not None:
            if b3.get_data() == b8:
                return True
            else:
                b3 = b3.get_next()
        return False
    def fonk6(self, b8):
        b3 = self.b1
        b4 = None
        b5 = False
        while not b5:
            if b3.get_data() == b8:
                b5 = True
                if b4 is None:
                    self.b1 = b3.get_next()
                else:
                    b4.set_next(b3.get_next())
            else:
                b4 = b3
                b3 = b3.get_next()
    def fonk7(self):
        b3 = self.b1
        while b3.get_next() is not None:
            b6 = b3
            b7 = b3.get_data()
            b8 = b3.get_next()
            while b8 is not None:
                if b7 > b8.get_data():
                    b7 = b8.get_data()
                    b6 = b8
                b8 = b8.get_next()
            b6.set_data(b3.get_data())
            b3.set_data(b7)
            b3 = b3.get_next()
    def fonk8(self):
        print(self.b1.get_data())
        b9 = self.b1.get_next()
        print(b9.get_data())
        print(b9.get_next().get_data())
    def fonk9(self):
        b3 = self.b1
        while b3 is not None:
            print(b3.get_data())
            b3 = b3.get_next()