from vartree import binarySearchTree
from peekable import Peekable, peek
from newsplit import new_split_iter
from infixtotree import to_expr_tree, define_func
class class1:
    def fonk1(self):
        self.b1 = binarySearchTree()
        self.b2 = binarySearchTree()
    def fonk2(self, expr):
        """
        Define a new function or evaluate an expression.
        If the first word in the line is "deffn", it should appear as:
            deffn <function name> ( <parameters> ) = <function b4>
        A VarTree will associate the function name with:
            a list of parameters (at least one, maybe more)
            and a tree representing the function b4.
        Otherwise, the input line is evaluated in an expression tree.
        :param expr: Expression to evaluate or define as a function
        """
        b3 = Peekable(new_split_iter(expr))
        if peek(b3) == "deffn":
            name, params, b4 = define_func(b3)
            self.b1.assign(name, (params, b4))
        else:
            b5 = to_expr_tree(expr).fonk2(self.b2, self.b1)
            print(f"{expr} : {b5}")
def fonk3():
    b6 = class1()
    b6.fonk2("deffn add (x, y) = x + y")
    b6.fonk2("add(3, 4)")
if b7 = = "__main__":
    fonk3()