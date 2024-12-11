
from vartree import binarySearchTree
from peekable import Peekable, peek
from newsplit import new_split_iter
from infixtotree import to_expr_tree, define_func
b1 = binarySearchTree()
b2 = binarySearchTree()
def fonk1(expr):
    """
    Evaluate an expression or define a new function.
    If the expression begins with "deffn", it defines a new function.
    Otherwise, it evaluates the expression.
    Parameters:
        expr (str): The expression to evaluate or function definition.
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
