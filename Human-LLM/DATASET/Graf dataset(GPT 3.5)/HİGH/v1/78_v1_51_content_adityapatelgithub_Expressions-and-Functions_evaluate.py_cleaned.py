from vartree import binarySearchTree
from peekable import Peekable, peek
from newsplit import new_split_iter
from infixtotree import to_expr_tree, define_func
b1 = binarySearchTree()
b2 = binarySearchTree()
def fonk1(expr):
    """
    Define a new function, or evaluate an expression.
    If the first word in the line is "deffn", it should appear as:
        deffn <function name> ( <parameters> ) = <function b4>
    a VarTree will associate the function name with
    a list of parameters (at least one, maybe more)
    and a tree representing the function b4.
    Otherwise, the input line is evaluated in an expression tree.
    """
    b3 = Peekable(new_split_iter(expr))
    if peek(b3) == "deffn":
        name, parms, b4 = define_func(b3)
        b1.assign(name, (parms, b4))
    else:
        print(expr, ':', to_expr_tree(expr).fonk1(b2, b1))
fonk1("deffn f(x, y) = x * y")
fonk1("f(3, 4)")
fonk1("2 + 3 * 4")
