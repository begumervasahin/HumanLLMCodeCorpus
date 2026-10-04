import datetime
from random import randint
class class1:
    def fonk1(self, val):
        self.b1 = val
        self.b2 = None
        self.b3 = None
    def fonk2(self, data):
        if self.b1 = = data:
            return False
        elif data < self.b1:
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
        elif data < self.b1:
            return self.b2.fonk9(data) if self.b2 else False
        else:
            return self.b3.fonk9(data) if self.b3 else False
    def fonk4(self):
        if self:
            print(self.b1)
            if self.b2:
                self.b2.fonk10()
            if self.b3:
                self.b3.fonk10()
    def fonk5(self):
        if self:
            if self.b2:
                self.b2.fonk11()
            if self.b3:
                self.b3.fonk11()
            print(self.b1)
    def fonk6(self):
        if self:
            if self.b2:
                self.b2.fonk12()
            print(self.b1)
            if self.b3:
                self.b3.fonk12()
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
        return self.b4.fonk9(data) if self.b4 else False
    def fonk10(self):
        print("PreOrder Traversal:")
        if self.b4:
            self.b4.fonk10()
        else:
            print("class2 is empty")
    def fonk11(self):
        print("PostOrder Traversal:")
        if self.b4:
            self.b4.fonk11()
        else:
            print("class2 is empty")
    def fonk12(self):
        print("InOrder Traversal:")
        if self.b4:
            self.b4.fonk12()
        else:
            print("class2 is empty")
def fonk13():
    b5 = class2()
    a1 = 10000
    b6 = datetime.datetime.now()
    for _ in range(a1):
        b5.fonk8(randint(0, 20000))
    b7 = datetime.datetime.now()
    print(f"Time to insert {a1} nodes: {(b7 - b6).total_seconds()} seconds")
    b6 = datetime.datetime.now()
    b5.fonk12()
    b7 = datetime.datetime.now()
    print(f"Time to traverse in-order: {(b7 - b6).total_seconds()} seconds")
if b8 = = "__main__":
    fonk13()