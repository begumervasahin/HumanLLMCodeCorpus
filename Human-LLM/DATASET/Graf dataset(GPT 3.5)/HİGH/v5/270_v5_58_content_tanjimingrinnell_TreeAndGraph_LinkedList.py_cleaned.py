class class1:
    def fonk1(self, b1 = None, next_node=None):
        self.b1 = b1
        self.b2 = next_node
    def fonk2(self):
        return f'class1 [{self.b1}]'
class class2:
    def fonk3(self):
        self.b3 = None
        self.b4 = None
    def fonk4(self, b1):
        b5 = class1(b1)
        if self.b3 is None:
            self.b3 = b5
            self.b4 = b5
        else:
            self.b4.b2 = b5
            self.b4 = b5
    def fonk5(self):
        if self.b3:
            b6 = self.b3
            b7 = f'class2 [\n{b6.b1}\n'
            while b6.b2:
                b6 = b6.b2
                b7 += f'{b6.b1}\n'
            return b7 + ']'
        return 'class2 []'
    def fonk6(self):
        self.b3 = None
        self.b4 = None