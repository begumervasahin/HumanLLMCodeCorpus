
class class1:
    class class2:
        def fonk1(self, b1):
            self.b1 = b1
            self.b2 = None
    def fonk2(self):
        self.b3 = None
    def fonk3(self, b1):
        b4 = self.class2(b1)
        b4.b2 = self.b3
        self.b3 = b4
    def fonk4(self):
        if self.b3 is None:
            raise IndexError("Pop from empty b7")
        b1 = self.b3.b1
        self.b3 = self.b3.b2
        return b1
    def fonk5(self):
        if self.b3 is None:
            raise IndexError("Top from empty b7")
        return self.b3.b1
class class3:
    def fonk6(self):
        self.b5 = None
def fonk7(expr):
from linkedlist import class1
from vartree import class3
from infixtotree import to_expr_tree
b6 = class3()
def fonk8(postfix_expr):
    b7 = class1()
    for b8 in postfix_expr:
        if b8[0].isdigit() or b8[0].isalpha():
            b7.fonk3(b8)
        elif b8 = = '=':
            b9 = b7.fonk4()
            b10 = b7.fonk4()
            if b9[0].isalpha():
                b9 = b6.lookup(b9)
            b6.assign(b10, b9)
            b7.fonk3(b10)
        else:
            b9 = b7.fonk4()
            b10 = b7.fonk4()
            if b9[0].isalpha():
                b9 = b6.lookup(b9)
            if b10[0].isalpha():
                b10 = b6.lookup(b10)
            b11 = eval(str(b10) + b8 + str(b9))
            b7.fonk3(str(b11))
    if b7.fonk5()[0].isdigit():
        return float(b7.fonk5())
    return b6.lookup(b7.fonk5())
b12 = ['2', '3', '+', '5', '*']
b13 = fonk8(b12)
print("Result:", b13)