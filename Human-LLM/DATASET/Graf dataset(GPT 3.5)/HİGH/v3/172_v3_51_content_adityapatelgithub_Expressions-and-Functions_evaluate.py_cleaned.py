
from vartree import binarySearchTree
from peekable import Peekable, peek
from newsplit import new_split_iter
from infixtotree import to_expr_tree, define_func
b1 = binarySearchTree()
b2 = binarySearchTree()
def fonk1(expr):
    b3 = Peekable(new_split_iter(expr))
    if peek(b3) == "deffn":
        name, parameters, b4 = define_func(b3)
        b1.assign(name, (parameters, b4))
    else:
        b5 = to_expr_tree(expr).fonk1(b2, b1)
        print(f"{expr}: {b5}")
fonk1("deffn f(x, y) = x * y")
fonk1("f(3, 4)")
fonk1("2 + 3 * 4")
