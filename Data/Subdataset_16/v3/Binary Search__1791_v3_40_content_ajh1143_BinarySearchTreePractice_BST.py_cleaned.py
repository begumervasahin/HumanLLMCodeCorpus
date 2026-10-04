class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
    def fonk2(self, b4):
        if b4 = = self.b1:
            return False
        elif b4 < self.b1:
            if self.b2:
                return self.b2.fonk8(b4)
            else:
                self.b2 = class1(b4)
                return True
        else:
            if self.b3:
                return self.b3.fonk8(b4)
            else:
                self.b3 = class1(b4)
                return True
    def fonk3(self, b4):
        if b4 = = self.b1:
            return True
        elif b4 < self.b1:
            return self.b2.fonk9(b4) if self.b2 else False
        else:
            return self.b3.fonk9(b4) if self.b3 else False
    def fonk4(self):
        print(self.b1)
        if self.b2:
            self.b2.fonk10()
        if self.b3:
            self.b3.fonk10()
    def fonk5(self):
        if self.b2:
            self.b2.fonk11()
        print(self.b1)
        if self.b3:
            self.b3.fonk11()
    def fonk6(self):
        if self.b2:
            self.b2.fonk12()
        if self.b3:
            self.b3.fonk12()
        print(self.b1)
class class2:
    def fonk7(self):
        self.b5 = None
    def fonk8(self, b4):
        if self.b5:
            return self.b5.fonk8(b4)
        else:
            self.b5 = class1(b4)
            return True
    def fonk9(self, b4):
        return self.b5.fonk9(b4) if self.b5 else False
    def fonk10(self):
        if self.b5:
            print("Preorder traversal:")
            self.b5.fonk10()
    def fonk11(self):
        if self.b5:
            print("Inorder traversal:")
            self.b5.fonk11()
    def fonk12(self):
        if self.b5:
            print("Postorder traversal:")
            self.b5.fonk12()
if b6 = = "__main__":
    b7 = class2()
    b7.fonk8(1)
    b7.fonk8(2)
    b7.fonk8(3)
    b7.fonk10()
    b7.fonk11()
    b7.fonk12()