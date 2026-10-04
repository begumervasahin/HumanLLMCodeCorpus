from linkedlist import LinkedList
from vartree import binarySearchTree
from infixtotree import to_expr_tree
b1 = binarySearchTree()
def fonk1(b9):
    b2 = LinkedList()
    for b3 in b9:
        if b3[0].isdigit() or b3[0].isalpha():
            b2.push(b3)
        elif b3 = = '=':
            b4 = b2.pop()
            b5 = b2.pop()
            if b4[0].isalpha():
                b4 = b1.lookup(b4)
            b1.assign(b5, b4)
            b2.push(b5)
        else:
            b4 = b2.pop()
            b5 = b2.pop()
            if b4[0].isalpha():
                b4 = b1.lookup(b4)
            if b5[0].isalpha():
                b5 = b1.lookup(b5)
            b6 = eval(f"{b5} {b3} {b4}")
            b2.push(str(b6))
    b7 = b2.b4()
    if b7[0].isdigit():
        return float(b7)
    return b1.lookup(b7)
if b8 = = "__main__":
    b9 = ['12', '3', '*', '5', '+', 'a', '=']
    b6 = fonk1(b9)
    print("Result:", b6)