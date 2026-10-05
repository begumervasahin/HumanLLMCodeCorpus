class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
    def fonk2(self, data):
        if self.b1 = = data:
            return False
        elif self.b1 > data:
            if self.b2:
                return self.b2.fonk8(data)
            else:
                self.b2 = class1(data)
                return True
        else:
            if self.b3:
                return self.b3.fonk8(data)
            else:
                self.b3 = class1(data)
                return True
    def fonk3(self, data):
        if self.b1 = = data:
            return True
        elif self.b1 > data:
            if self.b2:
                return self.b2.fonk9(data)
            else:
                return False
        else:
            if self.b3:
                return self.b3.fonk9(data)
            else:
                return False
    def fonk4(self):
        if self:
            print(str(self.b1))
            if self.b2:
                self.b2.fonk10()
            if self.b3:
                self.b3.fonk10()
    def fonk5(self):
        if self:
            if self.b2:
                self.b2.fonk11()
            print(str(self.b1))
            if self.b3:
                self.b3.fonk11()
    def fonk6(self):
        if self:
            if self.b2:
                self.b2.fonk12()
            if self.b3:
                self.b3.fonk12()
            print(str(self.b1))
class class2:
    def fonk7(self):
        self.b4 = None
    def fonk8(self, data):
        if self.b4:
            return self.b4.fonk8(data)
        else:
            self.b4 = class1(data)
            return True
    def fonk9(self, data):
        if self.b4:
            return self.b4.fonk9(data)
        else:
            return False
    def fonk10(self):
        print("Preorder:")
        if self.b4:
            self.b4.fonk10()
    def fonk11(self):
        print("Inorder:")
        if self.b4:
            self.b4.fonk11()
    def fonk12(self):
        print("Postorder:")
        if self.b4:
            self.b4.fonk12()
b5 = class2()
b5.fonk8(1)
b5.fonk8(2)
b5.fonk8(3)
b5.fonk10()
b5.fonk12()
b5.fonk11()