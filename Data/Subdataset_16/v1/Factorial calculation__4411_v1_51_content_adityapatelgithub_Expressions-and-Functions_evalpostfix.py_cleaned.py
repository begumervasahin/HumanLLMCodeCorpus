from linkedlist import LinkedList
from vartree import BinarySearchTree
from infixtotree import to_expr_tree
class class1(BinarySearchTree):
    def fonk1(self, variable, value):
        self.insert(variable, value)
    def fonk2(self, variable):
        b1 = self.search(variable)
        if b1:
            return b1.value
        raise ValueError(f"Variable '{variable}' not found in the tree")
b2 = class1()
def fonk3(postfixExpr):
    b3 = LinkedList()
    for b4 in postfixExpr:
        if b4[0].isdigit() or b4[0].isalpha():
            b3.push(b4)
        elif b4 = = '=':
            b5 = b3.pop()
            b6 = b3.pop()
            if b5[0].isalpha():
                b5 = b2.fonk2(b5)
            b2.fonk1(b6, b5)
            b3.push(b6)
        else:
            b5 = b3.pop()
            b6 = b3.pop()
            if b5[0].isalpha():
                b5 = b2.fonk2(b5)
            if b6[0].isalpha():
                b6 = b2.fonk2(b6)
            b7 = eval(f"{b6} {b4} {b5}")
            b3.push(str(b7))
    b8 = b3.b5()
    if b8[0].isdigit():
        return float(b8)
    return b2.fonk2(b8)
if b9 = = "__main__":
    b10 = ['12', '3', '*', '5', '+', 'a', '=']
    b8 = fonk3(b10)
    print("Result:", b8)