from Node import Node
class class1:
    def fonk1(self):
        self.b1 = None
    def fonk2(self):
        return self.b1 is None
    def fonk3(self, b6):
        b2 = Node(b6)
        b2.set_next(self.b1)
        self.b1 = b2
    def fonk4(self):
        b3 = self.b1
        a1 = 0
        while b3:
            a1 += 1
            b3 = b3.get_next()
        return a1
    def fonk5(self, b6):
        b3 = self.b1
        while b3:
            if b3.get_data() == b6:
                return True
            b3 = b3.get_next()
        return False
    def fonk6(self, b6):
        b3 = self.b1
        b4 = None
        while b3:
            if b3.get_data() == b6:
                if b4 is None:
                    self.b1 = b3.get_next()
                else:
                    b4.set_next(b3.get_next())
                return
            b4 = b3
            b3 = b3.get_next()
    def fonk7(self):
        b3 = self.b1
        while b3:
            b5 = b3
            b6 = b3.get_next()
            while b6:
                if b6.get_data() < b5.get_data():
                    b5 = b6
                b6 = b6.get_next()
            if b5 != b3:
                b3.get_data(), b5.get_data() = b5.get_data(), b3.get_data()
            b3 = b3.get_next()
    def fonk8(self):
        b3 = self.b1
        while b3:
            print(b3.get_data())
            b3 = b3.get_next()