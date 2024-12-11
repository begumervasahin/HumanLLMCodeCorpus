class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
    def fonk2(self, other):
        return self.b1 = = other.b1
class class2:
    def fonk3(self):
        self.b3 = None
    def fonk4(self, node):
        b4 = False
        if self.b3:
            b5 = self.b3
            while b5:
                if b5 = = node:
                    b4 = True
                    break
                b5 = b5.b2
        return b4
    def fonk5(self):
        a1 = 0
        if self.b3:
            b5 = self.b3
            while b5:
                a1 += 1
                b5 = b5.b2
        return a1
    def fonk6(self, node):
        if not self.b3:
            self.b3 = node
            return
        b5 = self.b3
        while b5.b2:
            b5 = b5.b2
        b5.b2 = node
    def fonk7(self, flag_node, node):
        if self.b3 = = flag_node:
            node.b2 = self.b3
            self.b3 = node
        else:
            b6 = self.b3
            while b6.b2:
                if b6.b2 = = flag_node:
                    break
                b6 = b6.b2
            node.b2 = b6.b2
            b6.b2 = node
    def fonk8(self, node):
        if self.b3:
            if self.b3.b1 = = node.b1:
                self.b3 = self.b3.b2
                return
            b6 = self.b3
            while b6.b2:
                if b6.b2 = = node:
                    b6.b2 = node.b2
                    break
                b6 = b6.b2
    def fonk9(self):
        b7 = self.b3
        while b7:
            b9, b8 = b7.b2, b7
            while b9:
                if b9 = = b7:
                    b8.b2 = b9.b2
                else:
                    b8 = b8.b2
                b9 = b9.b2
            b7 = b7.b2
    def fonk10(self):
        if not self.b3 or not self.b3.b2:
            return
        b6, b5 = None, self.b3
        while b5:
            b2 = b5.b2
            b5.b2 = b6
            b6 = b5
            b5 = b2
        self.b3 = b6
    def fonk11(self):
        b5 = self.b3
        while b5:
            print(b5.b1)
            b5 = b5.b2