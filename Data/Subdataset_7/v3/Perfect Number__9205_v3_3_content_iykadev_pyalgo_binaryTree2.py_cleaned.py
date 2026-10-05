class class1:
    def fonk1(self, root_value):
        self.b1 = root_value
        self.b2 = None
        self.b3 = None
    def fonk2(self, new_value):
        if self.b2 is None:
            self.b2 = class1(new_value)
        else:
            b4 = class1(new_value)
            b4.b2 = self.b2
            self.b2 = b4
    def fonk3(self, new_value):
        if self.b3 is None:
            self.b3 = class1(new_value)
        else:
            b4 = class1(new_value)
            b4.b3 = self.b3
            self.b3 = b4
    def fonk4(self):
        return self.b3
    def fonk5(self):
        return self.b2
    def fonk6(self, value):
        self.b1 = value
    def fonk7(self):
        return self.b1
b5 = class1('a')
print("Root value:", b5.fonk7())
print("Left child:", b5.fonk5())
b5.fonk2('b')
print("Left child after insertion:", b5.fonk5())
print("Root value of left child:", b5.fonk5().fonk7())
b5.fonk3('c')
print("Right child:", b5.fonk4())
print("Root value of right child:", b5.fonk4().fonk7())
b5.fonk4().fonk6('hello')
print("Updated root value of right child:", b5.fonk4().fonk7())